"""
This type stub file was generated by pyright.
"""

from typing import TypeVar
from codegen.utils.codemod.codemod_writer_decorators import py_apidoc
from graph_sitter.core.expressions.ternary_expression import TernaryExpression
from graph_sitter.core.interfaces.editable import Editable

Parent = TypeVar("Parent", bound="Editable")
@py_apidoc
class PyConditionalExpression(TernaryExpression[Parent]):
    """Conditional Expressions (A if condition else B)"""
    def __init__(self, ts_node, file_node_id, G, parent: Parent) -> None:
        ...
    


