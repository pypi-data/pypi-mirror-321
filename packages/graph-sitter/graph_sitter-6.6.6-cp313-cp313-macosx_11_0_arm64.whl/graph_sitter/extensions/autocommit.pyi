from collections.abc import Callable
from typing import Any, ParamSpec, TypeVar, overload

from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.interfaces.editable import Editable

P = ParamSpec("P")
T = TypeVar("T")

def is_outdated(c) -> bool: ...
@overload
def reader(wrapped: Callable[P, T]) -> Callable[P, T]: ...
@overload
def reader(wrapped: None = None, *, cache: bool | None = ...) -> Callable[[Callable[P, T]], Callable[P, T]]: ...

class AutoCommitMixin:
    """Support for autocommit"""

    autocommit_cache: dict[str, Any]
    removed: bool
    def __init__(self, G: CodebaseGraph) -> None: ...
    def update_generation(self, generation: int | None = None) -> None: ...
    @property
    def is_outdated(self) -> bool: ...
    def is_same_version(self, other: AutoCommitMixin) -> bool: ...

def update_dict(seen: set[Editable], obj: Editable, new_obj: Editable): ...
@overload
def commiter(wrapped: Callable[P, T]) -> Callable[P, T]: ...
@overload
def commiter(wrapped: None = None, *, reset: bool = ...) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
