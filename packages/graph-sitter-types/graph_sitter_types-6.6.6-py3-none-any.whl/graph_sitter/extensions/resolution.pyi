"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from functools import cached_property as cached_property
from typing import Generic
from typing_extensions import TypeVar
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.dataclasses.usage import UsageKind, UsageType
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.interfaces.has_name import HasName

NodeType = TypeVar("NodeType")
@dataclass
class ResolutionStack(Generic[NodeType]):
    """Represents the resolution stack from a symbol to a usage

    Symbol
    ...
    <Imports, Assignments, Etc>

    Attributes:
        aliased: If this was aliased at any point
        parent_frame: The frame above this frame
    """
    node: NodeType = ...
    parent_frame: ResolutionStack | None = ...
    direct: bool = ...
    aliased: bool = ...
    chained: bool = ...
    generics: dict = ...
    def with_frame(self, node, direct: bool = ..., aliased: bool = ..., chained: bool = ..., generics: dict | None = ...) -> ResolutionStack:
        """Adds node to the Resolution stack and returns it as a new frame."""
        ...
    
    def usage_type(self, direct: bool, aliased: bool) -> UsageType:
        ...
    
    def add_usage(self, match: Editable, usage_type: UsageKind, dest: HasName, G: CodebaseGraph, *, direct: bool = ..., aliased: bool = ..., chained: bool = ...) -> None:
        """Add the resolved type to the graph. Also adds any intermediate nodes as usages as well if they are on the graph."""
        ...
    
    @cached_property
    def top(self) -> ResolutionStack:
        ...
    
    @cached_property
    def is_direct_usage(self) -> bool:
        ...
    
    def with_new_base(self, base, *args, **kwargs) -> ResolutionStack:
        ...
    
    def with_new_base_frame(self, base: ResolutionStack) -> ResolutionStack:
        ...
    
    def __init__(self, node, parent_frame=..., aliased=..., direct=..., _seen=...) -> None:
        ...
    


