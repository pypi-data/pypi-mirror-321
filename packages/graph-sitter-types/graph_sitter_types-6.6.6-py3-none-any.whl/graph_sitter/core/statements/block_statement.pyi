"""
This type stub file was generated by pyright.
"""

from abc import ABC
from typing import Generic, TYPE_CHECKING, TypeVar
from tree_sitter import Node as TSNode
from codegen.utils.codemod.codemod_writer_decorators import apidoc, noapidoc
from graph_sitter.core.detached_symbols.function_call import FunctionCall
from graph_sitter.core.interfaces.has_block import HasBlock
from graph_sitter.core.interfaces.importable import Importable
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.statements.statement import Statement
from graph_sitter.extensions.autocommit import reader
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.detached_symbols.code_block import CodeBlock

if TYPE_CHECKING:
    ...
TCodeBlock = TypeVar("TCodeBlock", bound="CodeBlock")
@apidoc
class BlockStatement(Statement[TCodeBlock], HasBlock, ABC, Generic[TCodeBlock]):
    """Statement which contains a block."""
    code_block: TCodeBlock | None
    def __init__(self, ts_node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: TCodeBlock, pos: int | None = ...) -> None:
        ...
    
    @property
    @reader
    def nested_code_blocks(self) -> list[TCodeBlock]:
        """Returns all nested CodeBlocks within the statement.

        Gets all nested CodeBlocks contained within this BlockStatement. A BlockStatement may contain
        at most one code block.

        Args:
            None

        Returns:
            list[TCodeBlock]: A list containing the statement's code block if it exists, otherwise an empty list.
        """
        ...
    
    @property
    @reader
    def function_calls(self) -> list[FunctionCall]:
        """Gets all function calls within the statement's code block.

        Returns a list of FunctionCall instances contained within the statement's code block. If the statement does not have a code block, returns an empty list.

        Returns:
            list[FunctionCall]: A list of function call instances within the code block.
        """
        ...
    
    @property
    @noapidoc
    def descendant_symbols(self) -> list[Importable]:
        ...
    


