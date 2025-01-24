"""
This type stub file was generated by pyright.
"""

from typing import Generic, TYPE_CHECKING, TypeVar
from codegen.utils.codemod.codemod_writer_decorators import apidoc, noapidoc
from graph_sitter.core.autocommit import writer
from graph_sitter.core.expressions.expression import Expression
from graph_sitter.core.interfaces.resolvable import Resolvable

if TYPE_CHECKING:
    ...
Parent = TypeVar("Parent", bound="Expression")
@apidoc
class Name(Expression[Parent], Resolvable, Generic[Parent]):
    """Editable attribute on any given code objects that has a name.

    For example, function, classes, global variable, interfaces, attributes, parameters are all
    composed of a name.
    """
    @noapidoc
    @writer
    def rename_if_matching(self, old: str, new: str): # -> None:
        ...
    


