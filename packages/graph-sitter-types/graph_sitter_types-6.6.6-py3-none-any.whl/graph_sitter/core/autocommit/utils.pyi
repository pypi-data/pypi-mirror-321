"""
This type stub file was generated by pyright.
"""

from typing import Any, TYPE_CHECKING, TypeGuard, Union
from graph_sitter.core.file import File
from graph_sitter.core.import_resolution import Import
from graph_sitter.core.symbol import Symbol

"""Utilities to prevent circular imports."""
if TYPE_CHECKING:
    ...
def is_file(node: Any) -> TypeGuard[File]:
    ...

def is_symbol(node: Any) -> TypeGuard[Symbol]:
    ...

def is_on_graph(node: Any) -> TypeGuard[Union[Import, Symbol]]:
    ...

