from itertools import chain
from ..base import CommandCreater
from pylatex import UnsafeCommand


class OptionIndentationCommand(CommandCreater):
    """
    The OptionIndentationCommand object creates a list of Unsafecommands that are related to
    the options' indentation.
    """

    def create_option_indentation(self) -> list[UnsafeCommand]:
        """The create_option_indentation method creates options' indentation."""

        options = ["a", "b", "c", "d", ""]
        return list(
            map(lambda item: UnsafeCommand(fr"newlength\widthch{item}"), options)
        )

    def create_tab_width(self, value: dict) -> list[UnsafeCommand]:
        """The create_tab_width method creates new commands that set the new width of
           options' indentation.

        Args:
            value (dict): the value of tab_info in `self.create`.

        Returns:
            a list of UnsafeCommand objects
        """

        command_name = value["command_name"]
        width = value["width"]

        return [
            UnsafeCommand(fr"newlength\{command_name}"),
            UnsafeCommand(fr"setlength\{command_name}{{{width}\textwidth}}"),
        ]

    def create(self) -> list[UnsafeCommand]:
        """The create method creates the new commands."""

        tab_info = [
            {"command_name": "tabmaxwidth", "width": 0.96},
            {"command_name": "fourthtabwidth", "width": 0.25},
            {"command_name": "halftabwidth", "width": 0.5},
        ]

        option_indentation = self.create_option_indentation()
        tab_width = list(chain(*map(self.create_tab_width, tab_info)))

        return option_indentation + tab_width
