from __future__ import annotations

from typing import TYPE_CHECKING

from tree_sitter import Node as TSNode

from codegen.utils.codemod.codemod_writer_decorators import py_apidoc
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.expressions.multi_expression import MultiExpression
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.statements.assignment_statement import AssignmentStatement
from graph_sitter.extensions.utils import find_all_descendants
from graph_sitter.python.assignment import PyAssignment

if TYPE_CHECKING:
    from graph_sitter.python.detached_symbols.code_block import PyCodeBlock
    from graph_sitter.python.interfaces.has_block import PyHasBlock

import logging

logger = logging.getLogger(__name__)


@py_apidoc
class PyAssignmentStatement(AssignmentStatement["PyCodeBlock", PyAssignment]):
    """A class that represents a Python assignment statement in a codebase, such as `x = 1` or `a, b = 1, 2`.

    This includes potentially multiple Assignments via `statement.assignments`, which represent each assignment of a value to a variable within this statement.

    For example, assigning to a list, or assigning multiple values to multiple variables in a single statement.
    """

    assignment_types = {"assignment", "augmented_assignment", "named_expression"}

    @classmethod
    def from_assignment(cls, ts_node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: PyCodeBlock, pos: int, assignment_node: TSNode) -> PyAssignmentStatement:
        """Creates a PyAssignmentStatement instance from a TreeSitter assignment node.

        Factory method to create appropriate assignment statement objects based on the node type and parent context.
        If the parent is a PyClass, creates a PyAttribute, otherwise creates a PyAssignmentStatement.

        Args:
            ts_node (TSNode): The TreeSitter node representing the entire statement.
            file_node_id (NodeId): The ID of the file containing this node.
            G (CodebaseGraph): The codebase graph instance.
            parent (PyHasBlock): The parent block containing this statement.
            code_block (PyCodeBlock): The code block containing this statement.
            pos (int): The position of this statement within its code block.
            assignment_node (TSNode): The TreeSitter node representing the assignment operation.

        Returns:
            PyAssignmentStatement: A new assignment statement instance, either PyAttribute or PyAssignmentStatement.

        Raises:
            ValueError: If the assignment_node type is not one of the supported assignment types.
        """
        if assignment_node.type not in cls.assignment_types:
            raise ValueError(f"Invalid assignment node type: {assignment_node.type}")

        from graph_sitter.python.class_definition import PyClass

        if isinstance(parent, PyClass):
            from graph_sitter.python.statements.attribute import PyAttribute

            return PyAttribute(ts_node, file_node_id, G, parent, pos, assignment_node=assignment_node)
        return cls(ts_node, file_node_id, G, parent, pos, assignment_node=assignment_node)

    def _parse_assignments(self, assignment_node: TSNode) -> MultiExpression[PyHasBlock, PyAssignment]:
        if assignment_node.type in ["assignment", "augmented_assignment"]:
            return PyAssignment.from_assignment(assignment_node, self.file_node_id, self.G, self.parent)
        elif assignment_node.type == "named_expression":
            return PyAssignment.from_named_expression(assignment_node, self.file_node_id, self.G, self.parent)

        logger.info(f"Unknown assignment type: {assignment_node.type}")
        return MultiExpression(assignment_node, self.file_node_id, self.G, self.parent, [self.parent._parse_expression(assignment_node)])

    def _DEPRECATED_parse_assignments(self) -> MultiExpression[PyHasBlock, PyAssignment]:
        assignments = []
        for assignment in find_all_descendants(self.ts_node, {"assignment", "augmented_assignment"}, max_depth=5):
            left = assignment.child_by_field_name("left")
            right = assignment.child_by_field_name("right")
            if left.type == "pattern_list":
                for identifier in find_all_descendants(left, {"identifier", "attribute"}):
                    assignments.append(PyAssignment(assignment, self.file_node_id, self.G, self, left, right, identifier))
            else:
                assignments.append(PyAssignment(assignment, self.file_node_id, self.G, self, left, right, left))

        return MultiExpression(self.ts_node, self.file_node_id, self.G, self.parent, assignments)
