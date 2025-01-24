from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

from codegen.utils.codemod.codemod_writer_decorators import py_apidoc
from graph_sitter.core.statements.block_statement import BlockStatement
from graph_sitter.extensions.autocommit import reader
from graph_sitter.python.detached_symbols.code_block import PyCodeBlock
from graph_sitter.python.interfaces.has_block import PyHasBlock

if TYPE_CHECKING:
    pass


Parent = TypeVar("Parent", bound="PyCodeBlock")


@py_apidoc
class PyBlockStatement(BlockStatement[Parent], PyHasBlock, Generic[Parent]):
    """Statement which contains a block."""

    @reader
    def _parse_code_block(self) -> PyCodeBlock | None:
        body_node = self.ts_node.child_by_field_name("body")
        if body_node is None:
            body_node = next(filter(lambda node: node.type == "block", self.ts_node.named_children))
        if body_node:
            return super()._parse_code_block(body_node)
