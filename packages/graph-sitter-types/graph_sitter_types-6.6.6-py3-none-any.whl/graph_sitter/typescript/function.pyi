"""
This type stub file was generated by pyright.
"""

from functools import cached_property
from typing import TYPE_CHECKING
from tree_sitter import Node as TSNode
from codegen.utils.codemod.codemod_writer_decorators import noapidoc, ts_apidoc
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.autocommit import commiter, reader, writer
from graph_sitter.core.function import Function
from graph_sitter.core.import_resolution import Import, WildcardImport
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.symbol import Symbol
from graph_sitter.typescript.detached_symbols.decorator import TSDecorator
from graph_sitter.typescript.detached_symbols.parameter import TSParameter
from graph_sitter.typescript.enums import TSFunctionTypeNames
from graph_sitter.typescript.expressions.type import TSType
from graph_sitter.typescript.interfaces.has_block import TSHasBlock
from graph_sitter.typescript.symbol import TSSymbol
from graph_sitter.core.statements.export_statement import ExportStatement
from graph_sitter.core.statements.symbol_statement import SymbolStatement

if TYPE_CHECKING:
    ...
_VALID_TYPE_NAMES = ...
logger = ...
@ts_apidoc
class TSFunction(Function["TSFunction", TSDecorator, "TSCodeBlock", TSParameter, TSType], TSHasBlock, TSSymbol):
    """Representation of a Function in JavaScript/TypeScript"""
    @noapidoc
    @commiter
    def parse(self, G: CodebaseGraph) -> None:
        ...
    
    @property
    @reader
    def function_type(self) -> TSFunctionTypeNames:
        """Gets the type of function from its TreeSitter node.

        Extracts and returns the type of function (e.g., arrow function, generator function, function expression)
        from the node's type information.

        Args:
            None: Property method that uses instance's ts_node.

        Returns:
            TSFunctionTypeNames: The function type enum value representing the specific type of function.
        """
        ...
    
    @classmethod
    @noapidoc
    def from_function_type(cls, ts_node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: SymbolStatement | ExportStatement) -> TSFunction:
        """Creates a TSFunction object from a function declaration."""
        ...
    
    @property
    @reader
    def function_signature(self) -> str:
        """Returns a string representation of the function's signature.

        Generates a string containing the full function signature including name, parameters, and return type
        based on the function's type (arrow function, generator function, function expression, etc.).

        Returns:
            str: A string containing the complete function signature. For example: 'function foo(bar: string): number'

        Raises:
            NotImplementedError: If the function type is not implemented.
        """
        ...
    
    @cached_property
    @reader
    def is_private(self) -> bool:
        """Determines if a function is private based on its accessibility modifier.

        This property examines the function's accessibility modifier to determine if it's marked as private. In TypeScript, this means the function has the 'private' keyword.

        Returns:
            bool: True if the function has a 'private' accessibility modifier, False otherwise.
        """
        ...
    
    @cached_property
    @reader
    def is_magic(self) -> bool:
        """Returns whether this method is a magic method.

        A magic method is a method whose name starts and ends with double underscores, like __init__ or __str__.
        In this implementation, all methods are considered non-magic in TypeScript.

        Returns:
            bool: False, as TypeScript does not have magic methods.
        """
        ...
    
    @property
    @reader
    def is_anonymous(self) -> bool:
        """Property indicating whether a function is anonymous.

        Returns True if the function has no name or if its name is an empty string.

        Returns:
            bool: True if the function is anonymous, False otherwise.
        """
        ...
    
    @property
    def is_async(self) -> bool:
        """Determines if the function is asynchronous.

        Checks the function's node children to determine if the function is marked as asynchronous.

        Returns:
            bool: True if the function is asynchronous (has 'async' keyword), False otherwise.
        """
        ...
    
    @property
    @reader
    def is_arrow(self) -> bool:
        """Returns True iff the function is an arrow function.

        Identifies whether the current function is an arrow function (lambda function) in TypeScript/JavaScript.

        Returns:
            bool: True if the function is an arrow function, False otherwise.
        """
        ...
    
    @property
    @reader
    def is_property(self) -> bool:
        """Determines if the function is a property.

        Checks if any of the function's decorators are '@property' or '@cached_property'.

        Returns:
            bool: True if the function has a @property or @cached_property decorator, False otherwise.
        """
        ...
    
    @property
    @reader
    def is_jsx(self) -> bool:
        """Determines if the function is a React component by checking if it returns a JSX element.

        A function is considered a React component if it contains at least one JSX element in its body
        and either has no name or has a name that starts with an uppercase letter.

        Returns:
            bool: True if the function is a React component, False otherwise.
        """
        ...
    
    @writer
    def asyncify(self) -> None:
        """Modifies the function to be asynchronous, if it is not already.

        This method converts a synchronous function to be asynchronous by adding the 'async' keyword and wrapping
        the return type in a Promise if a return type exists.

        Returns:
            None

        Note:
            If the function is already asynchronous, this method does nothing.
        """
        ...
    
    @writer
    def arrow_to_named(self, name: str | None = ...) -> None:
        """Converts an arrow function to a named function in TypeScript/JavaScript.

        Transforms an arrow function into a named function declaration, preserving type parameters, parameters,
        return types, and function body. If the function is already asynchronous, the async modifier is preserved.

        Args:
            name (str | None): The name for the converted function. If None, uses the name of the variable
                the arrow function is assigned to.

        Returns:
            None

        Raises:
            ValueError: If name is None and the arrow function is not assigned to a named variable.
        """
        ...
    
    @noapidoc
    @reader
    def resolve_name(self, name: str, start_byte: int | None = ...) -> Symbol | Import | WildcardImport | None:
        ...
    
    @staticmethod
    def is_valid_node(node: TSNode) -> bool:
        """Determines if a given tree-sitter node corresponds to a valid function type.

        This method checks if a tree-sitter node's type matches one of the valid function types defined in the _VALID_TYPE_NAMES set.

        Args:
            node (TSNode): The tree-sitter node to validate.

        Returns:
            bool: True if the node's type is a valid function type, False otherwise.
        """
        ...
    
    @writer
    def convert_props_to_interface(self) -> None:
        """Converts React component props to TypeScript interfaces.

        For React components, converts inline props type definitions and PropTypes declarations
        to a separate interface. The interface will be named {ComponentName}Props and inserted
        before the component.

        Handles both simple types and complex types including:
        - Inline object type definitions
        - PropTypes declarations
        - Union types and optional props
        - Destructured parameters
        - Generic type parameters

        Example:
            ```typescript
            // Before
            function Button({ text, onClick }: { text: string, onClick: () => void }) {
                return <button onClick={onClick}>{text}</button>;
            }

            // After
            interface ButtonProps {
                text: string;
                onClick: () => void;
            }
            function Button({ text, onClick }: ButtonProps) {
                return <button onClick={onClick}>{text}</button>;
            }
            ```
        """
        ...
    


