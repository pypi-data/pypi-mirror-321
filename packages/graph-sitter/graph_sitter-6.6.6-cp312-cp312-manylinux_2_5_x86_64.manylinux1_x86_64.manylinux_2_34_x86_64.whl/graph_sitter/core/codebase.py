"""Codebase - main interface for Codemods to interact with the codebase"""

import codecs
import json
import logging
import os
import re
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING, Generic, Literal, TypeVar, Unpack, overload

import plotly.graph_objects as go
import rich.repr
from git import Commit as GitCommit
from git import Diff
from git.remote import PushInfoList
from networkx import Graph
from rich.console import Console
from typing_extensions import deprecated

from codegen.git import LocalRepoOperator, RepoOperator
from codegen.git.schemas.config import BaseRepoConfig
from codegen.git.schemas.enums import CheckoutResult
from codegen.utils.ai import AbstractAIHelper, MultiProviderAIHelper
from codegen.utils.codemod.codemod_writer_decorators import apidoc, noapidoc
from codegen.utils.perf_utils import stopwatch
from graph_sitter._proxy import proxy_property
from graph_sitter.codebase.codebase_ai import generate_system_prompt, generate_tools
from graph_sitter.codebase.codebase_graph import GLOBAL_FILE_IGNORE_LIST, CodebaseGraph
from graph_sitter.codebase.config import CodebaseConfig, DefaultConfig, ProjectConfig, SessionOptions
from graph_sitter.codebase.control_flow import MaxAIRequestsError
from graph_sitter.codebase.diff_lite import DiffLite
from graph_sitter.codebase.flagging.code_flag import CodeFlag
from graph_sitter.codebase.flagging.enums import FlagKwargs
from graph_sitter.codebase.span import Span
from graph_sitter.core.assignment import Assignment
from graph_sitter.core.class_definition import Class
from graph_sitter.core.detached_symbols.code_block import CodeBlock
from graph_sitter.core.detached_symbols.parameter import Parameter
from graph_sitter.core.directory import Directory
from graph_sitter.core.external_module import ExternalModule
from graph_sitter.core.file import File, SourceFile
from graph_sitter.core.function import Function
from graph_sitter.core.import_resolution import Import
from graph_sitter.core.interface import Interface
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.interfaces.has_name import HasName
from graph_sitter.core.symbol import Symbol
from graph_sitter.core.type_alias import TypeAlias
from graph_sitter.enums import NodeType, SymbolType
from graph_sitter.extensions.sort import sort_editables
from graph_sitter.extensions.utils import uncache_all
from graph_sitter.output.constants import ANGULAR_STYLE
from graph_sitter.python.assignment import PyAssignment
from graph_sitter.python.class_definition import PyClass
from graph_sitter.python.detached_symbols.code_block import PyCodeBlock
from graph_sitter.python.detached_symbols.parameter import PyParameter
from graph_sitter.python.file import PyFile
from graph_sitter.python.function import PyFunction
from graph_sitter.python.import_resolution import PyImport
from graph_sitter.python.symbol import PySymbol
from graph_sitter.typescript.assignment import TSAssignment
from graph_sitter.typescript.class_definition import TSClass
from graph_sitter.typescript.detached_symbols.code_block import TSCodeBlock
from graph_sitter.typescript.detached_symbols.parameter import TSParameter
from graph_sitter.typescript.file import TSFile
from graph_sitter.typescript.function import TSFunction
from graph_sitter.typescript.import_resolution import TSImport
from graph_sitter.typescript.interface import TSInterface
from graph_sitter.typescript.symbol import TSSymbol
from graph_sitter.typescript.type_alias import TSTypeAlias
from graph_sitter.utils import determine_project_language
from graph_visualization.visualization_manager import VisualizationManager

if TYPE_CHECKING:
    from app.codemod.types import Group

logger = logging.getLogger(__name__)
MAX_LINES = 10000  # Maximum number of lines of text allowed to be logged


TSourceFile = TypeVar("TSourceFile", bound="SourceFile")
TDirectory = TypeVar("TDirectory", bound="Directory")
TSymbol = TypeVar("TSymbol", bound="Symbol")
TClass = TypeVar("TClass", bound="Class")
TFunction = TypeVar("TFunction", bound="Function")
TImport = TypeVar("TImport", bound="Import")
TGlobalVar = TypeVar("TGlobalVar", bound="Assignment")
TInterface = TypeVar("TInterface", bound="Interface")
TTypeAlias = TypeVar("TTypeAlias", bound="TypeAlias")
TParameter = TypeVar("TParameter", bound="Parameter")
TCodeBlock = TypeVar("TCodeBlock", bound="CodeBlock")


@apidoc
class Codebase(Generic[TSourceFile, TDirectory, TSymbol, TClass, TFunction, TImport, TGlobalVar, TInterface, TTypeAlias, TParameter, TCodeBlock]):
    """Main interface for codemods to interact with codebases, including utility methods etc.."""

    _op: RepoOperator
    viz: VisualizationManager
    repo_path: Path
    console: Console

    @overload
    def __init__(
        self,
        repo_path: None = None,
        *,
        projects: list[ProjectConfig],
        config: CodebaseConfig = DefaultConfig,
    ) -> None: ...

    @overload
    def __init__(
        self,
        repo_path: str,
        *,
        projects: None = None,
        config: CodebaseConfig = DefaultConfig,
    ) -> None: ...

    def __init__(
        self,
        repo_path: str | None = None,
        *,
        projects: list[ProjectConfig] | None = None,
        config: CodebaseConfig = DefaultConfig,
    ) -> None:
        # Sanity check inputs
        if repo_path is not None and projects is not None:
            raise ValueError("Cannot specify both repo_path and projects")

        if repo_path is None and projects is None:
            raise ValueError("Must specify either repo_path or projects")

        # Initialize project with repo_path if projects is None
        if repo_path is not None:
            repo_path = os.path.abspath(repo_path)
            repo_config = BaseRepoConfig()
            main_project = ProjectConfig(
                repo_operator=LocalRepoOperator(repo_config=repo_config, repo_path=repo_path, default_branch="main"),
                programming_language=determine_project_language(repo_path),
            )
            projects = [main_project]
        else:
            main_project = projects[0]

        # Initialize codebase
        self._op = main_project.repo_operator
        self.viz = VisualizationManager(op=self._op)
        self.repo_path = Path(self._op.repo_path)
        self.G = CodebaseGraph(projects, config=config)
        self.console = Console(record=True, soft_wrap=True)
        os.chdir(self._op.repo_path)

    @noapidoc
    def __str__(self) -> str:
        return f"<Codebase for repo={self.G.repo_name} with {len(self.G.nodes)} nodes and {len(self.G.edges)} edges>"

    def __rich_repr__(self) -> rich.repr.Result:
        yield "repo", self.G.repo_name
        yield "nodes", len(self.G.nodes)
        yield "edges", len(self.G.edges)

    __rich_repr__.angular = ANGULAR_STYLE

    @property
    @deprecated("Please do not use the local repo operator directly")
    @noapidoc
    def op(self) -> RepoOperator:
        return self._op

    ####################################################################################################################
    # NODES
    ####################################################################################################################

    @noapidoc
    def _symbols(self, symbol_type: SymbolType | None = None) -> list[TSymbol | TClass | TFunction | TGlobalVar]:
        matches: list[Symbol] = self.G.get_nodes(NodeType.SYMBOL)
        return [x for x in matches if x.is_top_level and (symbol_type is None or x.symbol_type == symbol_type)]

    # =====[ Node Types ]=====
    @overload
    def files(self, *, extensions: list[str]) -> list[File]: ...
    @overload
    def files(self, *, extensions: Literal["*"]) -> list[File]: ...
    @overload
    def files(self, *, extensions: None = ...) -> list[TSourceFile]: ...
    @proxy_property
    def files(self, *, extensions: list[str] | Literal["*"] | None = None) -> list[TSourceFile] | list[File]:
        """A list property that returns all files in the codebase.

        By default, this only returns source files. Setting `extensions='*'` will return all files in the codebase, and
        `extensions=[...]` will return all files with the specified extensions.

        `extensions='*'` is REQUIRED for listing all non source code files. Or else, codebase.files will ONLY return source files (e.g. .py, .ts).

        Returns all Files in the codebase, sorted alphabetically. For Python codebases, returns PyFiles (python files).
        For Typescript codebases, returns TSFiles (typescript files).

        Returns:
            list[TSourceFile]: A sorted list of source files in the codebase.
        """
        if extensions is None:
            # Return all source files
            files = self.G.get_nodes(NodeType.FILE)
        else:
            files = []
            # Get all files with the specified extensions
            for filepath, _ in self._op.iter_files(extensions=None if extensions == "*" else extensions, ignore_list=GLOBAL_FILE_IGNORE_LIST):
                files.append(self.get_file(filepath, optional=False))
        # Sort files alphabetically
        return sort_editables(files, alphabetical=True, dedupe=False)

    @property
    def directories(self) -> list[TDirectory]:
        """List all directories in the codebase.

        Returns a list of all Directory objects present in the codebase. Each Directory object represents a directory in the codebase.
        This property is used to access and navigate the directory structure of the codebase.

        Returns:
            list[TDirectory]: A list of Directory objects in the codebase.
        """
        return list(self.G.directories.values())

    @property
    def imports(self) -> list[TImport]:
        """Returns a list of all Import nodes in the codebase.

        Retrieves all Import nodes from the codebase graph. These imports represent all import statements across all files in the codebase,
        including imports from both internal modules and external packages.

        Args:
            None

        Returns:
            list[TImport]: A list of Import nodes representing all imports in the codebase.
            TImport can be PyImport for Python codebases or TSImport for TypeScript codebases.
        """
        return self.G.get_nodes(NodeType.IMPORT)

    @property
    def external_modules(self) -> list[ExternalModule]:
        """Returns a list of all external modules in the codebase.

        An external module represents a dependency that is imported but not defined within the codebase itself (e.g. third-party packages like 'requests' or 'numpy').

        Returns:
            list[ExternalModule]: List of external module nodes from the codebase graph.
        """
        return self.G.get_nodes(NodeType.EXTERNAL)

    @property
    def symbols(self) -> list[TSymbol]:
        """List of all top-level Symbols (Classes, Functions, etc.) in the codebase. Excludes Class
        methods.

        Returns:
            list[TSymbol]: A list of Symbol objects of all top-level symbols in the codebase. Includes classes, functions, and global variables defined at the module level, excludes methods.
        """
        return self._symbols()

    @property
    def classes(self) -> list[TClass]:
        """List of all Classes in the codebase.

        Returns a sorted list of all Class nodes in the codebase. Class nodes represent class definitions in source files.
        Only includes top-level classes, not inner/nested classes.

        Returns:
            list[TClass]: A sorted list of all Class nodes in the codebase.
        """
        return sort_editables(self._symbols(symbol_type=SymbolType.Class), dedupe=False)

    @property
    def functions(self) -> list[TFunction]:
        """List of all Functions in the codebase.

        Returns a sorted list of all top-level Function objects in the codebase, excluding class methods.

        Returns:
            list[TFunction]: A list of Function objects representing all functions in the codebase, sorted alphabetically.
        """
        return sort_editables(self._symbols(symbol_type=SymbolType.Function), dedupe=False)

    @property
    def global_vars(self) -> list[TGlobalVar]:
        """List of all GlobalVars in the codebase.

        A GlobalVar represents a global variable assignment in the source code. These are variables defined at the module level.

        Returns:
            list[TGlobalVar]: A list of all global variable assignments in the codebase.
        """
        return self._symbols(symbol_type=SymbolType.GlobalVar)

    @property
    def interfaces(self) -> list[TInterface]:
        """Retrieves all interfaces in the codebase.

        Returns a list of all Interface symbols defined at the top-level of source files in the codebase.
        This property is only applicable for TypeScript codebases and will return an empty list for Python codebases.

        Returns:
            list[TInterface]: A list of Interface objects defined in the codebase's source files.
        """
        return self._symbols(symbol_type=SymbolType.Interface)

    @property
    def types(self) -> list[TTypeAlias]:
        """List of all Types in the codebase (Typescript only).

        Returns a list of all type aliases defined at the top level in the codebase. This method is only applicable
        for TypeScript codebases.

        Returns:
            list[TTypeAlias]: A list of all type aliases defined in the codebase.
        """
        return self._symbols(symbol_type=SymbolType.Type)

    ####################################################################################################################
    # EDGES
    ####################################################################################################################
    # TODO - no utilities needed here at the moment, but revisit

    ####################################################################################################################
    # EXTERNAL API
    ####################################################################################################################

    def create_file(self, filepath: str, content: str = "", sync: bool = True) -> File:
        """Creates a new file in the codebase with specified content.

        Args:
            filepath (str): The path where the file should be created.
            content (str): The content of the file to be created. Defaults to empty string.
            sync (bool): Whether to sync the graph after creating the file. Defaults to True.

        Returns:
            File: The newly created file object.

        Raises:
            ValueError: If the provided content cannot be parsed according to the file extension.
        """
        # Check if file already exists
        # TODO: These checks break parse tests ???
        # Look into this!
        # if self.has_file(filepath):
        #     raise ValueError(f"File {filepath} already exists in codebase.")
        # if os.path.exists(filepath):
        #     raise ValueError(f"File {filepath} already exists on disk.")

        file_exts = self.G.extensions
        # Create file as source file if it has a registered extension
        if any(filepath.endswith(ext) for ext in file_exts):
            file_cls = self.G.node_classes.file_cls
            file = file_cls.from_content(filepath, content, self.G, sync=sync)
            if file is None:
                raise ValueError(f"Failed to parse file with content {content}. Please make sure the content syntax is valid with respect to the filepath extension.")
        else:
            # Create file as non-source file
            file = File.from_content(filepath, content, self.G, sync=False)

        # This is to make sure we keep track of this file for diff purposes
        uncache_all()
        return file

    def create_directory(self, dir_path: str, exist_ok: bool = False, parents: bool = False) -> None:
        """Creates a directory at the specified path.

        Args:
            dir_path (str): The path where the directory should be created.
            exist_ok (bool): If True, don't raise an error if the directory already exists. Defaults to False.
            parents (bool): If True, create any necessary parent directories. Defaults to False.

        Raises:
            FileExistsError: If the directory already exists and exist_ok is False.
        """
        if parents:
            os.makedirs(dir_path, exist_ok=exist_ok)
        else:
            if not exist_ok or not os.path.isdir(dir_path):
                os.mkdir(dir_path)

    def has_file(self, filepath: str, ignore_case: bool = False) -> bool:
        """Determines if a file exists in the codebase.

        Args:
            filepath (str): The filepath to check for existence.
            ignore_case (bool): If True, ignore case when checking for file existence. Defaults to False.

        Returns:
            bool: True if the file exists in the codebase, False otherwise.
        """
        return self.get_file(filepath, optional=True, ignore_case=ignore_case) is not None

    @overload
    def get_file(self, filepath: str, *, optional: Literal[False] = ..., ignore_case: bool = ...) -> TSourceFile: ...
    @overload
    def get_file(self, filepath: str, *, optional: Literal[True], ignore_case: bool = ...) -> TSourceFile | None: ...
    def get_file(self, filepath: str, *, optional: bool = False, ignore_case: bool = False) -> TSourceFile | None:
        """Retrieves a file from the codebase by its filepath.

        This method first attempts to find the file in the graph, then checks the filesystem if not found. Files can be either source files (e.g. .py, .ts) or binary files.

        Args:
            filepath (str): The path to the file, relative to the codebase root.
            optional (bool): If True, return None if file not found. If False, raise ValueError.
            ignore_case (bool): If True, ignore case when checking for file existence. Defaults to False.

        Returns:
            TSourceFile | None: The source file if found, None if optional=True and file not found.

        Raises:
            ValueError: If file not found and optional=False.
        """

        def get_file_from_path(path: str) -> File | None:
            try:
                return File.from_content(path, open(path).read(), self.G, sync=False)
            except UnicodeDecodeError:
                # Handle when file is a binary file
                return File.from_content(path, open(path, "rb").read(), self.G, sync=False, binary=True)

        # Try to get the file from the graph first
        file = self.G.get_file(filepath, ignore_case=ignore_case)
        if file is not None:
            return file
        elif os.path.exists(filepath):
            return get_file_from_path(filepath)
        elif ignore_case:
            parent = os.path.dirname(filepath)
            if parent == "":
                for file in os.listdir("."):
                    if filepath.lower() == file.lower():
                        return get_file_from_path(file)
            else:
                for file in os.listdir(parent):
                    path = os.path.join(parent, file)
                    if filepath.lower() == path.lower():
                        return get_file_from_path(path)
        elif not optional:
            raise ValueError(f"File {filepath} not found in codebase. Use optional=True to return None instead.")
        return None

    def has_directory(self, dir_path: str, ignore_case: bool = False) -> bool:
        """Returns a boolean indicating if a directory exists in the codebase.

        Checks if a directory exists at the specified path within the codebase.

        Args:
            dir_path (str): The path to the directory to check for, relative to the codebase root.

        Returns:
            bool: True if the directory exists in the codebase, False otherwise.
        """
        return self.get_directory(dir_path, optional=True, ignore_case=ignore_case) is not None

    def get_directory(self, dir_path: str, optional: bool = False, ignore_case: bool = False) -> TDirectory | None:
        """Returns Directory by `dir_path`, or full path to the directory from codebase root.

        Args:
            dir_path (str): The path to the directory to retrieve.
            optional (bool): If True, return None when directory is not found. If False, raise ValueError.

        Returns:
            TDirectory | None: The Directory object if found, None if optional=True and directory not found.

        Raises:
            ValueError: If directory not found and optional=False.
        """
        # Sanitize the path
        dir_path = os.path.normpath(dir_path)
        dir_path = "" if dir_path == "." else dir_path
        directory = self.G.get_directory(dir_path, ignore_case=ignore_case)
        if directory is None and not optional:
            raise ValueError(f"Directory {dir_path} not found in codebase. Use optional=True to return None instead.")
        return directory

    def has_symbol(self, symbol_name: str) -> bool:
        """Returns whether a symbol exists in the codebase.

        This method checks if a symbol with the given name exists in the codebase.

        Args:
            symbol_name (str): The name of the symbol to look for.

        Returns:
            bool: True if a symbol with the given name exists in the codebase, False otherwise.
        """
        return any([x.name == symbol_name for x in self.symbols])

    def get_symbol(self, symbol_name: str, optional: bool = False) -> TSymbol | None:
        """Returns a Symbol by name from the codebase.

        Returns the first Symbol that matches the given name. If multiple symbols are found with the same name, raises a ValueError.
        If no symbol is found, returns None if optional is True, otherwise raises a ValueError.

        Args:
            symbol_name (str): The name of the symbol to find.
            optional (bool): If True, returns None when symbol is not found. If False, raises ValueError. Defaults to False.

        Returns:
            TSymbol | None: The matched Symbol if found, None if not found and optional=True.

        Raises:
            ValueError: If multiple symbols are found with the same name, or if no symbol is found and optional=False.
        """
        symbols = self.get_symbols(symbol_name)
        if len(symbols) == 0:
            if not optional:
                raise ValueError(f"Symbol {symbol_name} not found in codebase. Use optional=True to return None instead.")
            return None
        if len(symbols) > 1:
            raise ValueError(f"Symbol {symbol_name} is ambiguous in codebase - more than one instance")
        return symbols[0]

    def get_symbols(self, symbol_name: str) -> list[TSymbol]:
        """Retrieves all symbols in the codebase that match the given symbol name.

        This method is used when there may be multiple symbols with the same name, in which case get_symbol() would raise a ValueError.

        Args:
            symbol_name (str): The name of the symbols to retrieve.

        Returns:
            list[TSymbol]: A list of Symbol objects that match the given name, sorted alphabetically.

        Note:
            When a unique symbol is required, use get_symbol() instead. It will raise ValueError if multiple symbols are found.
        """
        return sort_editables(x for x in self.symbols if x.name == symbol_name)

    def get_class(self, class_name: str, optional: bool = False) -> TClass | None:
        """Returns a class that matches the given name.

        Args:
            class_name (str): The name of the class to find.
            optional (bool): If True, return None when class is not found instead of raising ValueError. Defaults to False.

        Returns:
            TClass | None: The class with the given name, or None if optional=True and class not found.

        Raises:
            ValueError: If the class is not found and optional=False, or if multiple classes with the same name exist.
        """
        matches = [c for c in self.classes if c.name == class_name]
        if len(matches) == 0:
            if not optional:
                raise ValueError(f"Class {class_name} not found in codebase. Use optional=True to return None instead.")
            return None
        if len(matches) > 1:
            raise ValueError(f"Class {class_name} is ambiguous in codebase - more than one instance")
        return matches[0]

    def get_function(self, function_name: str, optional: bool = False) -> TFunction | None:
        """Retrieves a function from the codebase by its name.

        This method searches through all functions in the codebase to find one matching the given name.
        If multiple functions with the same name exist, a ValueError is raised.

        Args:
            function_name (str): The name of the function to retrieve.
            optional (bool): If True, returns None when function is not found instead of raising ValueError.
                            Defaults to False.

        Returns:
            TFunction | None: The matching function if found. If optional=True and no match is found,
                             returns None.

        Raises:
            ValueError: If function is not found and optional=False, or if multiple matching functions exist.
        """
        matches = [f for f in self.functions if f.name == function_name]
        if len(matches) == 0:
            if not optional:
                raise ValueError(f"Function {function_name} not found in codebase. Use optional=True to return None instead.")
            return None
        if len(matches) > 1:
            raise ValueError(f"Function {function_name} is ambiguous in codebase - more than one instance")
        return matches[0]

    @noapidoc
    @staticmethod
    def _remove_extension(filename: str) -> str:
        """Removes the trailing extension from the filename if it appears at the end,
        e.g. filename.ext -> filename
        """
        return re.sub(r"\.[^.]+$", "", filename)

    def get_relative_path(self, from_file: str, to_file: str) -> str:
        """Calculates a relative path from one file to another, removing the extension from the target file.

        This method splits both `from_file` and `to_file` by forward slashes, finds their common path prefix,
        and determines how many directories to traverse upward from `from_file` before moving into the
        remaining directories of `to_file` (with its extension removed).

        Args:
            from_file (str): The file path from which the relative path will be computed.
            to_file (str): The file path (whose extension will be removed) to which the relative path will be computed.

        Returns:
            str: The relative path from `from_file` to `to_file` (with the extension removed from `to_file`).
        """
        # Remove extension from the target file
        to_file = self._remove_extension(to_file)

        from_parts = from_file.split("/")
        to_parts = to_file.split("/")

        # Find common prefix
        i = 0
        while i < len(from_parts) - 1 and i < len(to_parts) and from_parts[i] == to_parts[i]:
            i += 1

        # Number of '../' we need
        up_levels = len(from_parts) - i - 1

        # Construct relative path
        relative_path = ("../" * up_levels) + "/".join(to_parts[i:])

        return relative_path

    ####################################################################################################################
    # State/Git
    ####################################################################################################################
    def git_commit(self, message: str, *, verify: bool = False) -> GitCommit | None:
        """Commits all staged changes to the codebase and git.

        Args:
            message (str): The commit message
            verify (bool): Whether to verify the commit before committing. Defaults to False.

        Returns:
            GitCommit | None: The commit object if changes were committed, None otherwise.
        """
        os.chdir(self._op.repo_path)
        self.G.commit_transactions(sync_graph=False)
        if self._op.stage_and_commit_all_changes(message, verify):
            logger.info(f"Commited repository to {self._op.head_commit} on {self._op.get_active_branch_or_commit()}")
            return self._op.head_commit
        return None

    @noapidoc
    def commit(self, sync_graph: bool = True) -> None:
        """Commits all staged changes to the codebase and synchronizes the graph if specified.

        This method must be called when multiple overlapping edits are made on a single entity to ensure proper tracking of changes.
        For example, when renaming a symbol and then moving it to a different file, commit must be called between these operations.

        Args:
            sync_graph (bool): Whether to synchronize the graph after committing changes. Defaults to True.

        Returns:
            None
        """
        if not self.G.config.feature_flags.debug:
            self.log("Warning: using a method that may break codemod execution. This is unnessecary in most cases. You should use this only if you are certian it's nessecary")
        os.chdir(self._op.repo_path)
        self.G.commit_transactions(sync_graph=sync_graph and self.G.config.feature_flags.sync_enabled)

    @noapidoc
    def git_push(self, *args, **kwargs) -> PushInfoList:
        """Git push."""
        return self._op.push_changes(*args, **kwargs)

    @property
    def default_branch(self) -> str:
        """The default branch of this repository.

        Returns the name of the default branch (e.g. 'main' or 'master') for the current repository.

        Returns:
            str: The name of the default branch.
        """
        return self._op.default_branch

    @property
    def current_commit(self) -> GitCommit | None:
        """Returns the current Git commit that is checked out in the repository.

        Args:
            None

        Returns:
            GitCommit | None: The currently checked out Git commit object, or None if no commit is checked out.
        """
        return self._op.git_cli.head.commit

    @stopwatch
    @noapidoc
    def reset(self) -> None:
        """Resets the codebase by:
        - Discarding any staged/unstaged changes
        - Resetting stop codemod limits: (max seconds, max transactions, max AI requests)
        - Clearing logs
        - Clearing pending transactions + pending files
        - Syncing graph to synced_commit
        """
        logger.info("Resetting codebase ...")
        os.chdir(self._op.repo_path)
        self._op.discard_changes()  # Discard any changes made to the raw file state
        self._num_ai_requests = 0
        self.reset_logs()
        self.G.undo_applied_diffs()

    def checkout(self, *, commit: str | GitCommit | None = None, branch: str | None = None, create_if_missing: bool = False, remote: bool = False) -> CheckoutResult:
        """Checks out a git branch or commit and syncs the codebase graph to the new state.

        This method discards any pending changes, performs a git checkout of the specified branch or commit,
        and then syncs the codebase graph to reflect the new state.

        Args:
            commit (str | GitCommit | None): Hash or GitCommit object to checkout. Cannot be used with branch.
            branch (str | None): Name of branch to checkout. Cannot be used with commit.
            create_if_missing (bool): If True, creates the branch if it doesn't exist. Defaults to False.
            remote (bool): If True, attempts to pull from remote when checking out branch. Defaults to False.

        Returns:
            CheckoutResult: The result of the checkout operation.

        Raises:
            AssertionError: If neither commit nor branch is specified, or if both are specified.
        """
        self.reset()
        if commit is None:
            assert branch is not None, "Commit or branch must be specified"
            logger.info(f"Checking out branch {branch}")
            result = self._op.checkout_branch(branch, create_if_missing=create_if_missing, remote=remote)
        else:
            assert branch is None, "Cannot specify branch and commit"
            logger.info(f"Checking out commit {commit}")
            result = self._op.checkout_commit(commit_hash=commit)
        if result == CheckoutResult.SUCCESS:
            logger.info(f"Checked out {branch or commit}")
            self.sync_to_commit(self._op.head_commit)
        elif result == CheckoutResult.NOT_FOUND:
            logger.info(f"Could not find branch {branch or commit}")

        return result

    @noapidoc
    def sync_to_commit(self, target_commit: GitCommit) -> None:
        """Updates the current base to a new commit."""
        origin_commit = self.G.synced_commit
        if origin_commit.hexsha == target_commit.hexsha:
            logger.info(f"Codebase is already synced to {target_commit.hexsha}. Skipping sync_to_commit.")
            return
        if not self.G.config.feature_flags.sync_enabled:
            logger.info(f"Syncing codebase is disabled for repo {self._op.repo_name}. Skipping sync_to_commit.")
            return

        logger.info(f"Syncing {self._op.repo_name} to {target_commit.hexsha}")
        diff_index = origin_commit.diff(target_commit)
        diff_lites = []
        for diff in diff_index:
            diff_lites.append(DiffLite.from_git_diff(diff))
        self.G.apply_diffs(diff_lites)
        self.G.save_commit(target_commit)

    @noapidoc
    def get_diffs(self, base: str | None = None) -> list[Diff]:
        """Get all changed files."""
        if base is None:
            return self._op.get_diffs(self._op.head_commit)
        return self._op.get_diffs(base)

    @noapidoc
    def get_diff(self, base: str | None = None) -> str:
        """Produce a single git diff for all files."""
        self._op.git_cli.git.add(A=True)  # add all changes to the index so untracked files are included in the diff
        if base is None:
            return self._op.git_cli.git.diff(patch=True, full_index=True, staged=True)
        return self._op.git_cli.git.diff(base, full_index=True)

    @noapidoc
    def clean_repo(self):
        """Cleaning a codebase repo by:
        1. Deleting all branches except the checked out one
        2. Deleting all remotes except origin

        NOTE: doesn't discard changes b/c this should be handled by self.reset
        NOTE: doesn't checkout onto the default branch b/c this should be handled by self.checkout
        """
        logger.info(f"Cleaning codebase repo at {self.repo_path} ...")
        self._op.clean_remotes()
        self._op.clean_branches()

    @noapidoc
    def stash_changes(self):
        """Stash all changes in the codebase."""
        self._op.stash_push()

    @noapidoc
    def restore_stashed_changes(self):
        """Restore the most recent stash in the codebase."""
        self._op.stash_pop()

    ####################################################################################################################
    # GRAPH VISUALIZATION
    ####################################################################################################################

    def visualize(self, G: Graph | go.Figure, root: Editable | str | int | None = None) -> None:
        """Visualizes a NetworkX graph or Plotly figure.

        Creates a visualization of the provided graph using GraphViz. This is useful for visualizing dependency graphs, call graphs,
        directory structures, or other graph-based representations of code relationships.

        Args:
            G (Graph | go.Figure): A NetworkX graph or Plotly figure to visualize
            root (Editable | str | int | None): The root node to visualize around. When specified, the visualization will be centered on this node. Defaults to None.

        Returns:
            None
        """
        self.viz.write_graphviz_data(G=G, root=root)

    ####################################################################################################################
    # FLAGGING
    ####################################################################################################################

    @noapidoc
    def flags(self) -> list[CodeFlag]:
        """Returns all collected code flags in find mode.

        Returns:
            list[CodeFlag]: A list of all flags in the codebase.
        """
        return self.G.flags._flags

    @noapidoc
    def flag_instance(
        self,
        symbol: TSymbol | None = None,
        **kwargs: Unpack[FlagKwargs],
    ) -> CodeFlag:
        """Flags a symbol, file or import to enable enhanced tracking of changes and splitting into
        smaller PRs.

        This method should be called once per flaggable entity and should be called before any edits are made to the entity.
        Flags enable tracking of changes and can be used for various purposes like generating pull requests or applying changes selectively.

        Args:
            symbol (TSymbol | None): The symbol to flag. Can be None if just flagging a message.
            **kwargs: Arguments used to construct the flag
        Returns:
            CodeFlag: A flag object representing the flagged entity.
        """
        return self.G.flags.flag_instance(symbol, **kwargs)

    def should_fix(self, flag: CodeFlag) -> bool:
        """Returns True if the flag should be fixed based on the current mode and active group.

        Used to filter out flags that are not in the active group and determine if the flag should be processed or ignored.

        Args:
            flag (CodeFlag): The code flag to check.

        Returns:
            bool: True if the flag should be fixed, False if it should be ignored.
            Returns False in find mode.
            Returns True if no active group is set.
            Returns True if the flag's hash exists in the active group hashes.
        """
        return self.G.flags.should_fix(flag)

    @noapidoc
    def set_find_mode(self, find_mode: bool) -> None:
        self.G.flags.set_find_mode(find_mode)

    @noapidoc
    def set_active_group(self, group: "Group") -> None:
        """Will only fix these flags."""
        # TODO - flesh this out more with Group datatype and GroupBy
        self.G.flags.set_active_group(group)

    ####################################################################################################################
    # LOGGING
    ####################################################################################################################

    _logs = []

    def __is_markup_loggable__(self, arg) -> bool:
        return isinstance(arg, Editable)

    @noapidoc
    def log(self, *args) -> None:
        """Logs a message as a string.

        At the end, we will save a tail of these logs on the CodemodRun
        """
        self.G.transaction_manager.check_max_preview_time()
        if self.console.export_text(clear=False).count("\n") >= MAX_LINES:
            return  # if max lines has been reached, skip logging
        for arg in args:
            if self.__is_markup_loggable__(arg):
                fullName = arg.get_name() if isinstance(arg, HasName) and arg.get_name() else ""
                doc_lang = arg._api_doc_lang if hasattr(arg, "_api_doc_lang") else None
                class_name = arg.__class__.__name__
                link = f"::docs/codebase-sdk/{doc_lang}/{class_name}" if doc_lang is not None else ""
                self.console.print(f"{class_name}::{fullName}{link}", markup=True, soft_wrap=True)
        args = [arg for arg in args if not self.__is_markup_loggable__(arg)]
        if args:
            self.console.print(*args, markup=True, soft_wrap=True)

    @noapidoc
    def reset_logs(self) -> None:
        """Resets the logs."""
        self.console.clear()

    @noapidoc
    def get_finalized_logs(self) -> str:
        """Returns the logs as a string, truncating if necessary."""
        return self.console.export_text()

    ####################################################################################################################
    # INTERNAL UTILS
    ####################################################################################################################

    @contextmanager
    @noapidoc
    def session(self, sync_graph: bool = True, commit: bool = True, session_options: SessionOptions = SessionOptions()) -> Generator[None, None, None]:
        with self.G.session(sync_graph=sync_graph, commit=commit, session_options=session_options):
            yield None

    @noapidoc
    def _enable_experimental_language_engine(self, async_start: bool = False, install_deps: bool = False, use_v8: bool = False) -> None:
        """Debug option to enable experimental language engine for the current codebase."""
        if install_deps and not self.G.language_engine:
            from graph_sitter.core.external.dependency_manager import get_dependency_manager

            logger.info("Cold installing dependencies...")
            logger.info("This may take a while for large repos...")
            self.G.dependency_manager = get_dependency_manager(self.G.projects[0].programming_language, self.G, enabled=True)
            self.G.dependency_manager.start(async_start=False)
            # Wait for the dependency manager to be ready
            self.G.dependency_manager.wait_until_ready(ignore_error=False)
            logger.info("Dependencies ready")
        if not self.G.language_engine:
            from graph_sitter.core.external.language_engine import get_language_engine

            logger.info("Cold starting language engine...")
            logger.info("This may take a while for large repos...")
            self.G.language_engine = get_language_engine(self.G.projects[0].programming_language, self.G, use_ts=True, use_v8=use_v8)
            self.G.language_engine.start(async_start=async_start)
            # Wait for the language engine to be ready
            self.G.language_engine.wait_until_ready(ignore_error=False)
            logger.info("Language engine ready")

    ####################################################################################################################
    # AI
    ####################################################################################################################

    _ai_helper: AbstractAIHelper = None
    _num_ai_requests: int = 0

    @property
    @noapidoc
    def ai_client(self) -> AbstractAIHelper:
        """Enables calling AI/LLM APIs - re-export of the initialized `openai` module"""
        # Create a singleton AIHelper instance
        if self._ai_helper is None:
            if self.G.config.secrets.openai_key is None:
                raise ValueError("OpenAI key is not set")

            self._ai_helper = MultiProviderAIHelper(openai_key=self.G.config.secrets.openai_key, use_openai=True, use_claude=False)
        return self._ai_helper

    def ai(self, prompt: str, target: Editable | None = None, context: Editable | list[Editable] | dict[str, Editable | list[Editable]] | None = None, model: str = "gpt-4o") -> str:
        """Generates a response from the AI based on the provided prompt, target, and context.

        A method that sends a prompt to the AI client along with optional target and context information to generate a response.
        Used for tasks like code generation, refactoring suggestions, and documentation improvements.

        Args:
            prompt (str): The text prompt to send to the AI.
            target (Editable | None): An optional editable object (like a function, class, etc.) that provides the main focus for the AI's response.
            context (Editable | list[Editable] | dict[str, Editable | list[Editable]] | None): Additional context to help inform the AI's response.
            model (str): The AI model to use for generating the response. Defaults to "gpt-4o".

        Returns:
            str: The generated response from the AI.

        Raises:
            MaxAIRequestsError: If the maximum number of allowed AI requests (default 150) has been exceeded.
        """
        # Check max transactions
        logger.info("Creating call to OpenAI...")
        self._num_ai_requests += 1
        if self.G.session_options.max_ai_requests is not None and self._num_ai_requests > self.G.session_options.max_ai_requests:
            logger.info(f"Max AI requests reached: {self.G.session_options.max_ai_requests}. Stopping codemod.")
            raise MaxAIRequestsError(f"Maximum number of AI requests reached: {self.G.session_options.max_ai_requests}", threshold=self.G.session_options.max_ai_requests)

        params = {
            "messages": [{"role": "system", "content": generate_system_prompt(target, context)}, {"role": "user", "content": prompt}],
            "model": model,
            "functions": generate_tools(),
            "temperature": 0,
        }
        if model.startswith("gpt"):
            params["tool_choice"] = "required"

        # Make the AI request
        response = self.ai_client.llm_query_functions(**params)

        # Handle finish reasons
        # First check if there is a response
        if response.choices:
            # Check response reason
            choice = response.choices[0]
            if choice.finish_reason == "tool_calls" or choice.finish_reason == "function_call" or choice.finish_reason == "stop":
                # Check if there is a tool call
                if choice.message.tool_calls:
                    tool_call = choice.message.tool_calls[0]
                    response_answer = json.loads(tool_call.function.arguments)
                    if "answer" in response_answer:
                        response_answer = response_answer["answer"]
                    else:
                        raise ValueError("No answer found in tool call. (tool_call.function.arguments does not contain answer)")
                else:
                    raise ValueError("No tool call found in AI response. (choice.message.tool_calls is empty)")
            elif choice.finish_reason == "length":
                raise ValueError("AI response too long / ran out of tokens. (choice.finish_reason == length)")
            elif choice.finish_reason == "content_filter":
                raise ValueError("AI response was blocked by OpenAI's content filter. (choice.finish_reason == content_filter)")
            else:
                raise ValueError(f"Unknown finish reason from AI: {choice.finish_reason}")
        else:
            raise ValueError("No response from AI Provider. (response.choices is empty)")

        # Agent sometimes fucks up and does \\\\n for some reason.
        response_answer = codecs.decode(response_answer, "unicode_escape")
        logger.info(f"OpenAI response: {response_answer}")
        return response_answer

    def set_ai_key(self, key: str) -> None:
        """Sets the AI key for the current codebase instance."""
        # Reset the AI client
        self._ai_helper = None

        # Set the AI key
        self.G.config.secrets.openai_key = key

    def find_by_span(self, span: Span) -> list[Editable]:
        """Finds editable objects that overlap with the given source code span.

        Searches for editable objects (like functions, classes, variables) within a file
        that overlap with the specified byte range span. Returns an empty list if no
        matching file is found.

        Args:
            span (Span): The span object containing the filepath and byte range to search within.

        Returns:
            list[Editable]: A list of Editable objects that overlap with the given span.
        """
        if file := self.get_file(span.filepath):
            return file.find_by_byte_range(span.range)
        return []

    def set_session_options(self, **kwargs: Unpack[SessionOptions]) -> None:
        """Sets the Session options for the current codebase."""
        self.G.session_options = self.G.session_options.model_copy(update=kwargs)
        self.G.transaction_manager.set_max_transactions(self.G.session_options.max_transactions)
        self.G.transaction_manager.reset_stopwatch(self.G.session_options.max_seconds)


# The last 2 lines of code are added to the runner. See codegen-backend/cli/generate/utils.py
# Type Aliases
CodebaseType = Codebase[SourceFile, Directory, Symbol, Class, Function, Import, Assignment, Interface, TypeAlias, Parameter, CodeBlock]
PyCodebaseType = Codebase[PyFile, Directory, PySymbol, PyClass, PyFunction, PyImport, PyAssignment, Interface, TypeAlias, PyParameter, PyCodeBlock]
TSCodebaseType = Codebase[TSFile, Directory, TSSymbol, TSClass, TSFunction, TSImport, TSAssignment, TSInterface, TSTypeAlias, TSParameter, TSCodeBlock]
