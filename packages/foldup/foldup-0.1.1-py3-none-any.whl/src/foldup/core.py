from pathlib import Path
from typing import List, Tuple

from pathspec import PathSpec

from src.foldup.utils import get_file_extension, is_binary_file, should_exclude


def generate_tree(root_path: Path, pathspec: PathSpec, max_size_mb: float = 1) -> str:
    """
    Generate a tree visualization of the directory structure starting from the root path.

    Args:
        root_path: Path object representing the root directory to start from
        pathspec: PathSpec object for pattern matching
        max_size_mb: Maximum file size in megabytes to include in the tree

    Returns:
        String containing the ASCII tree representation of the directory structure
    """
    tree_str = [str(root_path.name)]

    def add_to_tree(path: Path, prefix: str = "", is_last: bool = True):
        if should_exclude(path, pathspec, max_size_mb):
            return

        # prepare the appropriate prefix for this item
        marker = "└─ " if is_last else "├─ "
        tree_str.append(f"{prefix}{marker}{path.name}")

        if path.is_dir():
            # get all valid items in directory
            items = [
                p
                for p in sorted(path.iterdir())
                if not should_exclude(p, pathspec, max_size_mb)
            ]

            # prepare the prefix for children
            new_prefix = prefix + ("    " if is_last else "│   ")

            # recursively add each item
            for i, item in enumerate(items):
                is_last_item = i == len(items) - 1
                add_to_tree(item, new_prefix, is_last_item)

    # process all root level items
    root_items = [
        p
        for p in sorted(root_path.iterdir())
        if not should_exclude(p, pathspec, max_size_mb)
    ]

    for i, path in enumerate(root_items):
        add_to_tree(path, "", i == len(root_items) - 1)

    return "\n".join(tree_str)


def process_file(file_path: Path, root_path: Path, stats: dict) -> Tuple[str, bool]:
    """
    Process a single file and generate its markdown representation with appropriate code fencing.

    Args:
        file_path: Path to the file being processed
        root_path: Root directory path, used to generate relative paths
        stats: Dictionary to track processing statistics

    Returns:
        Tuple containing:
            - String: Markdown representation of the file
            - Boolean: True if file was successfully processed, False if skipped/error
    """
    rel_path = file_path.relative_to(root_path)
    content = []

    # add file header
    content.append(f"\n# {rel_path}\n")

    # check if file is binary
    if is_binary_file(file_path):
        content.append("```plaintext")
        content.append("<!-- binary file contents omitted -->")
        content.append("```")
        stats["skipped_files"] += 1
        stats["skipped_file_list"].append(str(rel_path))
        return "\n".join(content), False

    # get appropriate language for code fence
    lang = get_file_extension(file_path)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()
            content.append(f"```{lang}")
            content.append(file_content)
            content.append("```")
        return "\n".join(content), True
    except UnicodeDecodeError:
        # handle files that looked like text but aren't
        content.append("```plaintext")
        content.append("<!-- file contents omitted: encoding error -->")
        content.append("```")
        stats["skipped_files"] += 1
        stats["skipped_file_list"].append(str(rel_path))
        return "\n".join(content), False


def generate_markdown(
    root_path: Path,
    pathspec: PathSpec,
    max_size_mb: float = 1,
    tree_only: bool = False,
) -> Tuple[str, dict]:
    """
    Generate the complete markdown document containing tree and optionally file contents.

    Args:
        root_path: Path object representing the root directory to process
        pathspec: PathSpec object for pattern matching
        max_size_mb: Maximum file size in megabytes to include in the output
        tree_only: If True, only generate the project tree without file contents

    Returns:
        Tuple containing:
            - String: The complete markdown document
            - Dict: Processing statistics
    """
    # start with project tree
    content = ["# PROJECT TREE\n"]
    content.append(generate_tree(root_path, pathspec, max_size_mb))

    # initialize stats
    stats = {
        "processed_files": 0,
        "skipped_files": 0,
        "total_size": 0,
        "processed_file_list": [],
        "skipped_file_list": [],
    }

    # if tree_only, return early with just the tree
    if tree_only:
        return "\n".join(content), stats

    def process_directory(path: Path) -> List[str]:
        if should_exclude(path, pathspec, max_size_mb):
            if path.is_file():
                stats["skipped_files"] += 1
                stats["skipped_file_list"].append(str(path.relative_to(root_path)))
            return []

        dir_content = []
        if path.is_file():
            file_content, success = process_file(path, root_path, stats)
            if success:
                stats["processed_files"] += 1
                stats["total_size"] += path.stat().st_size
                stats["processed_file_list"].append(str(path.relative_to(root_path)))
            dir_content.append(file_content)
        else:
            for item in sorted(path.iterdir()):
                dir_content.extend(process_directory(item))

        return dir_content

    # process all files
    content.extend(process_directory(root_path))

    return "\n".join(content), stats
