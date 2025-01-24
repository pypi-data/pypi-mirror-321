import logging
import os
import re
import resource
import sys
from abc import abstractmethod
from collections.abc import Sequence
from functools import cached_property
from pathlib import Path
from typing import Generic, Literal, Self, TypeVar, override

from tree_sitter import Node as TSNode

from codegen.utils.codemod.codemod_writer_decorators import apidoc, noapidoc
from codegen.utils.codeowners.utils import get_filepath_owners
from graph_sitter._proxy import proxy_property
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.codebase.range_index import RangeIndex
from graph_sitter.codebase.span import Range
from graph_sitter.core.assignment import Assignment
from graph_sitter.core.autocommit import commiter, mover, reader, remover, writer
from graph_sitter.core.class_definition import Class
from graph_sitter.core.dataclasses.usage import UsageType
from graph_sitter.core.detached_symbols.code_block import CodeBlock
from graph_sitter.core.directory import Directory
from graph_sitter.core.function import Function
from graph_sitter.core.import_resolution import Import, WildcardImport
from graph_sitter.core.interface import Interface
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.interfaces.has_attribute import HasAttribute
from graph_sitter.core.interfaces.has_block import HasBlock
from graph_sitter.core.interfaces.importable import Importable
from graph_sitter.core.interfaces.usable import Usable
from graph_sitter.core.statements.import_statement import ImportStatement
from graph_sitter.core.symbol import Symbol
from graph_sitter.enums import EdgeType, ImportType, NodeType, SymbolType
from graph_sitter.extensions.sort import sort_editables
from graph_sitter.topological_sort import pseudo_topological_sort
from graph_sitter.tree_sitter_parser import get_parser_by_filepath_or_extension, parse_file
from graph_sitter.typescript.function import TSFunction
from graph_visualization.enums import VizNode

logger = logging.getLogger(__name__)


class BadWriteError(Exception):
    pass


@apidoc
class File(Editable[None]):
    """Represents a generic file.

    Could represent a source file or a non-code file such as a markdown file or image file.
    """

    name: str
    file_path: str
    node_type: Literal[NodeType.FILE] = NodeType.FILE
    _pending_content_bytes: bytes | None = None
    _directory: Directory | None
    _pending_imports: set[str]
    _binary: bool = False
    _range_index: RangeIndex

    def __init__(self, filepath: str, G: CodebaseGraph, ts_node: TSNode | None = None, binary: bool = False) -> None:
        if ts_node is None:
            # TODO: this is a temp hack to deal with all symbols needing a TSNode.
            parser = get_parser_by_filepath_or_extension(".py")
            ts_node = parser.parse(bytes("", "utf-8")).root_node
        self._range_index = RangeIndex()
        super().__init__(ts_node, getattr(self, "node_id", None), G, None)
        self.name = os.path.splitext(os.path.basename(filepath))[0]
        self.file_path = filepath
        self._directory = None
        self._binary = binary

    @property
    @reader
    @override
    def _source(self):
        """Text representation of the Editable instance."""
        if self._binary:
            return f"[Binary Blob of size {len(self.content_bytes)} Bytes]"
        else:
            return self.content

    @property
    def file(self) -> Self:
        """A property that returns the file object for non-source files.

        This is used by Editable.file to work with non-source files, allowing consistent interface usage across both source and non-source files.

        Returns:
            Self: The current file object.
        """
        # This is a hack to allow Editable.file to work for non-source files
        return self

    @classmethod
    @noapidoc
    def from_content(cls, filepath: str, content: str | bytes, G: CodebaseGraph, sync: bool = False, binary: bool = False) -> Self | None:
        """Creates a new file from content."""
        if sync:
            logger.warn("Creating & Syncing non-source files are not supported. Ignoring sync...")

        path = Path(filepath)
        if not path.exists():
            update_graph = True
            path.parent.mkdir(parents=True, exist_ok=True)
            if not binary:
                path.write_text(content)
            else:
                path.write_bytes(content)

        new_file = cls(filepath, G, ts_node=None, binary=binary)
        return new_file

    @property
    @noapidoc
    @reader
    def content_bytes(self) -> bytes:
        """Loaded dynamically every time to preserve source of truth.

        TODO: move rest of graph sitter to operate in bytes to prevent multi byte character issues?
        """
        # Check against None due to possibility of empty byte
        if self._pending_content_bytes is None:
            return Path(self.file_path).read_bytes()
        return self._pending_content_bytes

    @property
    @reader
    def content(self) -> str:
        """Returns the content of the file as a UTF-8 encoded string.

        Gets the content of the file, either from pending changes or by reading from disk. Binary files cannot be read as strings.

        Args:
            None

        Returns:
            str: The content of the file as a UTF-8 encoded string.

        Raises:
            ValueError: If the file is binary. Use content_bytes instead for binary files.
        """
        if self._binary:
            raise ValueError("Cannot read binary file as string. Use content_bytes instead.")

        return self.content_bytes.decode(encoding="utf-8")

    @noapidoc
    def write(self, content: str | bytes, to_disk: bool = False) -> None:
        """Writes string contents to the file."""
        self.write_bytes(content.encode("utf-8") if isinstance(content, str) else content, to_disk=to_disk)

    @noapidoc
    def write_bytes(self, content_bytes: bytes, to_disk: bool = False) -> None:
        self._pending_content_bytes = content_bytes
        self.G.pending_files.add(self)
        if to_disk:
            self.write_pending_content()
            if self.ts_node.start_byte == self.ts_node.end_byte:
                # TS didn't parse anything, register a write to make sure the transaction manager can restore the file later.
                self.edit("")

    @noapidoc
    def write_pending_content(self) -> None:
        if self._pending_content_bytes is not None:
            Path(self.file_path).write_bytes(self._pending_content_bytes)
            self._pending_content_bytes = None
            logger.debug("Finished write_pending_content")

    @noapidoc
    @writer
    def check_changes(self) -> None:
        if self._pending_content_bytes is not None:
            logger.error(BadWriteError("Directly called file write without calling commit_transactions"))

    @property
    @reader
    def directory(self) -> Directory | None:
        """Returns the directory that contains this file.

        The file can be housed within a directory in the codebase, and this property will return that directory instance.

        Returns:
            Directory | None: The directory containing this file, or None if the file is not in any directory.
        """
        return self._directory

    @noapidoc
    def _set_directory(self, directory: Directory | None) -> None:
        self._directory = directory

    @property
    def is_binary(self) -> bool:
        """Indicates whether the file contains binary data.

        A property that returns True if the file contains binary data, False if it contains text data.

        Returns:
            bool: True if the file contains binary data, False if it contains text data.
        """
        return self._binary

    @property
    @reader
    def extension(self) -> str:
        """Returns the file extension.

        Returns:
            str: The file extension including the dot (e.g., '.py', '.ts', '.js').
        """
        return os.path.splitext(self.file_path)[1]

    @property
    @reader
    def owners(self) -> set[str]:
        """Returns the CODEOWNERS of the file.

        Returns all Github CODEOWNERS associated with this file. If there is no CODEOWNERS file in the codebase, returns an empty set.

        Returns:
            set[str]: A set of Github usernames or team names that own this file. Empty if no CODEOWNERS file exists.
        """
        if self.G.codeowners_parser:
            return get_filepath_owners(codeowners=self.G.codeowners_parser, filepath=self.file_path)
        return set()

    @cached_property
    @noapidoc
    def github_url(self) -> str | None:
        if self.G.base_url:
            return self.G.base_url + "/" + self.file_path

    @property
    @reader
    def start_byte(self) -> int:
        """Returns the starting byte position of a file in its content.

        The start byte is always 0 for a file as it represents the beginning of the file's content.

        Returns:
            int: Always returns 0.
        """
        return 0

    @remover
    def remove(self) -> None:
        """Removes the file from the file system and graph.

        Queues the file to be removed during the next commit operation. The file will be removed from the filesystem and its node will be removed from the graph.

        Args:
            None

        Returns:
            None
        """
        self.transaction_manager.add_file_remove_transaction(self.file_path, self)
        self._pending_content_bytes = None

    @property
    def filepath(self) -> str:
        """Retrieves the file path of the file that this Editable instance belongs to.

        Returns:
            str: The file path of the file.
        """
        return self.file_path

    @mover
    def rename(self, new_name: str) -> None:
        """Renames the file to the specified name, preserving the file extension.

        Args:
            new_name (str): The new name for the file. If the new name includes the file extension, it will be used as-is.
                Otherwise, the original file extension will be preserved.

        Returns:
            None

        Note:
            This method will update all imports that reference this file to use the new filepath.
            The file will be physically moved on disk and all graph references will be updated.
        """
        # Split the filepath into directory, filename, and extension
        directory, filename = os.path.split(self.filepath)
        _, extension = os.path.splitext(filename)

        # Check if new name already contains the extension
        if new_name.endswith(extension):
            new_filename = new_name
        else:
            # Create the new filename with the original extension
            new_filename = new_name + extension

        # Join the directory with the new filename
        new_filepath = os.path.join(directory, new_filename)

        # Rename the file
        self.update_filepath(new_filepath)

    @mover
    def update_filepath(self, new_filepath: str) -> None:
        """Updates the file path and inbound imports of a file.

        Updates the file path of the file on disk and in the codebase graph. Additionally updates all
        inbound imports to reference the new file path.

        Args:
            new_filepath (str): The new file path to rename the file to.

        Raises:
            BadWriteError: If there are pending file writes that haven't been committed.
            ValueError: If the new file path already exists in the codebase graph.
        """
        # =====[ Change the file on disk ]=====
        self.transaction_manager.add_file_rename_transaction(self, self.file_path, new_filepath)

    def parse(self, G: "CodebaseGraph") -> None:
        """Parses the file representation into the graph.

        This method is called during file initialization to parse the file and build its graph representation within the codebase graph.

        Args:
            G (CodebaseGraph): The codebase graph that the file belongs to.

        Returns:
            None
        """
        pass

    @noapidoc
    @commiter
    def _compute_dependencies(self, *args, **kwargs) -> None:
        pass


TImport = TypeVar("TImport", bound="Import")
TFunction = TypeVar("TFunction", bound="Function")
TClass = TypeVar("TClass", bound="Class")
TGlobalVar = TypeVar("TGlobalVar", bound="Assignment")
TInterface = TypeVar("TInterface", bound="Interface")
TCodeBlock = TypeVar("TCodeBlock", bound="CodeBlock")


@apidoc
class SourceFile(
    File,
    HasBlock,
    Usable,
    HasAttribute[Symbol | TImport],
    Generic[TImport, TFunction, TClass, TGlobalVar, TInterface, TCodeBlock],
):
    """Represents a file with source code in the codebase.

    Enables creating, reading, updating, and deleting files and searching through their contents,
    etc.
    """

    code_block: TCodeBlock
    _nodes: list[Importable]

    def __init__(self, ts_node: TSNode, filepath: str, G: CodebaseGraph) -> None:
        self.node_id = G.add_node(self)
        self._nodes = []
        super().__init__(filepath, G, ts_node=ts_node)
        self._nodes.clear()
        self.G.filepath_idx[filepath] = self.node_id
        self._directory = None
        self._pending_imports = set()
        try:
            self.parse(G)
        except RecursionError as e:
            logger.error(f"RecursionError parsing file {filepath}: {e} at depth {sys.getrecursionlimit()} and {resource.getrlimit(resource.RLIMIT_STACK)}")
            raise e
        except Exception as e:
            logger.error(f"Failed to parse file {filepath}: {e}")
            raise e

    @property
    @reader
    @override
    def _source(self):
        """Text representation of the Editable instance."""
        return self.ts_node.text.decode("utf-8")

    @noapidoc
    @commiter
    def parse(self, G: CodebaseGraph) -> None:
        self.__dict__.pop("_source", None)
        # Add self to the graph
        self.code_block = self._parse_code_block(self.ts_node)

        self.code_block.parse()
        self._parse_imports()
        # We need to clear the valid symbol/import names before we start resolving exports since these can be outdated.
        self.invalidate()
        sort_editables(self._nodes)

    @abstractmethod
    @commiter
    def _parse_imports(self) -> None: ...

    @noapidoc
    @commiter
    def remove_internal_edges(self) -> None:
        """Removes all its direct nodes and edges for each of its internal symbols and imports."""
        # ==== [ Classes, Assignments, Function, Interfaces ] ====
        for symbol in self.symbols(nested=True):
            symbol._remove_internal_edges()

        # ==== [ Exports ] ====
        if hasattr(self, "exports"):
            for export in self.exports:
                export._remove_internal_edges()

        # ==== [ Imports ] ====
        for imp in self.imports:
            imp._remove_internal_edges()

    @noapidoc
    @commiter
    def unparse(self, reparse: bool = False) -> list[Importable]:
        """Removes all its direct nodes and edges for each of its internal symbols and imports.

        Returns a list of external import node ids that need to be re-resolved
        """
        external_edges_to_resolve = []

        # Collect node ids of all the file's nested children and itself to remove
        node_ids_to_remove = set()
        # ==== [ Classes, Assignments, Function, Interfaces ] ====
        for symbol in self.get_nodes():
            node_ids_to_remove.add(symbol.node_id)

        # ==== [ File ] ====
        node_ids_to_remove.add(self.node_id)
        self._remove_internal_edges()

        # Save any external import resolution edges to be re-resolved before removing the nodes
        for node_id in node_ids_to_remove:
            external_edges_to_resolve.extend(self.G.predecessors(node_id))

        # Finally, remove the nodes
        for node_id in node_ids_to_remove:
            if reparse and node_id == self.node_id:
                continue
            if self.G.has_node(node_id):
                self.G.remove_node(node_id)
        if not reparse:
            self.G.filepath_idx.pop(self.file_path, None)
        self._nodes.clear()
        return list(filter(lambda node: self.G.has_node(node.node_id) and node is not None, external_edges_to_resolve))

    @noapidoc
    @commiter
    def sync_with_file_content(self) -> None:
        """Re-parses parent file and re-sets current TSNode."""
        self._generation = self.G.generation
        self._pending_imports.clear()
        self.ts_node = parse_file(self.filepath, self.content)
        if self.node_id is None:
            self.G.filepath_idx[self.file_path] = self.node_id
            self.file_node_id = self.node_id
        else:
            assert self.G.has_node(self.node_id)
        self.name = os.path.splitext(os.path.basename(self.file_path))[0]
        self._range_index.clear()
        self.parse(self.G)

    @staticmethod
    @noapidoc
    def get_extensions() -> list[str]:
        """Returns a list of file extensions for the given programming language file."""

    @abstractmethod
    def symbol_can_be_added(self, symbol: Symbol) -> bool:
        """Checks if the file type supports adding the given symbol.

        Determines whether the given symbol can be added to this file based on the symbol's type and the file's
        language/type support.

        Args:
            symbol (Symbol): The symbol to check for add compatibility.

        Returns:
            bool: True if the symbol can be added to this file type, False otherwise.
        """

    @noapidoc
    @commiter
    def _compute_dependencies(self, *args, **kwargs) -> None:
        self.invalidate()
        self.code_block._compute_dependencies()

    @noapidoc
    def invalidate(self):
        self.__dict__.pop("valid_symbol_names", None)
        self.__dict__.pop("valid_import_names", None)
        for imp in self.imports:
            imp.__dict__.pop("_wildcards", None)

    @classmethod
    @noapidoc
    def from_content(cls, filepath: str, content: str, G: CodebaseGraph, sync: bool = True, verify_syntax: bool = True) -> Self | None:
        """Creates a new file from content and adds it to the graph."""
        ts_node = parse_file(filepath, content)
        if ts_node.has_error and verify_syntax:
            logger.info("Failed to parse file %s", filepath)
            return None

        update_graph = False
        path = Path(filepath)
        if not path.exists():
            update_graph = True
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)

        if update_graph and sync:
            G.add_single_file(filepath)
            return G.get_file(filepath)
        else:
            return cls(ts_node, filepath, G)

    @classmethod
    @noapidoc
    def create_from_filepath(cls, filepath: str, G: CodebaseGraph) -> Self | None:
        """Makes a new empty file and adds it to the graph.

        Graph-safe.
        """
        if filepath in G.filepath_idx:
            raise ValueError(f"File already exists in graph: {filepath}")

        ts_node = parse_file(filepath, "")
        if ts_node.has_error:
            logger.info("Failed to parse file %s", filepath)
            raise SyntaxError

        file = cls(ts_node, filepath, G)
        file.write("", to_disk=True)
        return file

    @property
    @reader(cache=False)
    def inbound_imports(self) -> list[TImport]:
        """Returns all imports that are importing symbols contained in this file.

        Retrieves a list of Import objects representing imports that reference symbols or content defined in this file.
        This includes imports of symbols declared in the file and imports of the file itself.

        Returns:
            list[TImport]: A list of Import objects that reference content from this file.
        """
        inbound_imports = set()
        for s in self.symbols:
            inbound_imports.update(i for i in s.symbol_usages(UsageType.DIRECT | UsageType.CHAINED) if isinstance(i, Import))
        for imp in self.imports:
            inbound_imports.update(i for i in imp.symbol_usages(UsageType.DIRECT | UsageType.CHAINED) if isinstance(i, Import))

        inbound_imports.update(i for i in self.symbol_usages(UsageType.DIRECT | UsageType.CHAINED) if isinstance(i, Import))
        return list(inbound_imports)

    @property
    @reader(cache=False)
    def import_statements(self) -> list[ImportStatement]:
        """Returns all ImportStatements in the file, where each import statement can contain
        multiple imports.

        Retrieves a list of all import statements in the file, sorted by their position. Each ImportStatement can contain
        multiple individual imports (e.g., 'from module import a, b, c').

        Returns:
            list[ImportStatement]: A sorted list of import statements contained in the file.
        """
        return sort_editables(x.import_statement for x in self.imports)

    @property
    @reader
    def importers(self) -> list[TImport]:
        """Returns all imports that directly imports this file as a module.

        This method returns a list of imports where this file is imported directly as a module,
        not individual symbols from this file.

        For example:
        - `from a import <this file>` will be included
        - `from <this file> import a` will NOT be included

        Args:
            None

        Returns:
            list[TImport]: List of Import objects that import this file as a module,
                sorted by file location.
        """
        imps = [x for x in self.G.in_edges(self.node_id) if x[2].type == EdgeType.IMPORT_SYMBOL_RESOLUTION]
        return sort_editables((self.G.get_node(x[0]) for x in imps), by_file=True, dedupe=False)

    @property
    @reader(cache=False)
    def imports(self) -> list[TImport]:
        """List of all Imports in this file.

        Retrieves all imports defined in this file. The imports are sorted by their position in the file.

        Returns:
            list[TImport]: A list of Import instances contained in this file, ordered by their position.
        """
        return list(filter(lambda node: isinstance(node, Import), self.get_nodes(sort_by_id=True)))

    @reader
    def has_import(self, symbol_alias: str) -> bool:
        """Returns True if the file has an import with the given alias.

        Checks if the file contains an import statement with a specific alias.

        Args:
            symbol_alias (str): The alias to check for in the import statements.

        Returns:
            bool: True if an import with the given alias exists, False otherwise.
        """
        aliases = [x.alias for x in self.imports if x.alias]
        return any(a.source == symbol_alias for a in aliases)

    @reader
    def get_import(self, symbol_alias: str) -> TImport | None:
        """Returns the import with matching alias. Returns None if not found.

        Args:
            symbol_alias (str): The alias name to search for. This can match either the direct import name or the aliased name.

        Returns:
            TImport | None: The import statement with the matching alias if found, None otherwise.
        """
        return next((x for x in self.imports if x.alias is not None and x.alias.source == symbol_alias), None)

    @proxy_property
    def symbols(self, nested: bool = False) -> list[Symbol | TClass | TFunction | TGlobalVar | TInterface]:
        """Returns all Symbols in the file, sorted by position in the file.

        Args:
            nested: Include nested symbols

        Returns:
            list[Symbol | TClass | TFunction | TGlobalVar | TInterface]: A list of all top-level symbols in the file, sorted by their position in the file. Symbols can be one of the following types:
                - Symbol: Base symbol class
                - TClass: Class definition
                - TFunction: Function definition
                - TGlobalVar: Global variable assignment
                - TInterface: Interface definition
        """
        return sort_editables([x for x in self.get_nodes(sort=False) if isinstance(x, Symbol) and (nested or x.is_top_level)], dedupe=False)

    @reader(cache=False)
    @noapidoc
    def get_nodes(self, *, sort_by_id: bool = False, sort: bool = True) -> Sequence[Importable]:
        """Returns all nodes in the file, sorted by position in the file."""
        ret = self._nodes
        if sort:
            return sort_editables(ret, by_id=sort_by_id, dedupe=False)
        return ret

    @reader
    def get_symbol(self, name: str) -> Symbol | None:
        """Gets a symbol by its name from the file.

        Attempts to resolve the symbol by name using name resolution rules first. If that fails,
        searches through the file's symbols list for a direct name match.

        Args:
            name (str): The name of the symbol to find.

        Returns:
            Symbol | None: The found symbol, or None if not found.
        """
        if symbol := self.resolve_name(name, self.end_byte):
            if isinstance(symbol, Symbol):
                return symbol
        return next((x for x in self.symbols if x.name == name), None)

    @property
    @reader(cache=False)
    def symbols_sorted_topologically(self) -> list[Symbol]:
        """Returns all Symbols in the file, sorted topologically (parents first). Robust to
        dependency loops.

        Performs a topological sort of the symbols in the file based on symbol dependencies. This ensures that parent symbols
        appear before their dependents while handling potential dependency loops gracefully.

        Args:
            None

        Returns:
            list[Symbol]: A list of symbols sorted topologically with parents appearing before their dependents.
        """
        ids = [x.node_id for x in self.symbols]
        # Create a subgraph based on G
        subgraph = self.G.build_subgraph(ids)
        symbol_names = pseudo_topological_sort(subgraph)
        return [subgraph.get_node_data(x) for x in symbol_names]

    @property
    @reader(cache=False)
    def global_vars(self) -> list[TGlobalVar]:
        """Returns all GlobalVars in the file.

        Retrieves all global variables (assignments) defined at the top level in the file, sorted by their position in the file.

        Returns:
            list[TGlobalVar]: A list of global variable assignments, where each element is an Assignment representing a global variable.
        """
        return [s for s in self.symbols if s.symbol_type == SymbolType.GlobalVar]

    @reader
    def get_global_var(self, name: str) -> TGlobalVar | None:
        """Returns a specific global var by name. Returns None if not found.

        Args:
            name (str): The name of the global variable to find.

        Returns:
            TGlobalVar | None: The global variable if found, None otherwise.
        """
        return next((x for x in self.global_vars if x.name == name), None)

    @property
    @reader(cache=False)
    def classes(self) -> list[TClass]:
        """Returns all Classes in the file.

        Returns a list of all Classes defined in the file, sorted by position in the file.
        Use this method to iterate over all classes in a file or to get information about class definitions.

        Returns:
            list[TClass]: A list of Class objects in the file, sorted by position in the file.
        """
        return [s for s in self.symbols if s.symbol_type == SymbolType.Class]

    @reader
    def get_class(self, name: str) -> TClass | None:
        """Returns a specific Class by full name. Returns None if not found.

        Searches for a class in the file with the specified name. Similar to get_symbol, but specifically for Class types.

        Args:
            name (str): The full name of the class to search for.

        Returns:
            TClass | None: The matching Class object if found, None otherwise.
        """
        if symbol := self.resolve_name(name, self.end_byte):
            if isinstance(symbol, Class):
                return symbol

    @property
    @reader(cache=False)
    def functions(self) -> list[TFunction]:
        """Returns all Functions in the file.

        Returns a list of all top-level functions defined in the file, sorted by their position in the file.
        Does not include nested functions (functions defined within other functions or classes).

        Returns:
            list[TFunction]: A list of Function objects representing all top-level functions in the file.
        """
        return [s for s in self.symbols if s.symbol_type == SymbolType.Function]

    @reader
    def get_function(self, name: str) -> TFunction | None:
        """Returns a specific Function by name.

        Gets a Function object from the file by searching for a function with the given name.

        Args:
            name (str): The name of the function to find.

        Returns:
            TFunction | None: The matching Function object if found, None otherwise.
        """
        return next((x for x in self.functions if x.name == name), None)

    @noapidoc
    @reader
    def get_node_by_name(self, name: str) -> Symbol | TImport | None:
        """Returns something defined in this file by name.

        Used during import resolution
        """
        symbol = self.get_symbol(name)
        if symbol is not None:
            return symbol
        imp = self.get_import(name)
        if imp is not None:
            return imp
        return None

    @cached_property
    @noapidoc
    @reader(cache=True)
    def valid_symbol_names(self) -> dict[str, Symbol | TImport | WildcardImport[TImport]]:
        """Returns a dict mapping name => Symbol (or import) in this file."""
        valid_symbol_names = {}
        for s in self.symbols:
            valid_symbol_names[s.full_name] = s
        for imp in self.imports:
            for name, dest in imp.names:
                valid_symbol_names[name] = dest
        return valid_symbol_names

    @noapidoc
    @reader
    def resolve_name(self, name: str, start_byte: int | None = None) -> Symbol | Import | WildcardImport | None:
        if resolved := self.valid_symbol_names.get(name):
            return resolved

    @property
    @reader
    def import_module_name(self) -> str:
        """Returns the module name that this file gets imported as.

        Gets the module name for this file in the context of imports. This name is used when other files import this file, either directly or when importing symbols from this file.

        Returns:
            str: The module name used when importing this file.
        """
        return self.get_import_module_name_for_file(self.filepath, self.G)

    @classmethod
    @abstractmethod
    @noapidoc
    def get_import_module_name_for_file(cls, filepath: str, G: CodebaseGraph) -> str: ...

    @abstractmethod
    def remove_unused_exports(self):
        """Removes unused exports from the file.

        Removes all exports that have no usages by any other files in the codebase. This helps reduce unnecessary exports and maintain a cleaner API surface.

        Returns:
            None
        """

    ####################################################################################################################
    # MANIPULATIONS
    ####################################################################################################################

    @mover
    def update_filepath(self, new_filepath: str) -> None:
        """Renames the file and updates all imports to point to the new location.

        When a file is renamed, this method does three things:
        1. Creates a new file node in the graph with the new filepath
        2. Moves the file on disk to the new location
        3. Updates all inbound imports to point to the new module location

        Args:
            new_filepath (str): The new filepath to move the file to.

        Returns:
            None
        """
        # =====[ Add the new filepath as a new file node in the graph ]=====
        new_file = self.G.node_classes.file_cls.from_content(new_filepath, self.content, self.G)
        # =====[ Change the file on disk ]=====
        super().update_filepath(new_filepath)
        # =====[ Update all the inbound imports to point to the new module ]=====
        new_module_name = new_file.import_module_name
        for imp in self.inbound_imports:
            imp.set_import_module(new_module_name)

    @writer
    def add_symbol_import(
        self,
        symbol: Symbol,
        alias: str | None = None,
        import_type: ImportType = ImportType.UNKNOWN,
        is_type_import: bool = False,
    ):
        """Adds an import to a file for a given symbol.

        This method adds an import statement to the file for a specified symbol. If an import for the
        symbol already exists, it returns the existing import instead of creating a new one.

        Args:
            symbol (Symbol): The symbol to import.
            alias (str | None): Optional alias for the imported symbol. Defaults to None.
            import_type (ImportType): The type of import to use. Defaults to ImportType.UNKNOWN.
            is_type_import (bool): Whether this is a type-only import. Defaults to False.

        Returns:
            Import: The created or existing import for the symbol.
        """
        imports = self.imports
        match = next((x for x in imports if x.imported_symbol == symbol), None)
        if match:
            return match

        import_string = symbol.get_import_string(alias, import_type=import_type, is_type_import=is_type_import)
        self.add_import_from_import_string(import_string)

    @writer(commit=False)
    def add_import_from_import_string(self, import_string: str) -> None:
        """Adds import to the file from a string representation of an import statement.

        This method adds a new import statement to the file based on its string representation.
        If the import already exists in the file, or is pending to be added, it won't be added again.
        If there are existing imports, the new import will be added before the first import,
        otherwise it will be added at the beginning of the file.

        Args:
            import_string (str): The string representation of the import statement to add.

        Returns:
            None
        """
        if any(import_string.strip() in imp.source for imp in self.imports):
            return
        if import_string.strip() in self._pending_imports:
            # Don't add the import string if it will already be added by another symbol
            return
        self._pending_imports.add(import_string.strip())
        self.transaction_manager.pending_undos.add(lambda: self._pending_imports.clear())
        if self.imports:
            self.imports[0].insert_before(import_string, priority=1)
        else:
            self.insert_before(import_string, priority=1)

    @writer
    def add_symbol_from_source(self, source: str) -> None:
        """Adds a symbol to a file from a string representation.

        This method adds a new symbol definition to the file by appending its source code string. The symbol will be added
        after existing symbols if present, otherwise at the beginning of the file.

        Args:
            source (str): String representation of the symbol to be added. This should be valid source code for
                the file's programming language.

        Returns:
            None: The symbol is added directly to the file's content.
        """
        symbols = self.symbols
        if len(symbols) > 0:
            symbols[-1].insert_after("\n" + source, fix_indentation=True)
        else:
            self.insert_after("\n" + source)

    @writer
    def add_symbol(self, symbol: Symbol, should_export: bool = True):
        """Adds `symbol` to the file.

        Adds the given symbol to the file, optionally exporting it if applicable. If the symbol already exists in the file, returns the existing symbol.

        Args:
            symbol (Symbol): The symbol to add to the file.
            should_export (bool, optional): Whether to export the symbol. Defaults to True.

        Returns:
            Symbol: The added symbol, or the existing symbol if it already exists in the file.

        Raises:
            ValueError: If the symbol type cannot be added to this file type.
        """
        # Check if the symbol already exists in file
        existing_symbol = self.get_symbol(symbol.name)
        if existing_symbol is not None:
            return existing_symbol
        if not self.symbol_can_be_added(symbol):
            raise ValueError(f"Symbol {symbol.name} cannot be added to this file type.")

        source = symbol.source
        if isinstance(symbol, TSFunction) and symbol.is_arrow:
            raw_source = symbol._named_arrow_function.text.decode("utf-8")
        else:
            raw_source = symbol.ts_node.text.decode("utf-8")
        if should_export and hasattr(symbol, "export") and (not symbol.is_exported or raw_source not in symbol.export.source):
            source = source.replace(raw_source, f"export {raw_source}")

        self.add_symbol_from_source(source)

    @noapidoc
    @writer
    def convert_js_to_esm(self) -> None:
        """Converts a JS file to an ES module."""
        # Convert `require` to `import`
        content = self.content
        lines = content.split("\n")
        converted_lines = []
        router_lines = []
        last_import_index = -1
        import_fixed = False

        for i, line in enumerate(lines):
            # Handle require statements with destructuring
            if "require(" in line and "{" in line:
                line = re.sub(
                    r"const {([\w\s,]+)} = require\('(.+?)'\);",
                    lambda m: f"import {{{m.group(1)}}} from '{m.group(2)}';",
                    line,
                )
                last_import_index = i
                import_fixed = True

            # Handle regular require statements
            elif "require(" in line:
                line = re.sub(r"const (\w+) = require\('(.+?)'\);", r"import \1 from '\2';", line)
                last_import_index = i
                import_fixed = True

            # Convert module.exports
            if "module.exports = " in line:
                line = re.sub(r"module.exports = (\w+);", r"export default \1;", line)

            # TODO: remove express.Router() specifics
            # Check for express.Router() assignment
            if "= express.Router();" in line and import_fixed:
                router_lines.append((i, line + "\n"))
            else:
                converted_lines.append(line)

        # Reinsert lines that contain "= express.Router();" after the last import
        if router_lines:
            # If no imports were found, router lines will be added at the beginning
            insert_position = last_import_index + 1 if last_import_index != -1 else 0
            for _, router_line in router_lines:
                converted_lines.insert(insert_position, router_line)
                insert_position += 1

        self.write("\n".join(converted_lines), to_disk=True)

    @property
    @noapidoc
    def viz(self) -> VizNode:
        return VizNode(file_path=self.filepath, start_point=self.start_point, end_point=self.end_point, name=self.name, symbol_name=self.__class__.__name__)

    ####################################################################################################################
    # AST-GREP
    ####################################################################################################################

    # @writer
    # def ast_grep_replace(self, pattern: str, replace: str) -> None:
    #     """Searches the file's AST for nodes that match the query"""
    #     root = SgRoot(self.content, "python").root()  # 1. parse
    #     node = root.find(pattern=pattern)  # 3. find
    #     edit = node.replace(replace)
    #     new_src = node.commit_edits([edit])
    #     self.edit(new_src)
    @property
    @noapidoc
    @reader(cache=True)
    def valid_import_names(self) -> dict[str, Symbol | TImport | WildcardImport[TImport]]:
        """Returns a dict mapping name => Symbol (or import) in this file that can be imported from
        another file.
        """
        return self.valid_symbol_names

    @noapidoc
    @reader
    @override
    def resolve_attribute(self, name: str) -> Symbol | TImport | None:
        return self.valid_import_names.get(name, None)

    @property
    @noapidoc
    def self_dest(self) -> HasBlock:
        """Returns the symbol usage resolution destination node for the symbol."""
        return self

    @property
    @noapidoc
    def parent_symbol(self) -> Self:
        return self

    @reader
    def find_by_byte_range(self, range: Range) -> list[Editable]:
        """Finds all editable objects that overlap with the given byte range in the file.

        Uses the file's range index to efficiently retrieve all editable objects (like functions,
        classes, variables) that intersect with the specified byte range.

        Args:
            range (Range): The byte range to search within the file.

        Returns:
            list[Editable]: A list of all Editable objects that overlap with the given range.
        """
        return self._range_index.get_all_for_range(range)

    @property
    @noapidoc
    def descendant_symbols(self) -> list[Importable]:
        return self.get_nodes()
