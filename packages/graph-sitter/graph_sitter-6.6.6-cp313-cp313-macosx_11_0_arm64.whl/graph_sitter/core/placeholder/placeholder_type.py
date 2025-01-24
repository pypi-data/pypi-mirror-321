from typing import Generic, TypeVar

from codegen.utils.codemod.codemod_writer_decorators import apidoc
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.placeholder.placeholder import Placeholder

Parent = TypeVar("Parent", bound="Editable")


@apidoc
class TypePlaceholder(Placeholder[Parent], Generic[Parent]):
    """A placeholder for a Type node that does not exist.
    Can be populated using the `edit` method.
    """

    def edit(self, new_src: str, fix_indentation: bool = False, priority: int = 0, dedupe: bool = True) -> None:
        """Edits the type annotation of a placeholder node.

        Modifies the source code by adding or updating a type annotation after a node.
        Handles cases where the parent node has children and adjusts spacing accordingly.

        Args:
            new_src (str): The new type annotation text to be inserted.
            fix_indentation (bool, optional): Whether to fix the indentation of the new source.
            priority (int, optional): Priority of the edit operation.
            dedupe (bool, optional): Whether to remove duplicate edits.

        Returns:
            None
        """
        if len(self._parent_node.children) == 0:
            self._parent_node.insert_after(": " + new_src, newline=False)
        else:
            if len(self._parent_node.children) > 1 and " " in self._parent_node.source:
                new_src = new_src + " "
            self._parent_node.children[0].insert_after(": " + new_src, newline=False)
