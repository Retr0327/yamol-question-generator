from typing import Union
from enum import Enum, auto
from pylatex import UnsafeCommand
from abc import ABC, abstractmethod


class LatexPackages(Enum):
    """Enumeration members refer to Latex packages."""

    Indentfirst = auto()
    Graphicx = auto()
    Mathptm = auto()
    CJK = "encapsulated"
    Babel = "english"
    Ifthen = auto()

    @classmethod
    def get_packages_info(cls) -> list[tuple[str, str]]:
        """The get_packages_info method returns a list of tuples. Each tuple consist a key and value pair.

        Returns:
            a list: [
                (Indentfirst, None),
                ...,
                (CJK, ;encapsulated),
                ...
            ]
        """
        values = map(
            lambda item: item.value if isinstance(item.value, str) else None, cls
        )
        keys = map(lambda item: item.name.lower() if item.name != "CJK" else "CJK", cls)
        return list(zip(keys, values))


class CommandCreater(ABC):
    """
    The CommandCreater objects creates custom latex commands.
    """

    @abstractmethod
    def create(self) -> Union[list[UnsafeCommand], UnsafeCommand]:
        """The create method creates the commands."""
        pass
