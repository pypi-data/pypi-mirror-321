"""
This type stub file was generated by pyright.
"""

from typing import Generic, TYPE_CHECKING, TypeVar
from codegen.utils.codemod.codemod_writer_decorators import apidoc
from graph_sitter._proxy import proxy_property
from graph_sitter.core.autocommit import reader
from graph_sitter.core.dataclasses.usage import Usage, UsageType
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.interfaces.importable import Importable
from graph_sitter.core.export import Export
from graph_sitter.core.import_resolution import Import
from graph_sitter.core.symbol import Symbol

if TYPE_CHECKING:
    ...
Parent = TypeVar("Parent", bound="Editable")
@apidoc
class Usable(Importable[Parent], Generic[Parent]):
    """An interface for any node object that can be referenced by another node."""
    @proxy_property
    @reader(cache=False)
    def symbol_usages(self, usage_types: UsageType | None = ...) -> list[Import | Symbol | Export]:
        """Returns a list of symbols that use or import the exportable object.

        Args:
            usage_types (UsageType | None): The types of usages to search for. Defaults to any.

        Returns:
            list[Import | Symbol | Export]: A list of symbols that use or import the exportable object.

        Note:
            This method can be called as both a property or a method. If used as a property, it is equivalent to invoking it without arguments.
        """
        ...
    
    @proxy_property
    @reader(cache=False)
    def usages(self, usage_types: UsageType | None = ...) -> list[Usage]:
        """Returns a list of usages of the exportable object.

        Retrieves all locations where the exportable object is used in the codebase. By default, returns all usages, such as imports or references within the same file.

        Args:
            usage_types (UsageType | None): Specifies which types of usages to include in the results. Default is any usages.

        Returns:
            list[Usage]: A sorted list of Usage objects representing where this exportable is used, ordered by source location in reverse.

        Raises:
            ValueError: If no usage types are specified or if only ALIASED and DIRECT types are specified together.

        Note:
            This method can be called as both a property or a method. If used as a property, it is equivalent to invoking it without arguments.
        """
        ...
    
    def rename(self, new_name: str, priority: int = ...): # -> None:
        """Renames a symbol and updates all its references in the codebase.

        Args:
            new_name (str): The new name for the symbol.
            priority (int): Priority of the edit operation. Defaults to 0.

        Returns:
            tuple[NodeId, NodeId]: A tuple containing the file node ID and the new node ID of the renamed symbol.
        """
        ...
    


