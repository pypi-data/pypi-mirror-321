from typing import TYPE_CHECKING, TypeVar

from tree_sitter import Node as TSNode

from codegen.utils.codemod.codemod_writer_decorators import ts_apidoc
from graph_sitter.core.expressions.named_type import NamedType

if TYPE_CHECKING:
    pass
Parent = TypeVar("Parent")


@ts_apidoc
class TSNamedType(NamedType[Parent]):
    """Named type
    Examples:
        string
    """

    def _get_name_node(self) -> TSNode | None:
        return self.ts_node
