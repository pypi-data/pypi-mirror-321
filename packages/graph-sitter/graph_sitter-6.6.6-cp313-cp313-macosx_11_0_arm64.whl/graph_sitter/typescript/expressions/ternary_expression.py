from typing import TypeVar

from codegen.utils.codemod.codemod_writer_decorators import ts_apidoc
from graph_sitter.core.expressions.ternary_expression import TernaryExpression
from graph_sitter.core.interfaces.editable import Editable

Parent = TypeVar("Parent", bound="Editable")


@ts_apidoc
class TSTernaryExpression(TernaryExpression[Parent]):
    """Any ternary expression in the code where a condition will determine branched execution"""

    def __init__(self, ts_node, file_node_id, G, parent: Parent) -> None:
        super().__init__(ts_node, file_node_id, G, parent=parent)
        self.condition = self.child_by_field_name("condition")
        self.consequence = self.child_by_field_name("consequence")
        self.alternative = self.child_by_field_name("alternative")
