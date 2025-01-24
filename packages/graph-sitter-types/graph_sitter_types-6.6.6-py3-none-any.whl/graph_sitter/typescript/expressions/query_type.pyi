"""
This type stub file was generated by pyright.
"""

from typing import Generic, Self, TYPE_CHECKING, TypeVar
from tree_sitter import Node as TSNode
from codegen.utils.codemod.codemod_writer_decorators import ts_apidoc
from graph_sitter.core.autocommit import reader
from graph_sitter.core.expressions.type import Type
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.typescript.expressions.type import TSType

if TYPE_CHECKING:
    ...
Parent = TypeVar("Parent")
@ts_apidoc
class TSQueryType(Type[Parent], Generic[Parent]):
    """Type query

    Examples:
    typeof s
    """
    query: TSType[Self]
    def __init__(self, ts_node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: Parent) -> None:
        ...
    
    @property
    @reader
    def name(self) -> str | None:
        """Returns the name of the query type.

        A property that retrieves the name of the query type. This property is used to get the name
        associated with TypeScript type queries (e.g., 'typeof s').

        Returns:
            str | None: The name of the query type, or None if no name is available.
        """
        ...
    


