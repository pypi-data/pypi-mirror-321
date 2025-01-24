from __future__ import annotations

import os
from typing import TYPE_CHECKING

from tree_sitter import Node as TSNode

from codegen.utils.codemod.codemod_writer_decorators import noapidoc, py_apidoc
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.autocommit import reader
from graph_sitter.core.expressions import Name
from graph_sitter.core.import_resolution import Import, ImportResolution
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.interfaces.exportable import Exportable
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.statements.import_statement import ImportStatement
from graph_sitter.enums import ImportType, NodeType

if TYPE_CHECKING:
    from graph_sitter.python.file import PyFile

import logging

logger = logging.getLogger(__name__)


@py_apidoc
class PyImport(Import["PyFile"]):
    """Extends Import for Python codebases."""

    @reader
    def is_module_import(self) -> bool:
        """Determines if the import is a module-level or wildcard import.

        Checks whether the import is either a module import (e.g. 'import foo') or a wildcard import (e.g. 'from foo import *').

        Returns:
            bool: True if the import is a module-level or wildcard import, False otherwise.
        """
        return self.import_type in [ImportType.MODULE, ImportType.WILDCARD]

    @property
    @reader
    def namespace(self) -> str | None:
        """Returns the namespace of the import if it imports a file, or None otherwise.

        This property determines the namespace for file imports. It returns None for wildcard imports. For file
        imports (where resolved_symbol is a FILE), it returns the alias source. For all other cases, it returns None.

        Returns:
            str | None: The namespace string for file imports, None for wildcard imports or non-file imports.
        """
        if self.is_wildcard_import():
            return None

        resolved_symbol = self.resolved_symbol
        if resolved_symbol is not None and resolved_symbol.node_type == NodeType.FILE:
            return self.alias.source
        return None

    @property
    @reader
    def imported_exports(self) -> list[Exportable]:
        """Returns a list of exports from an import statement.

        Returns the enumerated list of symbols imported from a module import. If the import is
        not a module import, returns a list containing just the single imported symbol.
        For imports that don't resolve to any symbol, returns an empty list.

        Returns:
            list[Exportable]: A list of exported symbols. For module imports, contains all symbols
                and imports from the imported module. For non-module imports, contains a single imported
                symbol. For unresolved imports, returns empty list.
        """
        if self.imported_symbol is None:
            return []

        if not self.is_module_import():
            return [self.imported_symbol]

        return self.imported_symbol.symbols + self.imported_symbol.imports

    @noapidoc
    @reader
    def resolve_import(self, base_path: str | None = None) -> ImportResolution[PyFile] | None:
        base_path = base_path or self.G.projects[0].base_path or ""
        module_source = self.module.source if self.module else ""

        # If import is relative, convert to absolute path
        if module_source.startswith("."):
            module_source = self._relative_to_absolute_import(module_source)

        # =====[ Check if we are importing an entire file ]=====
        if self.is_module_import():
            # covers `import a.b.c` case and `from a.b.c import *` case
            filepath = os.path.join(base_path, module_source.replace(".", "/") + ".py")
        else:
            # This is the case where you do:
            # `from a.b.c import foo`
            filepath = os.path.join(
                base_path,
                module_source.replace(".", "/") + "/" + self.symbol_name.source + ".py",
            )
        if file := self.G.get_file(filepath):
            return ImportResolution(from_file=file, symbol=None, imports_file=True)

        filepath = filepath.replace(".py", "/__init__.py")
        if file := self.G.get_file(filepath):
            # TODO - I think this is another edge case, due to `dao/__init__.py` etc.
            # You can't do `from a.b.c import foo` => `foo.utils.x` right now since `foo` is just a file...
            return ImportResolution(from_file=file, symbol=None, imports_file=True)

        # =====[ Check if `module.py` file exists in the graph ]=====
        filepath = module_source.replace(".", "/") + ".py"
        filepath = os.path.join(base_path, filepath)
        if file := self.G.get_file(filepath):
            symbol = file.get_node_by_name(self.symbol_name.source)
            return ImportResolution(from_file=file, symbol=symbol)

        # =====[ Check if `module/__init__.py` file exists in the graph ]=====
        filepath = filepath.replace(".py", "/__init__.py")
        if from_file := self.G.get_file(filepath):
            symbol = from_file.get_node_by_name(self.symbol_name.source)
            return ImportResolution(from_file=from_file, symbol=symbol)

        # =====[ Case: Can't resolve the import ]=====
        if base_path == "":
            # Try to resolve with "src" as the base path
            return self.resolve_import(base_path="src")
        if base_path == "src":
            # Try "test" next
            return self.resolve_import(base_path="test")
        return None
        # # =====[ Check if we are importing an external module in the graph ]=====
        # if ext := self.G.get_external_module(self.source, self._unique_node.source):
        #     return ImportResolution(symbol=ext)
        # # Implies we are not importing the symbol from the current repo.
        # # In these cases, consider the import as an ExternalModule and add to graph
        # ext = ExternalModule.from_import(self)
        # return ImportResolution(symbol=ext)

    @noapidoc
    @reader
    def _relative_to_absolute_import(self, relative_import: str) -> str:
        """Helper to go from a relative import to an absolute one.
        Ex: ".foo.bar" in "src/file.py" would be -> "src.foo.bar"
        Ex: "..foo.bar" in "project/src/file.py" would be -> "project.foo.bar"
        """
        # Get the directory of the current file
        current_dir = os.path.dirname(self.to_file.file_path)

        # Count the number of dots at the start of the relative import
        dot_count = 0
        while relative_import.startswith("."):
            dot_count += 1
            relative_import = relative_import[1:]

        # Go up in the directory structure based on the number of dots
        for _ in range(dot_count - 1):
            current_dir = os.path.dirname(current_dir)

        # Convert the remaining path to a Python import path
        base_path = os.path.normpath(current_dir).replace(os.sep, ".")

        # Remove any leading '.' from the base_path
        while base_path.startswith("."):
            base_path = base_path[1:]

        # Combine the base path with the relative import
        if relative_import:
            return f"{base_path}.{relative_import}" if base_path else relative_import
        else:
            return base_path

    @classmethod
    @noapidoc
    def from_import_statement(cls, import_statement: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: ImportStatement) -> list[PyImport]:
        imports = []
        for module_node in import_statement.children_by_field_name("name"):
            if module_node.type == "dotted_name":
                imports.append(cls(import_statement, file_node_id, G, parent, module_node=module_node, name_node=module_node, alias_node=module_node, import_type=ImportType.MODULE))
            elif module_node.type == "aliased_import":
                module = module_node.child_by_field_name("name")
                symbol_name = module
                alias = module_node.child_by_field_name("alias")
                imports.append(cls(import_statement, file_node_id, G, parent, module_node=module, name_node=symbol_name, alias_node=alias, import_type=ImportType.MODULE))
            else:
                logger.error(f"Unsupported import statement: {import_statement.text.decode('utf-8')}")
        return imports

    @classmethod
    @noapidoc
    def from_import_from_statement(cls, import_statement: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: ImportStatement) -> list[PyImport]:
        module_node = import_statement.child_by_field_name("module_name")
        import_symbols = import_statement.children_by_field_name("name")
        if len(import_symbols) == 0:
            wildcard_import = next((node for node in import_statement.children if node.type == "wildcard_import"), None)
            if wildcard_import is None:
                raise ValueError(f"Unsupported import statement: {import_statement.text.decode('utf-8')}")
            return [cls(import_statement, file_node_id, G, parent, module_node=module_node, name_node=module_node, alias_node=module_node, import_type=ImportType.WILDCARD)]

        imports = []
        for import_symbol in import_symbols:
            if import_symbol.type == "dotted_name":
                imp = cls(import_statement, file_node_id, G, parent, module_node=module_node, name_node=import_symbol, alias_node=import_symbol, import_type=ImportType.NAMED_EXPORT)
            elif import_symbol.type == "aliased_import":
                symbol_name = import_symbol.child_by_field_name("name")
                alias = import_symbol.child_by_field_name("alias")
                imp = cls(import_statement, file_node_id, G, parent, module_node=module_node, name_node=symbol_name, alias_node=alias, import_type=ImportType.NAMED_EXPORT)
            else:
                raise ValueError(f"Unsupported import statement: {import_statement.text.decode('utf-8')}")
            imports.append(imp)
        return imports

    @classmethod
    @noapidoc
    def from_future_import_statement(cls, import_statement: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: ImportStatement) -> list[PyImport]:
        imports = []
        for module_node in import_statement.children_by_field_name("name"):
            imp = cls(import_statement, file_node_id, G, parent, module_node=module_node, name_node=module_node, alias_node=module_node, import_type=ImportType.SIDE_EFFECT)
            imports.append(imp)
        return imports

    @property
    @reader
    def import_specifier(self) -> Editable:
        """Retrieves the import specifier node for this import.

        Finds and returns the import specifier node that matches either the alias or symbol name of this import.

        Args:
            None

        Returns:
            Editable: The import specifier node as a Name object if found, None otherwise.
        """
        import_specifiers = self.ts_node.children_by_field_name("name")
        for import_specifier in import_specifiers:
            if import_specifier.type == "aliased_import":
                is_match = self.alias.source == import_specifier.child_by_field_name("alias").text.decode("utf-8")
            else:
                is_match = self.symbol_name.source == import_specifier.text.decode("utf-8")
            if is_match:
                return Name(import_specifier, self.file_node_id, self.G, self)

    @reader
    def get_import_string(
        self,
        alias: str | None = None,
        module: str | None = None,
        import_type: ImportType = ImportType.UNKNOWN,
        is_type_import: bool = False,
    ) -> str:
        """Generates an import string for a Python import statement.

        Creates a formatted import statement string based on the provided parameters. The generated string can represent different types of imports including wildcard imports and aliased imports.

        Args:
            alias (str | None): Optional alias name for the imported symbol.
            module (str | None): Optional module name to import from. If not provided, uses the file's import module name.
            import_type (ImportType): Type of import to generate. Defaults to UNKNOWN.
            is_type_import (bool): Whether this is a type import. Defaults to False.

        Returns:
            str: A formatted import statement string.
        """
        import_module = module if module is not None else self.file.import_module_name
        if import_type == ImportType.WILDCARD:
            file_as_module = self.file.name
            return f"from {import_module} import * as {file_as_module}"
        elif alias is not None and alias != self.name:
            return f"from {import_module} import {self.name} as {alias}"
        else:
            return f"from {import_module} import {self.name}"
