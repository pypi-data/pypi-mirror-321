"""
This type stub file was generated by pyright.
"""

from typing import Generic, TypeVar
from codegen.utils.codemod.codemod_writer_decorators import ts_apidoc
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.placeholder.placeholder import Placeholder

Parent = TypeVar("Parent", bound="Editable")
@ts_apidoc
class TSReturnTypePlaceholder(Placeholder[Parent], Generic[Parent]):
    """A placeholder class for function return type annotations in TypeScript.

    This class represents a placeholder for function return type annotations, allowing for modification
    and addition of return type annotations after the parameter list. It provides functionality to
    add or modify return type annotations with proper formatting.
    """
    def edit(self, new_src: str, fix_indentation: bool = ..., priority: int = ..., dedupe: bool = ...) -> None:
        """Modifies the return type annotation of a function.

        Adds or modifies the return type annotation of a function after its parameter list.

        Args:
            new_src (str): The return type annotation to add. If it doesn't start with ':', a ':' will be prepended.
            fix_indentation (bool, optional): Whether to fix the indentation of the added code. Defaults to False.
            priority (int, optional): The priority of this edit. Defaults to 0.
            dedupe (bool, optional): Whether to remove duplicate edits. Defaults to True.

        Returns:
            None

        Note:
            If new_src is empty or None, the method returns without making any changes.
        """
        ...
    


