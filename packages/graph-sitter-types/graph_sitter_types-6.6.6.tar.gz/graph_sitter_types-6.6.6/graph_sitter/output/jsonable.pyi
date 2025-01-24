"""
This type stub file was generated by pyright.
"""

from abc import ABC, abstractmethod
from tree_sitter import Node as TSNode
from codegen.utils.codemod.codemod_writer_decorators import noapidoc
from graph_sitter.codebase.span import Span
from graph_sitter.output.placeholder import Placeholder
from graph_sitter.types import JSON

BLACKLIST = ...
@noapidoc
class JSONable(ABC):
    ts_node: TSNode
    @noapidoc
    def json(self, max_depth: int = ..., methods: bool = ...) -> JSON:
        ...
    
    @property
    @noapidoc
    def placeholder(self) -> Placeholder:
        """Property that returns a placeholder representation of the current object.

        Creates a Placeholder object representing the current object, typically when a full JSON
        representation cannot be provided due to depth limitations.

        Returns:
            Placeholder: A simplified representation containing the object's span, string representation,
                kind_id from the TreeSitter node, and class name.
        """
        ...
    
    @property
    @abstractmethod
    @noapidoc
    def span(self) -> Span:
        ...
    


