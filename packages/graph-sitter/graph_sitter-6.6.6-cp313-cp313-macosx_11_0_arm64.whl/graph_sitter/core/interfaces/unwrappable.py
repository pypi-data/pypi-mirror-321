from abc import abstractmethod
from typing import Generic

from typing_extensions import TypeVar

from codegen.utils.codemod.codemod_writer_decorators import apidoc
from graph_sitter.core.expressions import Expression
from graph_sitter.core.interfaces.editable import Editable

Parent = TypeVar("Parent", bound=Editable)


@apidoc
class Unwrappable(Expression[Parent], Generic[Parent]):
    """An abstract representation of an expression that can be unwrapped.
    Expressions that can be unwrapped include binary expressions and ternary expressions.
    """

    @abstractmethod
    def unwrap(self, node: Expression | None = None):
        """Unwrap this expression, removing parenthesis and other syntax elements while maintaining the function of the code.

        Args:
            node: the node that's remaining. If None, assume all children of this expression are kept
        """
