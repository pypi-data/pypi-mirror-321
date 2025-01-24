"""
This type stub file was generated by pyright.
"""

from typing import Generic, TypeVar
from codegen.utils.codemod.codemod_writer_decorators import ts_apidoc
from graph_sitter.core.detached_symbols.function_call import FunctionCall
from graph_sitter.core.expressions import Expression, Name
from graph_sitter.core.expressions.chained_attribute import ChainedAttribute
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.extensions.autocommit import reader

Parent = TypeVar("Parent", bound="Editable")
@ts_apidoc
class TSChainedAttribute(ChainedAttribute[Expression, Name, Parent], Generic[Parent]):
    """A TypeScript chained attribute class representing member access expressions.

    This class handles the representation and analysis of chained attribute access expressions in TypeScript,
    such as 'object.property' or 'object.method()'. It provides functionality for accessing the object
    and property components of the expression, as well as analyzing function calls made on the object.
    """
    def __init__(self, ts_node, file_node_id, G, parent: Parent) -> None:
        ...
    
    @property
    @reader
    def function_calls(self) -> list[FunctionCall]:
        """Returns a list of function calls associated with this chained attribute's object.

        Retrieves all function calls made on the object component of this chained attribute.
        This is useful for analyzing call sites and call patterns in code analysis and refactoring tasks.

        Returns:
            list[FunctionCall]: A list of function calls made on this chained attribute's object.
        """
        ...
    


