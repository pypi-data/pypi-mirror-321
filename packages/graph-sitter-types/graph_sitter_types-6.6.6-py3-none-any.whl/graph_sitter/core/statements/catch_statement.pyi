"""
This type stub file was generated by pyright.
"""

from typing import Generic, Self, TYPE_CHECKING, TypeVar
from codegen.utils.codemod.codemod_writer_decorators import apidoc
from graph_sitter.core.expressions import Expression
from graph_sitter.core.statements.block_statement import BlockStatement
from graph_sitter.core.detached_symbols.code_block import CodeBlock

if TYPE_CHECKING:
    ...
Parent = TypeVar("Parent", bound="CodeBlock")
@apidoc
class CatchStatement(BlockStatement[Parent], Generic[Parent]):
    """Abstract representation catch clause.

    Attributes:
        code_block: The code block that may trigger an exception
        condition: The condition which triggers this clause
    """
    condition: Expression[Self] | None = ...


