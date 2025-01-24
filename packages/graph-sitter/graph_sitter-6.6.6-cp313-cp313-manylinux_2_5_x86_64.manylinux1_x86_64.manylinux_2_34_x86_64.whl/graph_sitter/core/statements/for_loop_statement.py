from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, Generic, Self, TypeVar

from codegen.utils.codemod.codemod_writer_decorators import apidoc
from graph_sitter.core.expressions import Expression
from graph_sitter.core.import_resolution import Import, WildcardImport
from graph_sitter.core.interfaces.chainable import Chainable
from graph_sitter.core.interfaces.has_block import HasBlock
from graph_sitter.core.statements.block_statement import BlockStatement
from graph_sitter.core.statements.statement import StatementType
from graph_sitter.core.symbol import Symbol
from graph_sitter.core.symbol_groups.collection import Collection

if TYPE_CHECKING:
    from graph_sitter.core.detached_symbols.code_block import CodeBlock


Parent = TypeVar("Parent", bound="CodeBlock")


@apidoc
class ForLoopStatement(BlockStatement[Parent], HasBlock, ABC, Generic[Parent]):
    """Abstract representation of the for loop.

    Attributes:
        code_block: The code block that is executed in each iteration of the loop
    """

    statement_type = StatementType.FOR_LOOP_STATEMENT
    item: Expression[Self] | None = None
    iterable: Expression[Self]

    def resolve_name(self, name: str, start_byte: int | None = None) -> Symbol | Import | WildcardImport | None:
        if self.item and isinstance(self.iterable, Chainable):
            if start_byte is None or start_byte > self.iterable.end_byte:
                if name == self.item:
                    for frame in self.iterable.resolved_type_frames:
                        if frame.generics:
                            return next(iter(frame.generics.values()))
                        return frame.top.node
                elif isinstance(self.item, Collection):
                    for idx, item in enumerate(self.item):
                        if item == name:
                            for frame in self.iterable.resolved_type_frames:
                                if frame.generics and len(frame.generics) > idx:
                                    return list(frame.generics.values())[idx]
                                return frame.top.node
        return super().resolve_name(name, start_byte)
