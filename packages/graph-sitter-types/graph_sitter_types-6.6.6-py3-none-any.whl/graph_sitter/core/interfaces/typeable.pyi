"""
This type stub file was generated by pyright.
"""

from typing import Generic, Self, TYPE_CHECKING, TypeVar
from codegen.utils.codemod.codemod_writer_decorators import apidoc
from graph_sitter.core.autocommit import reader
from graph_sitter.core.interfaces.chainable import Chainable
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.placeholder.placeholder_type import TypePlaceholder
from graph_sitter.core.expressions.type import Type

if TYPE_CHECKING:
    ...
TType = TypeVar("TType", bound="Type")
Parent = TypeVar("Parent", bound="Editable")
@apidoc
class Typeable(Chainable[Parent], Generic[TType, Parent]):
    """An interface for any node object that can be typed, eg. function parameters, variables, etc.

    Attributes:
        type: The type annotation associated with this node
    """
    type: TType | TypePlaceholder[Self]
    @property
    @reader
    def is_typed(self) -> bool:
        """Indicates if a node has an explicit type annotation.

        Returns:
            bool: True if the node has an explicit type annotation, False otherwise.
        """
        ...
    


