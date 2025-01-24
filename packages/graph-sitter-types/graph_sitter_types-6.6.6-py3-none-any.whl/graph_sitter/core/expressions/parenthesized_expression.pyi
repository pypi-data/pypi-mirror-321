"""
This type stub file was generated by pyright.
"""

from typing import Generic, TypeVar, override
from codegen.utils.codemod.codemod_writer_decorators import apidoc
from graph_sitter.core.autocommit import writer
from graph_sitter.core.detached_symbols.function_call import FunctionCall
from graph_sitter.core.expressions import Expression
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.interfaces.has_value import HasValue
from graph_sitter.core.interfaces.unwrappable import Unwrappable
from graph_sitter.core.interfaces.wrapper_expression import IWrapper
from graph_sitter.extensions.autocommit import reader

Parent = TypeVar("Parent", bound="Editable")
@apidoc
class ParenthesizedExpression(Unwrappable[Parent], HasValue, IWrapper, Generic[Parent]):
    """An expression surrounded in a set of parenthesis.

    Example:
        ```typescript
        (5 + 5)
        ```
    """
    def __init__(self, ts_node, file_node_id, G, parent: Parent) -> None:
        ...
    
    @property
    @reader
    def function_calls(self) -> list[FunctionCall]:
        """Retrieves a list of function calls within a parenthesized expression.

        Gets all function calls from the resolved value of this parenthesized expression.

        Returns:
            list[FunctionCall]: A list of FunctionCall objects representing all function calls within the parenthesized expression.
        """
        ...
    
    @writer
    @override
    def unwrap(self, node: Expression | None = ...): # -> None:
        """Removes the parentheses from a parenthesized expression node.

        Modifies the AST by removing the parentheses from a ParenthesizedExpression node, leaving only the inner expression.

        Args:
            node (Expression | None, optional): The node to unwrap. Defaults to None.

        Returns:
            None
        """
        ...
    
    @writer
    def reduce_condition(self, bool_condition: bool, node: Editable) -> None:
        """Simplifies an expression based on a boolean condition.

        Args:
            bool_condition (bool): The boolean value to reduce the condition to.
            node (Editable): The node to be simplified.

        Returns:
            None
        """
        ...
    


