"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING
from tree_sitter import Node as TSNode
from codegen.utils.codemod.codemod_writer_decorators import noapidoc, py_apidoc
from graph_sitter.core.detached_symbols.function_call import FunctionCall
from graph_sitter.core.interfaces.importable import Importable
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.statements.while_statement import WhileStatement
from graph_sitter.extensions.autocommit import reader
from graph_sitter.python.interfaces.has_block import PyHasBlock
from graph_sitter.python.statements.if_block_statement import PyIfBlockStatement
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.python.detached_symbols.code_block import PyCodeBlock

if TYPE_CHECKING:
    ...
@py_apidoc
class PyWhileStatement(WhileStatement["PyCodeBlock"], PyHasBlock):
    """An abstract representation of a python while statement.

    Attributes:
        else_statement (PyIfBlockStatement | None): the statement that will run if the while loop completes, if any.
    """
    else_statement: PyIfBlockStatement[PyCodeBlock[PyWhileStatement]] | None = ...
    def __init__(self, ts_node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: PyCodeBlock, pos: int | None = ...) -> None:
        ...
    
    @property
    @reader
    def nested_code_blocks(self) -> list[PyCodeBlock]:
        """Returns a list of all code blocks nested within the while statement.

        Returns all code blocks contained within this while statement, including blocks from the else statement
        if it exists. The first block in the list is always the main while statement's code block.

        Returns:
            list[PyCodeBlock]: A list of code blocks contained within this statement, including those in the else branch.
        """
        ...
    
    @property
    @reader
    def function_calls(self) -> list[FunctionCall]:
        """Returns all function calls within the while statement and its else block.

        Returns a list of FunctionCall objects representing all function calls found in both the while statement's
        code block and its else block (if it exists). Function calls are sorted but not deduplicated.

        Returns:
            list[FunctionCall]: A sorted list of FunctionCall objects representing all function calls within the
                while statement and its else block.
        """
        ...
    
    @property
    @noapidoc
    def descendant_symbols(self) -> list[Importable]:
        ...
    


