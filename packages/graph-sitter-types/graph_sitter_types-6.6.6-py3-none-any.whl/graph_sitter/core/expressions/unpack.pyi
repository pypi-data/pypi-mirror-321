"""
This type stub file was generated by pyright.
"""

from typing import Generic, TypeVar
from codegen.utils.codemod.codemod_writer_decorators import apidoc
from graph_sitter.core.expressions import Expression
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.interfaces.has_value import HasValue
from graph_sitter.core.interfaces.unwrappable import Unwrappable
from graph_sitter.core.interfaces.wrapper_expression import IWrapper

Parent = TypeVar("Parent", bound="Editable")
@apidoc
class Unpack(Unwrappable[Parent], HasValue, IWrapper, Generic[Parent]):
    """Unpacking of an iterable.

    Example:
        ```python
        [a, *b]
        ```
    """
    def __init__(self, ts_node, file_node_id, G, parent: Parent) -> None:
        ...
    
    def unwrap(self, node: Expression | None = ...): # -> None:
        """Unwraps a node's content into its parent node.

        Unwraps the content of a node by removing its wrapping syntax and merging its content with its parent node.
        Specifically handles dictionary unwrapping, maintaining proper indentation and formatting.

        Args:
            node (Expression | None): The node to unwrap. If None, uses the instance's value node.

        Returns:
            None
        """
        ...
    


