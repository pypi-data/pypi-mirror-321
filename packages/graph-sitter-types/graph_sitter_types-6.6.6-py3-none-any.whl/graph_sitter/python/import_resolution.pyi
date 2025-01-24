"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING
from tree_sitter import Node as TSNode
from codegen.utils.codemod.codemod_writer_decorators import noapidoc, py_apidoc
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.autocommit import reader
from graph_sitter.core.import_resolution import Import, ImportResolution
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.interfaces.exportable import Exportable
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.statements.import_statement import ImportStatement
from graph_sitter.enums import ImportType
from graph_sitter.python.file import PyFile

if TYPE_CHECKING:
    ...
logger = ...
@py_apidoc
class PyImport(Import["PyFile"]):
    """Extends Import for Python codebases."""
    @reader
    def is_module_import(self) -> bool:
        """Determines if the import is a module-level or wildcard import.

        Checks whether the import is either a module import (e.g. 'import foo') or a wildcard import (e.g. 'from foo import *').

        Returns:
            bool: True if the import is a module-level or wildcard import, False otherwise.
        """
        ...
    
    @property
    @reader
    def namespace(self) -> str | None:
        """Returns the namespace of the import if it imports a file, or None otherwise.

        This property determines the namespace for file imports. It returns None for wildcard imports. For file
        imports (where resolved_symbol is a FILE), it returns the alias source. For all other cases, it returns None.

        Returns:
            str | None: The namespace string for file imports, None for wildcard imports or non-file imports.
        """
        ...
    
    @property
    @reader
    def imported_exports(self) -> list[Exportable]:
        """Returns a list of exports from an import statement.

        Returns the enumerated list of symbols imported from a module import. If the import is
        not a module import, returns a list containing just the single imported symbol.
        For imports that don't resolve to any symbol, returns an empty list.

        Returns:
            list[Exportable]: A list of exported symbols. For module imports, contains all symbols
                and imports from the imported module. For non-module imports, contains a single imported
                symbol. For unresolved imports, returns empty list.
        """
        ...
    
    @noapidoc
    @reader
    def resolve_import(self, base_path: str | None = ...) -> ImportResolution[PyFile] | None:
        ...
    
    @classmethod
    @noapidoc
    def from_import_statement(cls, import_statement: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: ImportStatement) -> list[PyImport]:
        ...
    
    @classmethod
    @noapidoc
    def from_import_from_statement(cls, import_statement: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: ImportStatement) -> list[PyImport]:
        ...
    
    @classmethod
    @noapidoc
    def from_future_import_statement(cls, import_statement: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: ImportStatement) -> list[PyImport]:
        ...
    
    @property
    @reader
    def import_specifier(self) -> Editable:
        """Retrieves the import specifier node for this import.

        Finds and returns the import specifier node that matches either the alias or symbol name of this import.

        Args:
            None

        Returns:
            Editable: The import specifier node as a Name object if found, None otherwise.
        """
        ...
    
    @reader
    def get_import_string(self, alias: str | None = ..., module: str | None = ..., import_type: ImportType = ..., is_type_import: bool = ...) -> str:
        """Generates an import string for a Python import statement.

        Creates a formatted import statement string based on the provided parameters. The generated string can represent different types of imports including wildcard imports and aliased imports.

        Args:
            alias (str | None): Optional alias name for the imported symbol.
            module (str | None): Optional module name to import from. If not provided, uses the file's import module name.
            import_type (ImportType): Type of import to generate. Defaults to UNKNOWN.
            is_type_import (bool): Whether this is a type import. Defaults to False.

        Returns:
            str: A formatted import statement string.
        """
        ...
    


