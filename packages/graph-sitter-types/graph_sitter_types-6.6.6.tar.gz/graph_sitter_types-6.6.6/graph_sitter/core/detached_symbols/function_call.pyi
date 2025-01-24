"""
This type stub file was generated by pyright.
"""

from typing import Generic, Self, TYPE_CHECKING, TypeVar, override
from tree_sitter import Node as TSNode
from codegen.utils.codemod.codemod_writer_decorators import apidoc, noapidoc
from graph_sitter.codebase.resolution_stack import ResolutionStack
from graph_sitter.core.autocommit import reader, remover, writer
from graph_sitter.core.detached_symbols.argument import Argument
from graph_sitter.core.detached_symbols.parameter import Parameter
from graph_sitter.core.expressions import Expression
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.interfaces.has_name import HasName
from graph_sitter.core.interfaces.importable import Importable
from graph_sitter.core.interfaces.resolvable import Resolvable
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.symbol_groups.collection import Collection
from graph_sitter.extensions.utils import cached_property
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.function import Function
from graph_sitter.core.interfaces.callable import Callable
from graph_visualization.enums import VizNode

if TYPE_CHECKING:
    ...
Parent = TypeVar("Parent", bound="Expression | None")
@apidoc
class FunctionCall(Expression[Parent], HasName, Resolvable, Generic[Parent]):
    """Abstract representation of a function invocation, e.g. in Python:
    ```
    def f():
        g() # FunctionCall
    ```
    """
    _arg_list: Collection[Argument, Self]
    def __init__(self, node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: Parent) -> None:
        ...
    
    @classmethod
    def from_usage(cls, node: Editable[Parent], parent: Parent | None = ...) -> Self | None:
        """Creates a FunctionCall object from an Editable instance that represents a function call.

        Takes an Editable node that potentially represents a function call and creates a FunctionCall object from it.
        Useful when working with search results from the Editable API that may contain function calls.

        Args:
            node (Editable[Parent]): The Editable node that potentially represents a function call.
            parent (Parent | None): The parent node for the new FunctionCall. If None, uses the parent from the input node.

        Returns:
            Self | None: A new FunctionCall object if the input node represents a function call, None otherwise.
        """
        ...
    
    @property
    @reader
    def parent_function(self) -> Function | None:
        """Retrieves the parent function of the current function call.

        Returns the Function object that contains this function call, useful for understanding the context in which a function call is made.

        Returns:
            Function | None: The parent Function object containing this function call, or None if not found or if the function call is not within a function.
        """
        ...
    
    @property
    @reader
    def is_awaited(self) -> bool:
        """Returns whether the function call is awaited with an 'await' keyword.

        Checks if this function call appears within an await expression by traversing up the parent nodes.

        Returns:
            bool: True if the function call is within an await expression, False otherwise.
        """
        ...
    
    @writer
    def asyncify(self) -> None:
        """Converts the function call to an async function call by wrapping it with 'await'.

        This method adds 'await' syntax to a function call if it is not already awaited. It wraps the function call in parentheses and prefixes it with 'await'.

        Args:
            None

        Returns:
            None
        """
        ...
    
    @property
    @reader
    def predecessor(self) -> FunctionCall[Parent] | None:
        """Returns the previous function call in a function call chain.

        Returns the previous function call in a function call chain. This method is useful for traversing function call chains
        to analyze or modify sequences of chained function calls.

        Returns:
            FunctionCall[Parent] | None: The previous function call in the chain, or None if there is no predecessor
            or if the predecessor is not a function call.
        """
        ...
    
    @property
    @noapidoc
    @override
    def viz(self) -> VizNode:
        ...
    
    @property
    @reader
    def source(self) -> str:
        """Gets the source code representation of this FunctionCall.

        Returns the textual representation of the function call. For chained function calls (e.g., a().b()),
        it returns only the current function call's source code by removing the predecessor's source.

        Args:
            None

        Returns:
            str: The source code representation of this function call. For chained calls, returns only the current
                function call's portion of the chain.
        """
        ...
    
    @property
    @reader
    def args(self) -> Collection[Argument, Self]:
        """Returns a list of arguments passed into the function invocation.

        The `args` property provides access to all arguments, both positional and keyword, that are passed to the function call.

        Args:
            None

        Returns:
            Collection[Argument, Self]: A collection containing the function's arguments.
        """
        ...
    
    def set_kwarg(self, name: str, value: str, *, create_on_missing: bool = ..., override_existing: bool = ...) -> None:
        """Set a keyword argument in a function call.

        Sets or modifies a keyword argument in the function call. Can create new arguments or modify existing ones based on configuration.

        Args:
            name (str): The name of the parameter/argument to set.
            value (str): The value to set the argument to.
            create_on_missing (bool, optional): If True, creates a new keyword argument if it doesn't exist. Defaults to True.
            override_existing (bool, optional): If True, modifies the value of existing argument. Defaults to True.

        Returns:
            None

        Raises:
            None
        """
        ...
    
    @noapidoc
    @reader
    def find_parameter_by_index(self, index: int) -> Parameter | None:
        ...
    
    @noapidoc
    @reader
    def find_parameter_by_name(self, name: str) -> Parameter | None:
        ...
    
    @reader
    def get_arg_by_parameter_name(self, param_name: str) -> Argument | None:
        """Returns an argument by its parameter name.

        Searches through the arguments of a function call to find an argument that matches
        a specified parameter name. This first checks for named arguments (kwargs) that match
        the parameter name directly, then checks for positional arguments by resolving their
        corresponding parameter names.

        Args:
            param_name (str): The name of the parameter to search for.

        Returns:
            Argument | None: The matching argument if found, None otherwise.
        """
        ...
    
    @reader
    def get_arg_by_index(self, arg_idx: int) -> Argument | None:
        """Returns the Argument with the given index from the function call's argument list.

        Args:
            arg_idx (int): The index of the argument to retrieve.

        Returns:
            Argument | None: The Argument object at the specified index, or None if the index is out of bounds.
        """
        ...
    
    @writer
    def convert_args_to_kwargs(self, exclude: int = ...) -> None:
        """Converts positional arguments in a function call to keyword arguments.

        This method converts positional arguments to keyword arguments, excluding any leading arguments specified by the exclude parameter.
        This is useful when refactoring function calls to be more explicit and self-documenting.

        Args:
            exclude (int): Number of leading positional arguments to exclude from conversion. Defaults to 0.

        Returns:
            None

        Note:
            - Skips conversion if the argument is already named
            - Skips arguments within the exclude range
            - Skips unpacked arguments (e.g. **kwargs)
            - Stops converting if it encounters a named argument that would conflict with an existing one
            - Requires the function definition to be resolvable and have parameters
        """
        ...
    
    @cached_property
    @reader
    @noapidoc
    def function_definition_frames(self) -> list[ResolutionStack[Callable]]:
        ...
    
    @cached_property
    @reader
    def function_definitions(self) -> list[Callable]:
        """Returns a list of callable objects that could potentially be the target of this function
        call.

        Finds and returns all possible functions that this call could be invoking based on name resolution.
        This is useful for analyzing parameter names, parameter types, and return types of the potential target functions.

        Returns:
            list[Callable]: A list of Callable objects representing the possible function definitions that this call could be invoking.
        """
        ...
    
    @property
    @reader
    def function_definition(self) -> Callable | None:
        """Returns the resolved function definition that is being called.

        This method returns the function definition associated with this function call.
        This is useful for accessing parameter names, parameter types, and return types of the called function.

        Returns:
            Callable | None: The resolved function definition, or None if no definition is found.
        """
        ...
    
    @remover
    def remove(self, delete_formatting: bool = ..., priority: int = ..., dedupe: bool = ...) -> None:
        """Removes a node and optionally its related extended nodes.

        This method removes a FunctionCall node from the codebase. If the node is part of an expression statement,
        it removes the entire expression statement. Otherwise, it performs a standard node removal.

        Args:
            delete_formatting (bool, optional): Whether to delete associated formatting nodes. Defaults to True.
            priority (int, optional): Priority level for the removal operation. Defaults to 0.
            dedupe (bool, optional): Whether to deduplicate identical removals. Defaults to True.

        Returns:
            None
        """
        ...
    
    @property
    @reader
    def function_calls(self) -> list[FunctionCall]:
        """Returns a list of all function calls contained within this function call.

        This method traverses through all arguments and the function name node to find any nested
        function calls. For example, if a function call has arguments that are themselves function
        calls, these will be included in the returned list.

        Returns:
            list[FunctionCall]: A list of FunctionCall instances contained within this function call,
                including the call itself. Sorted by their appearance in the code.
        """
        ...
    
    @property
    @noapidoc
    def descendant_symbols(self) -> list[Importable]:
        ...
    
    @noapidoc
    @writer
    def rename_if_matching(self, old: str, new: str): # -> None:
        ...
    
    @property
    @reader
    def call_chain(self) -> list[FunctionCall]:
        """Returns a list of all function calls in this function call chain, including this call. Does not include calls made after this one."""
        ...
    
    @property
    @reader
    def base(self) -> Editable | None:
        """Returns the base object of this function call chain."""
        ...
    


