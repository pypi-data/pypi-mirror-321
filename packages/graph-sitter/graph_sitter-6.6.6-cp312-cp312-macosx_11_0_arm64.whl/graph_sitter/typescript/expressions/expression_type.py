from typing import Generic, TypeVar

from tree_sitter import Node as TSNode

from codegen.utils.codemod.codemod_writer_decorators import ts_apidoc
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.expressions import Expression
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.typescript.expressions.named_type import TSNamedType

Parent = TypeVar("Parent", bound="Editable")


@ts_apidoc
class TSExpressionType(TSNamedType, Generic[Parent]):
    """Type defined by evaluation of an expression

    Attributes:
        expression: The expression to evaluate that yields the type
    """

    expression: Expression["TSExpressionType[Parent]"]

    def __init__(self, ts_node: TSNode, file_node_id: NodeId, G: "CodebaseGraph", parent: Parent):
        super().__init__(ts_node, file_node_id, G, parent)
        self.expression = self._parse_expression(ts_node)
