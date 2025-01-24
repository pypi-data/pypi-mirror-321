from __future__ import annotations

from typing import TYPE_CHECKING, Literal, override

from tree_sitter import Node as TSNode

from codegen.utils.codemod.codemod_writer_decorators import apidoc, noapidoc
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.autocommit import commiter, reader
from graph_sitter.core.dataclasses.usage import UsageKind
from graph_sitter.core.expressions.name import Name
from graph_sitter.core.interfaces.callable import Callable
from graph_sitter.core.interfaces.has_attribute import HasAttribute
from graph_sitter.core.interfaces.has_name import HasName
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.placeholder.placeholder_stub import StubPlaceholder
from graph_sitter.enums import ImportType, NodeType
from graph_visualization.enums import VizNode

if TYPE_CHECKING:
    from graph_sitter.core.detached_symbols.parameter import Parameter
    from graph_sitter.core.import_resolution import Import


@apidoc
class ExternalModule(
    Callable,
    HasAttribute["ExternalModule"],
):
    """Represents an external module, like `datetime`, that can be referenced.

    These are only added to the graph during import resolution and will not exist in a local file's
    subgraph. This is because we don't know what an import is referencing or resolves to until we
    see the full codebase.
    """

    node_type: Literal[NodeType.EXTERNAL] = NodeType.EXTERNAL

    def __init__(self, ts_node: TSNode, file_node_id: NodeId, G: CodebaseGraph, import_name: Name) -> None:
        self.node_id = G.add_node(self)
        super().__init__(ts_node, file_node_id, G, None)
        self._name_node = import_name
        self.return_type = StubPlaceholder(parent=self)
        assert self._idx_key not in self.G._ext_module_idx
        self.G._ext_module_idx[self._idx_key] = self.node_id

    @property
    def _idx_key(self) -> str:
        return self.source + "::" + self.name

    @noapidoc
    @commiter
    def parse(self, G: CodebaseGraph) -> None:
        raise NotImplementedError(f"{type(self)} is not part of the graph at the moment")

    @classmethod
    def from_import(cls, imp: Import) -> ExternalModule:
        """Creates an ExternalModule instance from an Import instance.

        This class method creates a new ExternalModule object that represents an external module
        that can be referenced in the codebase, such as 'datetime' or other imported modules.
        External modules are added to the graph during import resolution.

        Args:
            imp (Import): An Import instance containing the module information.

        Returns:
            ExternalModule: A new ExternalModule instance representing the external module.
        """
        return cls(imp.ts_node, imp.file_node_id, imp.G, imp._unique_node)

    @property
    @reader
    def parameters(self) -> list[Parameter]:
        """Returns list of named parameters from an external function symbol.

        Retrieves the parameter list from an external module function. This is not yet implemented and will raise an error.

        Returns:
            list[Parameter]: A list of parameters associated with the external function.

        Raises:
            NotImplementedError: This functionality is not yet supported for external modules.
        """
        # TODO: figure out how to get parameters from this module
        raise NotImplementedError("Parsing parameters from an external module is not yet supported.")

    @reader
    def get_import_string(self, alias: str | None = None, module: str | None = None, import_type: ImportType = ImportType.UNKNOWN, is_type_import: bool = False) -> str:
        """Returns the import string used to import this module.

        Gets the string representation needed to import this external module. This method is used to generate import statements.

        Args:
            alias (str | None, optional): An alternative name for the imported module.
            module (str | None, optional): The module from which to import.
            import_type (ImportType, optional): The type of import to generate. Defaults to ImportType.UNKNOWN.
            is_type_import (bool, optional): Whether this is a type import. Defaults to False.

        Returns:
            str: The import string that can be used to import this module.
        """
        # TODO - will need to fix the relative imports
        return self.source

    @property
    def file(self) -> None:
        """File property for ExternalModule class.

        Returns None since ExternalModule represents an external module that is not part of any local file.

        Returns:
            None: Always returns None as ExternalModule is not associated with any file.
        """
        return None

    @property
    def filepath(self) -> str:
        """Returns the filepath of the module.

        For an ExternalModule, this will always return an empty string as it represents an external module that
        does not belong to the local codebase.

        Returns:
            str: An empty string representing the filepath of the external module.
        """
        return ""

    @property
    @noapidoc
    def viz(self) -> VizNode:
        return VizNode(file_path=self.filepath, start_point=self.start_point, end_point=self.end_point, name=self.name, symbol_name=self.__class__.__name__)

    @noapidoc
    @reader
    def resolve_attribute(self, name: str) -> ExternalModule | None:
        return self

    @noapidoc
    @commiter
    @override
    def _compute_dependencies(self, usage_type: UsageKind | None = None, dest: HasName | None = None) -> None:
        pass

    def __hash__(self):
        if self._hash is None:
            self._hash = hash((self.filepath, self.range, self.ts_node.kind_id, self._idx_key))
        return self._hash

    @reader
    def __eq__(self, other: object):
        if isinstance(other, ExternalModule):
            return super().__eq__(other) and self._idx_key == other._idx_key
        return super().__eq__(other)
