from __future__ import annotations

from typing import TYPE_CHECKING

from tree_sitter import Node as TSNode

from codegen.utils.codemod.codemod_writer_decorators import noapidoc, py_apidoc
from graph_sitter.core.dataclasses.usage import UsageKind
from graph_sitter.core.detached_symbols.function_call import FunctionCall
from graph_sitter.core.expressions import Expression
from graph_sitter.core.interfaces.has_name import HasName
from graph_sitter.core.interfaces.importable import Importable
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.statements.for_loop_statement import ForLoopStatement
from graph_sitter.extensions.autocommit import commiter, reader
from graph_sitter.python.statements.block_statement import PyBlockStatement

if TYPE_CHECKING:
    from graph_sitter.codebase.codebase_graph import CodebaseGraph
    from graph_sitter.python.detached_symbols.code_block import PyCodeBlock


@py_apidoc
class PyForLoopStatement(ForLoopStatement["PyCodeBlock"], PyBlockStatement):
    """Abstract representation of the for loop in Python

    Attributes:
        item: An item in the iterable object
        iterable: The iterable that is being iterated over
    """

    item: Expression[PyForLoopStatement]
    iterable: Expression[PyForLoopStatement]

    def __init__(self, ts_node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: PyCodeBlock, pos: int | None = None) -> None:
        super().__init__(ts_node, file_node_id, G, parent, pos)
        self.item = self.child_by_field_name("left")
        self.iterable = self.child_by_field_name("right")

    @property
    @reader
    def function_calls(self) -> list[FunctionCall]:
        """Gets all function calls within this for loop statement.

        A property that retrieves all function calls from the iterable expression and combines them with any function
        calls from the parent class implementation. This includes function calls within the iterable expression and
        any function calls in the loop body.

        Returns:
            list[FunctionCall]: A list of all function calls within the for loop statement, including those from
                both the iterable expression and the parent class implementation.
        """
        fcalls = self.iterable.function_calls
        fcalls.extend(super().function_calls)
        return fcalls

    @noapidoc
    @commiter
    def _compute_dependencies(self, usage_type: UsageKind | None = None, dest: HasName | None = None) -> None:
        self.item._compute_dependencies(usage_type, dest)
        self.iterable._compute_dependencies(usage_type, dest)
        super()._compute_dependencies(usage_type, dest)

    @property
    @noapidoc
    def descendant_symbols(self) -> list[Importable]:
        symbols = []
        symbols.extend(self.item.descendant_symbols)
        symbols.extend(self.iterable.descendant_symbols)
        symbols.extend(super().descendant_symbols)
        return symbols
