from abc import abstractmethod
from collections.abc import Generator
from typing import TYPE_CHECKING, Generic, Self, TypeVar

from codegen.utils.codemod.codemod_writer_decorators import noapidoc
from graph_sitter.codebase.resolution_stack import ResolutionStack
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.extensions.utils import cached_property

if TYPE_CHECKING:
    from graph_sitter.core.interfaces.has_attribute import HasAttribute

Parent = TypeVar("Parent", bound="Editable")


@noapidoc
class Chainable(Editable[Parent], Generic[Parent]):
    """Represents a class that can be used as an object in a function call chain."""

    _resolving: bool = False

    @abstractmethod
    def _resolved_types(self) -> Generator["ResolutionStack[Self]", None, None]: ...

    @cached_property
    @noapidoc
    def resolved_type_frames(self) -> list[ResolutionStack["Self"]]:
        """Resolve the definition(s) of this object."""
        if self._resolving:
            return [ResolutionStack(self)]  # Break cycles
        self._resolving = True
        try:
            ret = list(self._resolved_types())
            self.__dict__.pop("resolved_type_frames", None)
            return ret
        finally:
            self._resolving = False

    @noapidoc
    def with_resolution_frame(self, child: Editable, *args, generic_parameters: list | None = None, generics: dict | None = None, **kwargs) -> Generator[ResolutionStack["Self"], None, None]:
        """Resolve the definition(s) of this object."""
        from graph_sitter.core.interfaces.supports_generic import SupportsGenerics

        if isinstance(child, Chainable):
            assert child is not self
            if not child._resolving:
                resolved = child.resolved_type_frames
                if len(resolved) > 0:
                    for resolution in resolved:
                        assert resolution is not self
                        generics = generics or resolution.generics
                        if generic_parameters:
                            if isinstance(resolution.top.node, SupportsGenerics):
                                generics = {k: v for v, k in zip(generic_parameters, resolution.top.node.generics)}
                            elif not generics:
                                generics = {i: v for i, v in enumerate(generic_parameters)}
                        yield resolution.with_frame(self, *args, **kwargs, generics=generics)
                    return
        if generics is None:
            generics = {i: v for i, v in enumerate(generic_parameters)} if generic_parameters else None
        yield ResolutionStack(child).with_frame(self, *args, **kwargs, generics=generics)

    @cached_property
    @noapidoc
    def resolved_types(self) -> list["HasAttribute"]:
        """Resolve the definition(s) of this object.

        Returns type at the top of the resolution stack.
        """
        return list(frame.top.node for frame in self.resolved_type_frames)
