"""
This type stub file was generated by pyright.
"""

from collections.abc import Callable
from dataclasses import dataclass
from typing import TypeVar

@dataclass
class DocumentedObject:
    name: str
    module: str
    object: any
    def __lt__(self, other) -> bool:
        ...
    
    def signature(self) -> str:
        ...
    


def canonical(codemod):
    """Decorator for canonical Codemods that will be used for AI-agent prompts."""
    ...

apidoc_objects: list[DocumentedObject] = ...
def apidoc(obj):
    """Decorator for objects that will be used as API documentation for AI-agent prompts."""
    ...

py_apidoc_objects: list[DocumentedObject] = ...
def py_apidoc(obj):
    """Decorator for objects that will be used as Python API documentation for AI-agent prompts."""
    ...

ts_apidoc_objects: list[DocumentedObject] = ...
def ts_apidoc(obj):
    """Decorator for objects that will be used as Typescript API documentation for AI-agent prompts."""
    ...

no_apidoc_objects: list[DocumentedObject] = ...
no_apidoc_signatures: set[str] = ...
T = TypeVar("T", bound=Callable)
def noapidoc(obj: T) -> T:
    """Decorator for things that are hidden from the API documentation for AI-agent prompts."""
    ...

def get_documented_object(obj) -> DocumentedObject | None:
    ...

