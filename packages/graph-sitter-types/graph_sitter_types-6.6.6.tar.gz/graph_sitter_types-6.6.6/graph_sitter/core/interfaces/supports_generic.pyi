"""
This type stub file was generated by pyright.
"""

from typing import Generic, Self, TYPE_CHECKING
from typing_extensions import TypeVar
from codegen.utils.codemod.codemod_writer_decorators import noapidoc
from graph_sitter.core.symbol import Symbol
from graph_sitter.core.symbol_groups.type_parameters import TypeParameters
from graph_sitter.extensions.utils import cached_property
from graph_sitter.core.expressions import Type

if TYPE_CHECKING:
    ...
TType = TypeVar("TType", bound="Type")
class SupportsGenerics(Symbol, Generic[TType]):
    type_parameters: TypeParameters[TType, Self] | None = ...
    @cached_property
    @noapidoc
    def generics(self) -> dict[str, TType]:
        ...
    


