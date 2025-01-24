from enum import StrEnum

from rich.console import Console

console = Console()


class ProjectType(StrEnum):
    """Different types of projects."""

    BASIC = "basic"
    API = "api"
    API_AGENTS = "api-agents"
    AGENTS = "agents"
    DEEP_LEARNING = "dl"
    API_DEEP_LEARNING = "api-dl"
    ALL = "all"


__all__ = [
    "ProjectType",
    "console",
]
