"""
This type stub file was generated by pyright.
"""

from collections.abc import Iterable, Iterator, MutableSequence
from typing import Generic, TYPE_CHECKING, TypeVar, overload
from tree_sitter import Node as TSNode
from codegen.utils.codemod.codemod_writer_decorators import noapidoc
from graph_sitter.core.autocommit import reader, writer
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.symbol_group import SymbolGroup
from graph_sitter.codebase.codebase_graph import CodebaseGraph

if TYPE_CHECKING:
    ...
Child = TypeVar("Child", bound="Editable")
Parent = TypeVar("Parent")
class Collection(SymbolGroup[Child, Parent], MutableSequence[Child], Generic[Child, Parent]):
    """Ordered collection of nodes
    Attributes:
        _bracket_size: Number of characters wrapping the collection
    """
    _elements: int
    _reversed: set[int]
    _inserts: dict[int, int]
    _pending_removes: int = ...
    _delimiter: str
    _indent: int = ...
    _bracket_size: int = ...
    _container_start_byte: int
    _container_end_byte: int
    def __init__(self, node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: Parent, delimiter: str = ..., children: list[Child] | None = ..., *, bracket_size: int = ...) -> None:
        ...
    
    @overload
    def __setitem__(self, key: int, value: str | Child) -> None:
        ...
    
    @overload
    def __setitem__(self, key: slice, value: Iterable[Child] | Iterable[str]) -> None:
        ...
    
    @writer
    def __setitem__(self, key: int | slice, value: str | Child | Iterable[Child] | Iterable[str]) -> None:
        ...
    
    @writer
    def __delitem__(self, key: int | slice) -> None:
        ...
    
    def __iter__(self) -> Iterator[Child]:
        ...
    
    @reader
    def __len__(self) -> int:
        ...
    
    @writer
    def remove(self, value: Child | None, *args, **kwargs) -> None:
        """Removes an element from a Collection.

        Deletes the specified element from the Collection by calling its remove method. If no value is specified,
        delegates to the parent class's remove method.

        Args:
            value (Child | None): The element to remove from the Collection. If None, delegates to parent class.
            *args: Variable length argument list to pass to the remove method.
            **kwargs: Arbitrary keyword arguments to pass to the remove method.

        Returns:
            None: This method doesn't return anything.
        """
        ...
    
    @writer
    def insert(self, index: int, value: str | Child) -> None:
        """Adds `value` to the container that this node represents
        Args:
            value: source to add
            index: If  provided, the `value` will be inserted at that index, otherwise will default to end of the list.
        """
        ...
    
    @property
    @reader
    def source(self) -> str:
        """Get the source code content of the node.

        Retrieves the underlying source code content associated with this node as stored in the _source attribute.

        Returns:
            str: The source code content of the node.
        """
        ...
    
    @source.setter
    @writer
    def source(self, value) -> None:
        """Set the source of the Editable instance by calling .edit(..)"""
        ...
    
    @writer
    def edit(self, *args, **kwargs) -> None:
        """Edit the source for this Collection instance.

        This method is used to update the source of a Collection while preserving its start and end brackets. It is primarily used internally by
        Collection to maintain structural integrity during edits.

        Args:
            *args: Variable length argument list passed to the parent Editable class's edit method.
            **kwargs: Arbitrary keyword arguments passed to the parent Editable class's edit method.

        Returns:
            None
        """
        ...
    
    @property
    @reader
    @noapidoc
    def uncommitted_len(self): # -> int:
        """Get the len of this list including pending removes and adds."""
        ...
    
    @reader
    def index(self, value: Child, start: int = ..., stop: int | None = ...) -> int:
        """Return the index of the first occurrence of value.

        Returns -1 if value is not present.
        """
        ...
    
    @noapidoc
    def reset(self): # -> None:
        ...
    


