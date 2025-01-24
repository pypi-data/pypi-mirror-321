from __future__ import annotations

import os
import shutil
from collections import Counter
from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING, TypeVar

from tree_sitter import Node as TSNode

from graph_sitter.enums import ProgrammingLanguage
from graph_sitter.extensions.utils import find_all_descendants, find_first_descendant, get_all_identifiers
from graph_sitter.typescript.enums import TSFunctionTypeNames

if TYPE_CHECKING:
    from graph_sitter.core.interfaces.editable import Editable
"""
Utility functions for traversing the tree sitter structure.
Do not include language specific traversals, or string manipulations here.
"""


def find_first_function_descendant(node: TSNode) -> TSNode:
    type_names = [function_type.value for function_type in TSFunctionTypeNames]
    return find_first_descendant(node=node, type_names=type_names, max_depth=2)


def find_index(target: TSNode, siblings: list[TSNode]) -> int:
    """Returns the index of the target node in the list of siblings, or -1 if not found. Recursive implementation."""
    if target in siblings:
        return siblings.index(target)

    for i, sibling in enumerate(siblings):
        index = find_index(target, sibling.named_children if target.is_named else sibling.children)
        if index != -1:
            return i
    return -1


def find_first_ancestor(node: TSNode, type_names: list[str], max_depth: int | None = None) -> TSNode | None:
    depth = 0
    while node is not None and (max_depth is None or depth <= max_depth):
        if node.type in type_names:
            return node
        node = node.parent
        depth += 1
    return None


def find_first_child_by_field_name(node: TSNode, field_name: str) -> TSNode | None:
    child = node.child_by_field_name(field_name)
    if child is not None:
        return child
    for child in node.children:
        first_descendant = find_first_child_by_field_name(child, field_name)
        if first_descendant is not None:
            return first_descendant
    return None


def has_descendant(node: TSNode, type_name: str) -> bool:
    def traverse(current_node: TSNode, depth: int = 0) -> bool:
        if current_node.type == type_name:
            return True
        return any(traverse(child, depth + 1) for child in current_node.children)

    return traverse(node)


def get_first_identifier(node: TSNode) -> TSNode | None:
    """Get the text of the first identifier child of a tree-sitter node. Recursive implementation"""
    if node.type in ("identifier", "shorthand_property_identifier_pattern"):
        return node
    for child in node.children:
        output = get_first_identifier(child)
        if output is not None:
            return output
    return None


def descendant_for_byte_range(node: TSNode, start_byte: int, end_byte: int, allow_comment_boundaries: bool = True) -> TSNode | None:
    """Proper implementation of descendant_for_byte_range, which returns the lowest node that contains the byte range."""
    ts_match = node.descendant_for_byte_range(start_byte, end_byte)

    # We don't care if the match overlaps with comments
    if allow_comment_boundaries:
        return ts_match

    # Want to prevent it from matching with part of the match within a comment
    else:
        if not ts_match.children:
            return ts_match
        comments = find_all_descendants(ts_match, "comment")
        # see if any of these comments partially overlaps with the match
        if any(comment.start_byte < start_byte < comment.end_byte or comment.start_byte < end_byte < comment.end_byte for comment in comments):
            return None
        return ts_match


@contextmanager
def shadow_files(files: str | list[str]):
    """Creates shadow copies of the given files. Restores the original files after the context manager is exited.

    Returns list of filenames of shadowed files.
    """
    if isinstance(files, str):
        files = [files]
    shadowed_files = {}
    # Generate shadow file names
    for file_name in files:
        shadow_file_name = file_name + ".gs_internal.bak"
        shadowed_files[file_name] = shadow_file_name
    # Shadow files
    try:
        # Backup the original files
        for file_name, shadow_file_name in shadowed_files.items():
            shutil.copy(file_name, shadow_file_name)
        yield shadowed_files.values()
    finally:
        # Restore the original files
        for file_name, shadow_file_name in shadowed_files.items():
            # If shadow file was created, restore the original file and delete the shadow file
            if os.path.exists(shadow_file_name):
                # Delete the original file if it exists
                if os.path.exists(file_name):
                    os.remove(file_name)
                # Copy the shadow file to the original file path
                shutil.copy(shadow_file_name, file_name)
                # Delete the shadow file
                os.remove(shadow_file_name)


E = TypeVar("E", bound="Editable")


def calculate_base_path(full_path, relative_path):
    """Calculate the base path represented by './' in a relative path.

    :param full_path: The full path to a file or directory
    :param relative_path: A relative path starting with './'
    :return: The base path represented by './' in the relative path
    """
    # Normalize paths to handle different path separators
    full_path = os.path.normpath(full_path)
    relative_path = os.path.normpath(relative_path)

    # Split paths into components
    full_components = full_path.split(os.sep)
    relative_components = relative_path.split(os.sep)

    # Remove './' from the start of relative path if present
    if relative_components[0] == ".":
        relative_components = relative_components[1:]

    # Calculate the number of components to keep from the full path
    keep_components = len(full_components) - len(relative_components)

    # Join the components to form the base path
    base_path = os.sep.join(full_components[:keep_components])

    return base_path


__all__ = [
    "find_all_descendants",
    "find_first_ancestor",
    "find_first_child_by_field_name",
    "find_first_descendant",
    "get_all_identifiers",
    "has_descendant",
]


def get_language_file_extensions(language: ProgrammingLanguage):
    """Returns the file extensions for the given language."""
    from graph_sitter.python import PyFile
    from graph_sitter.typescript.file import TSFile

    if language == ProgrammingLanguage.PYTHON:
        return set(PyFile.get_extensions())
    elif language == ProgrammingLanguage.TYPESCRIPT:
        return set(TSFile.get_extensions())


def determine_project_language(folder_path: str):
    from graph_sitter.python import PyFile
    from graph_sitter.typescript.file import TSFile

    EXTENSIONS = {
        ProgrammingLanguage.PYTHON: PyFile.get_extensions(),
        ProgrammingLanguage.TYPESCRIPT: TSFile.get_extensions(),
    }

    """
    Analyzes a folder to determine the primary programming language based on file extensions.
    Returns the language with the most matching files.

    Args:
        folder_path (str): Path to the folder to analyze

    Returns:
        Optional[ProgrammingLanguage]: The dominant programming language, or None if no matching files found
    """
    folder = Path(folder_path)
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"Invalid folder path: {folder_path}")

    # Initialize counters for each language
    language_counts = Counter()

    # Walk through the directory
    for file_path in folder.rglob("*"):
        # Skip directories and hidden files
        if file_path.is_dir() or file_path.name.startswith("."):
            continue

        # Skip common directories to ignore
        if any(ignore in str(file_path) for ignore in [".git", "node_modules", "__pycache__", "venv", ".env"]):
            continue

        # Count files for each language based on extensions
        for language, exts in EXTENSIONS.items():
            if file_path.suffix in exts:
                language_counts[language] += 1

    # If no files found, return None
    if not language_counts:
        return ProgrammingLanguage.UNSUPPORTED

    # Return the language with the highest count
    return language_counts.most_common(1)[0][0]
