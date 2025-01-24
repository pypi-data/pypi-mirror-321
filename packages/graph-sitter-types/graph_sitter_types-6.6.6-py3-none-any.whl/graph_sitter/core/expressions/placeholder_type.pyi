"""
This type stub file was generated by pyright.
"""

from typing import Generic, TYPE_CHECKING, TypeVar
from codegen.utils.codemod.codemod_writer_decorators import apidoc
from graph_sitter.core.expressions.type import Type
from graph_sitter.core.interfaces.editable import Editable

if TYPE_CHECKING:
    ...
TType = TypeVar("TType", bound="Type")
Parent = TypeVar("Parent", bound="Editable")
@apidoc
class PlaceholderType(Type[Parent], Generic[TType, Parent]):
    """Represents a type that has not been implemented yet."""
    ...


