from __future__ import annotations

from tree_sitter import Node as TSNode

from codegen.utils.codemod.codemod_writer_decorators import ts_apidoc
from graph_sitter.core.autocommit import reader
from graph_sitter.core.detached_symbols.decorator import Decorator
from graph_sitter.core.detached_symbols.function_call import FunctionCall


@ts_apidoc
class TSDecorator(Decorator["JSClass", "TSFunction", "TsParameter"]):
    """Abstract representation of a Decorator"""

    @reader
    def _get_name_node(self) -> TSNode:
        """Returns the name of the decorator."""
        for child in self.ts_node.children:
            # =====[ Identifier ]=====
            # Just `@dataclass` etc.
            if child.type == "identifier":
                return child

            # =====[ Attribute ]=====
            # e.g. `@a.b`
            elif child.type == "member_expression":
                return child

            # =====[ Call ]=====
            # e.g. `@a.b()`
            elif child.type == "call_expression":
                func = child.child_by_field_name("function")
                return func

        raise ValueError(f"Could not find decorator name within {self.source}")

    @property
    @reader
    def call(self) -> FunctionCall | None:
        """Retrieves the function call expression associated with the decorator.

        This property checks if the decorator has a function call expression (e.g., @decorator()) and returns it as a FunctionCall object.
        If the decorator is a simple identifier (e.g., @decorator), returns None.

        Returns:
            FunctionCall | None: A FunctionCall object representing the decorator's call expression if present, None otherwise.
        """
        if call_node := next((x for x in self.ts_node.named_children if x.type == "call_expression"), None):
            return FunctionCall(call_node, self.file_node_id, self.G, self.parent)
        return None
