from __future__ import annotations

from typing import TYPE_CHECKING, Self, override

from tree_sitter import Node as TSNode

from codegen.utils.codemod.codemod_writer_decorators import noapidoc, ts_apidoc
from graph_sitter.core.dataclasses.usage import UsageKind
from graph_sitter.core.detached_symbols.function_call import FunctionCall
from graph_sitter.core.interfaces.has_name import HasName
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.statements.try_catch_statement import TryCatchStatement
from graph_sitter.extensions.autocommit import commiter, reader
from graph_sitter.typescript.statements.block_statement import TSBlockStatement
from graph_sitter.typescript.statements.catch_statement import TSCatchStatement

if TYPE_CHECKING:
    from graph_sitter.codebase.codebase_graph import CodebaseGraph
    from graph_sitter.core.interfaces.importable import Importable
    from graph_sitter.typescript.detached_symbols.code_block import TSCodeBlock


@ts_apidoc
class TSTryCatchStatement(TryCatchStatement["TSCodeBlock"], TSBlockStatement):
    """Abstract representation of the try/catch/finally block in TypeScript.

    Attributes:
        catch: The catch block.
    """

    catch: TSCatchStatement[Self] | None = None

    def __init__(self, ts_node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: TSCodeBlock, pos: int | None = None) -> None:
        super().__init__(ts_node, file_node_id, G, parent, pos)
        if handler_node := self.ts_node.child_by_field_name("handler"):
            self.catch = TSCatchStatement(handler_node, file_node_id, G, self.code_block)
        if finalizer_node := self.ts_node.child_by_field_name("finalizer"):
            self.finalizer = TSBlockStatement(finalizer_node, file_node_id, G, self.code_block)

    @property
    @reader
    def function_calls(self) -> list[FunctionCall]:
        """Gets all function calls within a try-catch-finally statement.

        This property retrieves all function calls from the try block, catch block (if present), and finally block (if present).

        Returns:
            list[FunctionCall]: A list of function calls found within the try-catch-finally statement, including those from
            the try block, catch block (if it exists), and finally block (if it exists).
        """
        fcalls = super().function_calls
        if self.catch:
            fcalls.extend(self.catch.function_calls)
        if self.finalizer:
            fcalls.extend(self.finalizer.function_calls)
        return fcalls

    @noapidoc
    @commiter
    def _compute_dependencies(self, usage_type: UsageKind | None = None, dest: HasName | None = None) -> None:
        super()._compute_dependencies(usage_type, dest)
        if self.catch:
            self.catch._compute_dependencies(usage_type, dest)
        if self.finalizer:
            self.finalizer._compute_dependencies(usage_type, dest)

    @property
    @noapidoc
    def descendant_symbols(self) -> list[Importable]:
        symbols = super().descendant_symbols
        if self.catch:
            symbols.extend(self.catch.descendant_symbols)
        if self.finalizer:
            symbols.extend(self.finalizer.descendant_symbols)
        return symbols

    @property
    @reader
    @override
    def nested_code_blocks(self) -> list[TSCodeBlock]:
        """Returns all nested CodeBlocks within the statement.

        Retrieves a list of all the code blocks nested within this try/catch/finally statement, including the catch and finally blocks if they exist.

        Returns:
            list[TSCodeBlock]: A list of nested code blocks, including the catch and finally blocks.
        """
        nested_blocks = super().nested_code_blocks
        if self.catch:
            nested_blocks.append(self.catch.code_block)
        if self.finalizer:
            nested_blocks.append(self.finalizer.code_block)
        return nested_blocks
