from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Generic, TypeVar

from tree_sitter import Node as TSNode

from codegen.utils.codemod.codemod_writer_decorators import apidoc, noapidoc
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.assignment import Assignment
from graph_sitter.core.dataclasses.usage import UsageKind
from graph_sitter.core.expressions import Expression
from graph_sitter.core.expressions.multi_expression import MultiExpression
from graph_sitter.core.expressions.name import Name
from graph_sitter.core.interfaces.has_name import HasName
from graph_sitter.core.interfaces.has_value import HasValue
from graph_sitter.core.interfaces.importable import Importable
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.statements.statement import Statement, StatementType
from graph_sitter.extensions.autocommit import commiter

if TYPE_CHECKING:
    from graph_sitter.core.detached_symbols.code_block import CodeBlock
    from graph_sitter.core.interfaces.has_block import HasBlock


TCodeBlock = TypeVar("TCodeBlock", bound="CodeBlock")
TAssignment = TypeVar("TAssignment", bound="Assignment")


@apidoc
class AssignmentStatement(Statement[TCodeBlock], HasValue, Generic[TCodeBlock, TAssignment]):
    """A class that represents an assignment statement in a codebase, such as `x = 1`, `a, b = 1, 2`, `const {a: b} = myFunc(),`, etc.

    This includes potentially multiple Assignments via `statement.assignments`, which represent each assignment of a value to a variable within this statement.

    For example, assigning to a destructured object, or assigning multiple values to multiple variables in a single statement.
    """

    statement_type = StatementType.ASSIGNMENT
    assignments: list[TAssignment]
    left: Expression[TAssignment]
    right: Expression[TAssignment] | None

    def __init__(self, ts_node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: TCodeBlock, pos: int, assignment_node: TSNode) -> None:
        super().__init__(ts_node, file_node_id, G, parent, pos=pos)
        self.assignments = self._DEPRECATED_parse_assignments().expressions
        if len(self.assignments) == 0:
            raise ValueError(f"No assignments found: {self.ts_node}\n\n{self.source}")

        first_assignment: TAssignment = self.assignments[0]
        self._name_node = self.G.parser.parse_expression(first_assignment.ts_node, self.file_node_id, self.G, parent, default=Name)
        self.left = first_assignment.left
        self.right = first_assignment.value
        self._value_node = self.right

    @abstractmethod
    def _parse_assignments(self, ts_node: TSNode) -> MultiExpression[HasBlock, TAssignment]: ...

    @abstractmethod
    def _DEPRECATED_parse_assignments(self) -> MultiExpression[HasBlock, TAssignment]: ...

    @noapidoc
    @commiter
    def _compute_dependencies(self, usage_type: UsageKind = UsageKind.BODY, dest: HasName | None = None) -> None:
        # We compute assignment dependencies separately
        pass

    @property
    @noapidoc
    def descendant_symbols(self) -> list[Importable]:
        """Returns the nested symbols of the importable object."""
        symbols = []
        for assignment in self.assignments:
            symbols.extend(assignment.descendant_symbols)
        return symbols
