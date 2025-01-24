"""
This type stub file was generated by pyright.
"""

import json
from rich.console import RenderResult
from tree_sitter import Node as TSNode, Point

def style_editable(ts_node: TSNode, filepath: str, file_node: TSNode) -> RenderResult:
    ...

def url_to_github(url: str, branch: str) -> str:
    ...

def stylize_error(path: str, start: tuple[int, int] | Point, end: tuple[int, int] | Point, file_node: TSNode, content: str, message: str): # -> None:
    ...

def safe_getattr(obj, attr, default=...): # -> Any | None:
    ...

class DeterministicJSONEncoder(json.JSONEncoder):
    def default(self, obj): # -> str | list[Any] | dict[Any, Any] | Any:
        ...
    


def deterministic_json_dumps(data, **kwargs): # -> str:
    ...

