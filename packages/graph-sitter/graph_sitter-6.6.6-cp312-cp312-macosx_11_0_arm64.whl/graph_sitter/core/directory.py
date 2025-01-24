import os
from itertools import chain
from typing import TYPE_CHECKING, Generic, Self, TypeVar

from codegen.utils.codemod.codemod_writer_decorators import apidoc

if TYPE_CHECKING:
    from graph_sitter.core.assignment import Assignment
    from graph_sitter.core.class_definition import Class
    from graph_sitter.core.file import File
    from graph_sitter.core.function import Function
    from graph_sitter.core.import_resolution import ImportStatement
    from graph_sitter.core.symbol import Symbol

import logging

logger = logging.getLogger(__name__)


TFile = TypeVar("TFile", bound="File")
TSymbol = TypeVar("TSymbol", bound="Symbol")
TImportStatement = TypeVar("TImportStatement", bound="ImportStatement")
TGlobalVar = TypeVar("TGlobalVar", bound="Assignment")
TClass = TypeVar("TClass", bound="Class")
TFunction = TypeVar("TFunction", bound="Function")


@apidoc
class Directory(Generic[TFile, TSymbol, TImportStatement, TGlobalVar, TClass, TFunction]):
    """Directory representation for codebase.
    GraphSitter abstraction of a file directory that can be used to look for files and symbols within a specific directory.
    """

    path: str
    parent: Self | None
    items: dict[str, TFile | Self]

    def __init__(self, path: str, parent: Self | None):
        self.path = path
        self.parent = parent
        self.items = dict()

    def __iter__(self):
        return iter(self.items.values())

    def __contains__(self, item: str | TFile | Self) -> bool:
        if isinstance(item, str):
            return item in self.items
        else:
            return item in self.items.values()

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, item_name: str) -> TFile | Self:
        return self.items[item_name]

    def __setitem__(self, item_name: str, item: TFile | Self) -> None:
        self.items[item_name] = item

    def __delitem__(self, item_name: str) -> None:
        del self.items[item_name]
        raise KeyError(f"Item {item_name} not found in directory {self.path}")

    def __repr__(self) -> str:
        return f"Directory({self.path}, {self.items.keys()})"

    @property
    def name(self) -> str:
        """Get the base name of the directory's path.

        Extracts the final component of the directory path. For example, for a path '/home/user/project', returns 'project'.

        Returns:
            str: The directory's base name.
        """
        return os.path.basename(self.path)

    @property
    def files(self) -> list[TFile]:
        """Get a recursive list of all files in the directory and its subdirectories."""
        files = []

        def _get_files(directory: Directory):
            for item in directory.items.values():
                if isinstance(item, Directory):
                    _get_files(item)
                else:
                    files.append(item)

        _get_files(self)
        return files

    @property
    def subdirectories(self) -> list[Self]:
        """Get a recursive list of all subdirectories in the directory and its subdirectories."""
        subdirectories = []

        def _get_subdirectories(directory: Directory):
            for item in directory.items.values():
                if isinstance(item, Directory):
                    subdirectories.append(item)
                    _get_subdirectories(item)

        _get_subdirectories(self)
        return subdirectories

    @property
    def symbols(self) -> list[TSymbol]:
        """Get a recursive list of all symbols in the directory and its subdirectories."""
        return list(chain.from_iterable(f.symbols for f in self.files))

    @property
    def import_statements(self) -> list[TImportStatement]:
        """Get a recursive list of all import statements in the directory and its subdirectories."""
        return list(chain.from_iterable(f.import_statements for f in self.files))

    @property
    def global_vars(self) -> list[TGlobalVar]:
        """Get a recursive list of all global variables in the directory and its subdirectories."""
        return list(chain.from_iterable(f.global_vars for f in self.files))

    @property
    def classes(self) -> list[TClass]:
        """Get a recursive list of all classes in the directory and its subdirectories."""
        return list(chain.from_iterable(f.classes for f in self.files))

    @property
    def functions(self) -> list[TFunction]:
        """Get a recursive list of all functions in the directory and its subdirectories."""
        return list(chain.from_iterable(f.functions for f in self.files))

    def get_symbol(self, name: str) -> TSymbol | None:
        """Get a symbol by name in the directory and its subdirectories."""
        return next((s for s in self.symbols if s.name == name), None)

    def get_import_statement(self, name: str) -> TImportStatement | None:
        """Get an import statement by name in the directory and its subdirectories."""
        return next((s for s in self.import_statements if s.name == name), None)

    def get_global_var(self, name: str) -> TGlobalVar | None:
        """Get a global variable by name in the directory and its subdirectories."""
        return next((s for s in self.global_vars if s.name == name), None)

    def get_class(self, name: str) -> TClass | None:
        """Get a class by name in the directory and its subdirectories."""
        return next((s for s in self.classes if s.name == name), None)

    def get_function(self, name: str) -> TFunction | None:
        """Get a function by name in the directory and its subdirectories."""
        return next((s for s in self.functions if s.name == name), None)

    def add_file(self, file: TFile) -> None:
        """Add a file to the directory."""
        rel_path = os.path.relpath(file.file_path, self.path)
        self.items[rel_path] = file

    def remove_file(self, file: TFile) -> None:
        """Remove a file from the directory."""
        rel_path = os.path.relpath(file.file_path, self.path)
        del self.items[rel_path]

    def remove_file_by_path(self, file_path: str) -> None:
        """Remove a file from the directory by its path."""
        rel_path = os.path.relpath(file_path, self.path)
        del self.items[rel_path]

    def get_file(self, filename: str, ignore_case: bool = False) -> TFile | None:
        """Get a file by its name relative to the directory."""
        from graph_sitter.core.file import File

        if ignore_case:
            return next((f for name, f in self.items.items() if name.lower() == filename.lower() and isinstance(f, File)), None)
        return self.items.get(filename, None)

    def add_subdirectory(self, subdirectory: Self) -> None:
        """Add a subdirectory to the directory."""
        rel_path = os.path.relpath(subdirectory.path, self.path)
        self.items[rel_path] = subdirectory

    def remove_subdirectory(self, subdirectory: Self) -> None:
        """Remove a subdirectory from the directory."""
        rel_path = os.path.relpath(subdirectory.path, self.path)
        del self.items[rel_path]

    def remove_subdirectory_by_path(self, subdirectory_path: str) -> None:
        """Remove a subdirectory from the directory by its path."""
        rel_path = os.path.relpath(subdirectory_path, self.path)
        del self.items[rel_path]

    def get_subdirectory(self, subdirectory_name: str) -> Self | None:
        """Get a subdirectory by its path relative to the directory."""
        return self.items.get(subdirectory_name, None)

    def remove(self):
        """Remove the directory and all its files and subdirectories."""
        for f in self.files:
            f.remove()

    def update_filepath(self, new_filepath: str) -> None:
        """Update the filepath of the directory."""
        old_path = self.path
        new_path = new_filepath

        for file in self.files:
            new_file_path = os.path.join(new_path, os.path.relpath(file.file_path, old_path))
            file.update_filepath(new_file_path)

    def rename(self, new_name: str) -> None:
        """Rename the directory."""
        parent_dir, _ = os.path.split(self.path)
        new_path = os.path.join(parent_dir, new_name)
        self.update_filepath(new_path)
