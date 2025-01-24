from collections.abc import Generator, Iterable
from functools import cached_property

from tree_sitter import Node as TSNode

def get_all_identifiers(node: TSNode) -> list[TSNode]:
    """Get all the identifiers in a tree-sitter node. Recursive implementation"""

def iter_all_descendants(node: TSNode, type_names: Iterable[str] | str, max_depth: int | None = None, nested: bool = True) -> Generator[TSNode, None, None]: ...
def find_all_descendants(
    node: TSNode,
    type_names: Iterable[str] | str,
    max_depth: int | None = None,
    nested: bool = True,
) -> list[TSNode]: ...
def find_line_start_and_end_nodes(node: TSNode) -> list[tuple[TSNode, TSNode]]:
    """Returns a list of tuples of the start and end nodes of each line in the node"""

def find_first_descendant(node: TSNode, type_names: list[str], max_depth: int | None = None) -> TSNode | None: ...

cached_property = cached_property

def uncache_all(): ...
