"""
This type stub file was generated by pyright.
"""

from pydantic import BaseModel

logger = ...
class BaseRepoConfig(BaseModel):
    """Base version of RepoConfig that does not depend on the db."""
    name: str = ...
    respect_gitignore: bool = ...


