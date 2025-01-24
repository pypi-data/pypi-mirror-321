"""
This type stub file was generated by pyright.
"""

from typing import Generic, TYPE_CHECKING, TypeVar
from tree_sitter import Node as TSNode
from codegen.utils.codemod.codemod_writer_decorators import apidoc
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.autocommit import reader
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.statements.if_block_statement import IfBlockStatement
from graph_sitter.typescript.detached_symbols.code_block import TSCodeBlock

if TYPE_CHECKING:
    ...
logger = ...
Parent = TypeVar("Parent", bound="TSCodeBlock")
@apidoc
class TSIfBlockStatement(IfBlockStatement[Parent, "TSIfBlockStatement"], Generic[Parent]):
    """Typescript implementation of the if/elif/else statement block.
    For example, if there is a code block like:
    if (condition1) {
        block1
    } else if (condition2) {
        block2
    } else {
        block3
    }
    This class represents the entire block, including the conditions and nested code blocks.
    """
    statement_type = ...
    _else_clause_node: TSNode | None = ...
    def __init__(self, ts_node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: Parent, pos: int, else_clause_node: TSNode | None = ..., main_if_block: TSIfBlockStatement | None = ...) -> None:
        ...
    
    @property
    @reader
    def is_if_statement(self) -> bool:
        """Determines if the current block is a standalone 'if' statement.

        Args:
            None

        Returns:
            bool: True if the current block is a standalone 'if' statement, False otherwise.
        """
        ...
    
    @property
    @reader
    def is_else_statement(self) -> bool:
        """Determines if the current block is an else block.

        A property that checks if the current TreeSitter node represents an else clause in an if/elif/else statement structure.

        Returns:
            bool: True if the current block is an else block, False otherwise.
        """
        ...
    
    @property
    @reader
    def is_elif_statement(self) -> bool:
        """Determines if the current block is an elif block.

        This method checks if the current block is an elif block by verifying that it is both an if_statement and has an else clause node associated with it.

        Returns:
            bool: True if the current block is an elif block, False otherwise.
        """
        ...
    


