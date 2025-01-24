"""
This type stub file was generated by pyright.
"""

from abc import abstractmethod
from typing import Generic, Self, TYPE_CHECKING, TypeVar
from tree_sitter import Node as TSNode
from codegen.utils.codemod.codemod_writer_decorators import apidoc, noapidoc
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.interfaces.exportable import Exportable
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.symbol_groups.collection import Collection
from graph_sitter.extensions.autocommit import commiter
from graph_sitter.core.statements.export_statement import ExportStatement

if TYPE_CHECKING:
    ...
Parent = TypeVar("Parent", bound="Collection[Export, ExportStatement]")
@apidoc
class Export(Exportable[Parent], Generic[Parent]):
    """Represents a single symbol being exported."""
    export_statement: ExportStatement
    def __init__(self, ts_node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: Parent) -> None:
        ...
    
    @noapidoc
    @abstractmethod
    def parse(self, G: CodebaseGraph) -> None:
        """Add self to the graph and SYMBOL_USAGE edges from export to exported symbol."""
        ...
    
    @property
    @abstractmethod
    def exported_symbol(self) -> Exportable | None:
        """Returns the symbol, file, or import being exported from this export object.

        Returns:
            Exportable | None: The exported symbol, file, or import, or None if it cannot be resolved.
        """
        ...
    
    @property
    @abstractmethod
    def resolved_symbol(self) -> Exportable | None:
        """Returns the resolved symbol for an export.

        Gets the final symbol, file, or external module that this export resolves to by following through indirect imports and exports.

        Returns:
            Exportable | None: The final resolved symbol, which can be a Symbol, File, or External module. Returns None if the symbol cannot be resolved.
        """
        ...
    
    @abstractmethod
    def is_named_export(self) -> bool:
        """Determines if the export is named or default.

        Returns:
            bool: True if the export is named, False if it is default.
        """
        ...
    
    @abstractmethod
    def is_module_export(self) -> bool:
        """Determines if the export is a module-level export.

        This method checks if the export statement represents a module-level export,
        such as wildcard exports or default object exports.

        Returns:
            bool: True if the export is a module-level export, False otherwise.
        """
        ...
    
    def is_aliased(self) -> bool:
        """Determines if the Export object is aliased.

        Checks if the exported symbol has a different name than the name it is exported as.

        Returns:
            bool: True if the exported symbol has a different name than the name it is exported as, False otherwise.
        """
        ...
    
    @noapidoc
    @commiter
    def compute_export_dependencies(self) -> None:
        ...
    
    @property
    @noapidoc
    def parent_symbol(self) -> Self:
        """Returns the parent symbol of the symbol."""
        ...
    


