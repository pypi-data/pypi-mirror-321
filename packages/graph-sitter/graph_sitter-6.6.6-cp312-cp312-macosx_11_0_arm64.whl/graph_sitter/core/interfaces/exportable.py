from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

from rustworkx import NoSuitableNeighbors

from codegen.utils.codemod.codemod_writer_decorators import apidoc
from graph_sitter.core.autocommit import reader
from graph_sitter.core.interfaces.usable import Usable
from graph_sitter.enums import EdgeType, ImportType, NodeType

if TYPE_CHECKING:
    from graph_sitter.core.export import Export
    from graph_sitter.core.interfaces.editable import Editable
Parent = TypeVar("Parent", bound="Editable")


@apidoc
class Exportable(Usable[Parent], Generic[Parent]):
    """An interface for any node object that can be exported
    eg. Class, class name,  top-level functions, imports
    """

    @property
    def is_exported(self) -> bool:
        """Indicates if the symbol is exported from its defining file.

        Returns:
            bool: True if the symbol has an export object, False otherwise.
        """
        return self.export is not None

    @property
    @reader(cache=False)
    def export(self) -> Export | None:
        """Returns the export object that exports this symbol.

        Retrieves the export object by examining incoming EXPORT edges in the CodebaseGraph.

        Args:
            None

        Returns:
            Export | None: The Export object that exports this symbol, or None if not exported.
        """
        try:
            if self.node_id is None:
                return None
            return self.G.predecessor(self.node_id, edge_type=EdgeType.EXPORT)
        except NoSuitableNeighbors:
            return None

    @property
    @reader(cache=False)
    def exported_name(self) -> str | None:
        """Retrieves the exported name of a symbol from its file.

        If the symbol is an export node, returns the node's name. If the symbol is not exported, returns None.

        Returns:
            str | None: The name the symbol is exported as, or None if not exported.
        """
        if self.node_type == NodeType.EXPORT:
            # Export's exported name is itself
            return self.name

        export = self.export
        if export is None:
            return None
        return export.name

    @property
    @reader
    def is_reexported(self) -> bool:
        """Determines if the symbol is re-exported from a different file.

        A re-export occurs when a symbol is imported into a file and then exported
        from that same file.

        Returns:
            bool: True if the symbol is re-exported from a different file than where
            it was defined, False otherwise.
        """
        return any(x.node_type == NodeType.EXPORT and x.file != self.file for x in self.symbol_usages + self.file.symbol_usages)

    @reader
    def get_import_string(self, alias: str | None = None, module: str | None = None, import_type: ImportType = ImportType.UNKNOWN, is_type_import: bool = False) -> str:
        """Returns the import string for a symbol.

        Generates the import statement needed to import a symbol from its module.

        Args:
            alias (str | None): Optional alias for the symbol.
            module (str | None): Optional module name to import from.
            import_type (ImportType): Type of import to generate.
            is_type_import (bool): Indicates if it's a type-only import.

        Returns:
            str: The formatted import string.

        Raises:
            NotImplementedError: If called on the base class.
        """
        raise NotImplementedError("The subclass must implement `to_import_string`.")
