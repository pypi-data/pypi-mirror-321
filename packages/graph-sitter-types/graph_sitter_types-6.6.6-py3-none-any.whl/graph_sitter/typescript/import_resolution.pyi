"""
This type stub file was generated by pyright.
"""

from collections.abc import Generator
from typing import Self, TYPE_CHECKING, override
from tree_sitter import Node as TSNode
from codegen.utils.codemod.codemod_writer_decorators import noapidoc, ts_apidoc
from graph_sitter.codebase.codebase_graph import CodebaseGraph
from graph_sitter.core.autocommit import reader
from graph_sitter.core.external_module import ExternalModule
from graph_sitter.core.import_resolution import Import, ImportResolution, WildcardImport
from graph_sitter.core.interfaces.editable import Editable
from graph_sitter.core.interfaces.exportable import Exportable
from graph_sitter.core.node_id_factory import NodeId
from graph_sitter.core.statements.import_statement import ImportStatement
from graph_sitter.core.symbol import Symbol
from graph_sitter.enums import ImportType
from graph_sitter.typescript.file import TSFile
from graph_sitter.typescript.statements.import_statement import TSImportStatement

if TYPE_CHECKING:
    ...
@ts_apidoc
class TSImport(Import["TSFile"], Exportable):
    """Extends Import for TypeScript codebases."""
    @reader
    def is_type_import(self) -> bool:
        """Checks if an import is a type import.

        Determines whether an import statement is specifically for types. This includes explicit type imports
        (e.g., 'import type foo from bar'), exports of types, and dynamic imports followed by property access.

        Returns:
            bool: True if the import is a type import, False otherwise.
        """
        ...
    
    @reader
    def is_module_import(self) -> bool:
        """Determines if an import represents a module-level import.

        Module imports represent imports of an entire file rather than specific symbols from a file.
        These imports must traverse through the file to resolve the actual symbol(s) being imported.

        Args:
            self (TSImport): The import object to check.

        Returns:
            bool: True if the import is a module-level import, False otherwise.
                Returns True for:
                - Imports of type MODULE, WILDCARD, or DEFAULT_EXPORT
                - Side effect imports that are not type imports
        """
        ...
    
    @reader
    def is_default_import(self) -> bool:
        """Determines whether the import is a default export import.

        Checks if the import is importing a default export from a module. The default export
        may be a single symbol or an entire module.

        Args:
            self (TSImport): The import instance.

        Returns:
            bool: True if the import is a default export import, False otherwise.
        """
        ...
    
    @property
    @reader
    def namespace(self) -> str | None:
        """If import is a module import, returns any namespace prefix that must be used with import reference.

        Returns the namespace prefix for import reference when the import is a module import, specifically when
        the import resolves to a file node_type. The namespace is determined by the alias if set, otherwise None.

        Returns:
            str | None: The alias name if the import resolves to a file node_type and has an alias,
                None otherwise.
        """
        ...
    
    @property
    @reader
    def imported_exports(self) -> list[Exportable]:
        """Returns the enumerated list of exports imported from a module import.

        Returns a list of exports that this import statement references. The exports can be direct exports
        or re-exports from other modules.

        Returns:
            list[Exportable]: List of exported symbols. Empty list if this import doesn't reference any exports
            or if imported_symbol is None.
        """
        ...
    
    @property
    @reader
    def resolved_symbol(self) -> Symbol | ExternalModule | TSFile | None:
        """Returns the resolved symbol that the import is referencing.

        Follows the imported symbol and returns the final symbol it resolves to. For default imports, resolves to the exported symbol.
        For module imports with matching symbol names, resolves through module imports to find the matching symbol.
        For indirect imports, follows the import chain to find the ultimate symbol.

        Returns:
            Union[Symbol, ExternalModule, TSFile, None]: The resolved symbol. Returns None if the import cannot be resolved,
            Symbol for resolved import symbols, ExternalModule for external module imports,
            or TSFile for module/file imports.
        """
        ...
    
    @reader
    def resolve_import(self, base_path: str | None = ...) -> ImportResolution[TSFile] | None:
        """Resolves an import statement to its target file and symbol.

        This method is used by GraphBuilder to resolve import statements to their target files and symbols. It handles both relative and absolute imports,
        and supports various import types including named imports, default imports, and module imports.

        Args:
            base_path (str | None): The base path to resolve imports from. If None, uses the codebase's base path
                or the tsconfig base URL.

        Returns:
            ImportResolution[TSFile] | None: An ImportResolution object containing the resolved file and symbol,
                or None if the import could not be resolved (treated as an external module).
                The ImportResolution contains:
                - from_file: The file being imported from
                - symbol: The specific symbol being imported (None for module imports)
                - imports_file: True if importing the entire file/module
        """
        ...
    
    @classmethod
    @noapidoc
    def from_export_statement(cls, source_node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: TSImportStatement) -> list[TSImport]:
        """Constructs import objects defined from an export statement"""
        ...
    
    @classmethod
    @noapidoc
    def from_import_statement(cls, import_statement_node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: TSImportStatement) -> list[TSImport]:
        ...
    
    @classmethod
    @noapidoc
    def from_dynamic_import_statement(cls, import_call_node: TSNode, module_node: TSNode, file_node_id: NodeId, G: CodebaseGraph, parent: ImportStatement) -> list[TSImport]:
        """Parses a dynamic import statement, given a reference to the `import`/`require` node and `module` node.
        e.g.
        const myModule = await import('./someFile')`;
        const { exportedFunction, exportedVariable: aliasedVariable } = await import('./someFile');
        import('./someFile');

        const myModule = require('./someFile')`;
        const { exportedFunction, exportedVariable: aliasedVariable } = require('./someFile');
        require('./someFile');
        Note: imports using `require` will import whatever is defined in `module.exports = ...` or `export = ...`
        """
        ...
    
    @property
    @reader
    def import_specifier(self) -> Editable:
        """Retrieves the import specifier node for this import.

        Finds and returns the import specifier node containing this import's name and optional alias.
        For named imports, this is the import_specifier or export_specifier node.
        For other imports, this is the identifier node containing the import name.

        Returns:
            Editable: The import specifier node containing this import's name and alias.
                For named imports, returns the import_specifier/export_specifier node.
                For other imports, returns the identifier node containing the import name.
                Returns None if no matching specifier is found.
        """
        ...
    
    @reader
    def get_import_string(self, alias: str | None = ..., module: str | None = ..., import_type: ImportType = ..., is_type_import: bool = ...) -> str:
        """Generates an import string for an import statement.

        Generates a string representation of an import statement with optional type and alias information.

        Args:
            alias (str | None): Alias name for the imported symbol. Defaults to None.
            module (str | None): Module name to import from. Defaults to None. If not provided, uses the file's import module name.
            import_type (ImportType): Type of import (e.g. WILDCARD, NAMED_EXPORT). Defaults to ImportType.UNKNOWN.
            is_type_import (bool): Whether this is a type import. Defaults to False.

        Returns:
            str: A string representation of the import statement.
        """
        ...
    
    @property
    @noapidoc
    @override
    def names(self) -> Generator[tuple[str, Self | WildcardImport[Self]], None, None]:
        ...
    


