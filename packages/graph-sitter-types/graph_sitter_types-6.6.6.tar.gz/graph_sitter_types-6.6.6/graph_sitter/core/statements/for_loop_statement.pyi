"""
This type stub file was generated by pyright.
"""

from abc import ABC
from typing import Generic, Self, TYPE_CHECKING, TypeVar
from codegen.utils.codemod.codemod_writer_decorators import apidoc
from graph_sitter.core.expressions import Expression
from graph_sitter.core.import_resolution import Import, WildcardImport
from graph_sitter.core.interfaces.has_block import HasBlock
from graph_sitter.core.statements.block_statement import BlockStatement
from graph_sitter.core.symbol import Symbol
from graph_sitter.core.detached_symbols.code_block import CodeBlock

if TYPE_CHECKING:
    ...
Parent = TypeVar("Parent", bound="CodeBlock")
@apidoc
class ForLoopStatement(BlockStatement[Parent], HasBlock, ABC, Generic[Parent]):
    """Abstract representation of the for loop.

    Attributes:
        code_block: The code block that is executed in each iteration of the loop
    """
    statement_type = ...
    item: Expression[Self] | None = ...
    iterable: Expression[Self]
    def resolve_name(self, name: str, start_byte: int | None = ...) -> Symbol | Import | WildcardImport | None:
        ...
    


