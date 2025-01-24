"""
This type stub file was generated by pyright.
"""

from typing import override
from tree_sitter import Node as TSNode
from codegen.utils.codemod.codemod_writer_decorators import noapidoc, py_apidoc
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.autocommit import commiter, reader, writer
from graph_sitter.core.function import Function
from graph_sitter.core.import_resolution import Import, WildcardImport
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.symbol import Symbol
from graph_sitter.extensions.utils import cached_property
from graph_sitter.python.detached_symbols.code_block import PyCodeBlock
from graph_sitter.python.detached_symbols.decorator import PyDecorator
from graph_sitter.python.detached_symbols.parameter import PyParameter
from graph_sitter.python.expressions.type import PyType
from graph_sitter.python.interfaces.has_block import PyHasBlock
from graph_sitter.python.symbol import PySymbol

logger = ...
@py_apidoc
class PyFunction(Function["PyFunction", PyDecorator, PyCodeBlock, PyParameter, PyType], PyHasBlock, PySymbol):
    """Extends Function for Python codebases."""
    _decorated_node: TSNode | None
    def __init__(self, ts_node: TSNode, file_id: NodeId, G: CodebaseGraph, parent: PyHasBlock, decorated_node: TSNode | None = ...) -> None:
        ...
    
    @cached_property
    @reader
    def is_private(self) -> bool:
        """Determines if a method is a private method.

        Private methods in Python start with an underscore and are not magic methods.

        Returns:
            bool: True if the method is private (starts with '_' and is not a magic method), False otherwise.
        """
        ...
    
    @cached_property
    @reader
    def is_magic(self) -> bool:
        """Determines if a method is a magic method.

        A magic method in Python is a method that starts and ends with double underscores, such as `__init__` or `__str__`.
        This property checks if the current method's name matches this pattern.

        Returns:
            bool: True if the method is a magic method (name starts and ends with double underscores), False otherwise.
        """
        ...
    
    @property
    @reader
    def is_overload(self) -> bool:
        """Determines whether a function is decorated with an overload decorator.

        Checks if the function has any of the following decorators:
        - @overload
        - @typing.overload
        - @typing_extensions.overload

        Returns:
            bool: True if function has an overload decorator, False otherwise.
        """
        ...
    
    @property
    @reader
    def is_property(self) -> bool:
        """Determines if the function is a property.

        Checks the decorators list to see if the function has a `@property` or `@cached_property` decorator.

        Returns:
            bool: True if the function has a `@property` or `@cached_property` decorator, False otherwise.
        """
        ...
    
    @property
    @reader
    def is_static_method(self) -> bool:
        """Determines if the function is a static method.

        Checks the function's decorators to determine if it is decorated with the @staticmethod decorator.

        Returns:
            bool: True if the function is decorated with @staticmethod, False otherwise.
        """
        ...
    
    @property
    @reader
    def is_class_method(self) -> bool:
        """Indicates whether the current function is decorated with @classmethod.

        Args:
            self: The PyFunction instance.

        Returns:
            bool: True if the function is decorated with @classmethod, False otherwise.
        """
        ...
    
    @noapidoc
    @reader
    def resolve_name(self, name: str, start_byte: int | None = ...) -> Symbol | Import | WildcardImport | None:
        ...
    
    @noapidoc
    @commiter
    def parse(self, G: CodebaseGraph) -> None:
        ...
    
    @property
    @reader
    def function_signature(self) -> str:
        """Returns the function signature as a string.

        Gets the string representation of the function's signature, including name, parameters, and return type.

        Args:
            None

        Returns:
            str: A string containing the complete function signature including the function name,
                parameters (if any), return type annotation (if present), and a colon.
        """
        ...
    
    @property
    @reader
    def body(self) -> str:
        """Returns the body of the function as a string.

        Gets the source code of the function's body, excluding the docstring if present.

        Returns:
            str: The function's body content as a string, with any docstring removed and whitespace stripped.
        """
        ...
    
    @writer
    def prepend_statements(self, lines: str) -> None:
        """Prepends statements to the start of the function body.

        Given a string of code statements, adds them at the beginning of the function body, right after any existing docstring. The method handles indentation automatically.

        Args:
            lines (str): The code statements to prepend to the function body.

        Returns:
            None: This method modifies the function in place.
        """
        ...
    
    @writer
    @override
    def set_return_type(self, new_return_type: str) -> None:
        """Sets or modifies the return type annotation of a function.

        Updates the function's return type annotation by either modifying an existing return type or adding a new one.
        If an empty string is provided as the new return type, removes the existing return type annotation.

        Args:
            new_return_type (str): The new return type annotation to set. Provide an empty string to remove the return type annotation.

        Returns:
            None
        """
        ...
    


