from typing import Union
from enum import Enum, auto
from abc import ABC, abstractmethod
from pylatex import UnsafeCommand
from pylatex.package import Package
from pylatex.base_classes import Environment


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


class Question(Environment):
    """The Question object wraps LaTex's question environment."""

    packages = [Package("question")]
    escape = False
    content_separator = "\n"


class CJK(Environment):
    """The CJK object wraps LaTex's CJK environment."""

    packages = [Package("question", option=["UTF8", "bsmi"])]
    escape = False
    content_separator = "\n"
