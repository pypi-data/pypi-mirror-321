"""
This type stub file was generated by pyright.
"""

from typing import Generic, TypeVar
from codegen.utils.codemod.codemod_writer_decorators import apidoc
from graph_sitter.core.expressions import Expression
from graph_sitter.core.expressions.builtin import Builtin

Parent = TypeVar("Parent", bound="Expression")
@apidoc
class Number(Expression[Parent], Builtin, Generic[Parent]):
    """A number value.

    eg. 1, 2.0, 3.14
    """
    ...


