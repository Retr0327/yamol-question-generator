from typing import Union
from itertools import chain
from pylatex import UnsafeCommand


def show_all_answers() -> list[UnsafeCommand]:
    """The show_all_answers function generates the newcommands of `\showallanswers`"""

    new_box = UnsafeCommand(r"newbox\allanswers")
    set_box = UnsafeCommand(r"setbox\allanswers=\vbox{}")
    new_environment = UnsafeCommand(
        "newenvironment",
        r"\showallanswers",
        extra_arguments=[
            r"\global\setbox\allanswers=\vbox\bgroup\unvbox\allanswers",
            r" \bigbreak\egroup",
        ],
    )
    new_command = UnsafeCommand(
        "newcommand", r"\showallanswers", extra_arguments=[r"\par\unvbox\allanswers"]
    )

    return [new_box, set_box, new_environment, new_command]


class OptionsNewCommands:
    """
    The OptionsNewCommands object creates a list of Unsafecommands that are related to
    setting options' format.
    """

    def create_options_command(self, arg: str, extra_args: list) -> UnsafeCommand:
        """The create_options_command method creates an unsafecommand.

        Args:
            arg (str): the argument of an UnsafeCommand.
            extra_args (list): a list of extra arguments of an UnsafeCommand.

        Returns:
            an UnsafeCommand object
        """

        return UnsafeCommand(
            command="newcommand", arguments=arg, options=5, extra_arguments=extra_args
        )

    def create(self) -> list[UnsafeCommand]:
        one_line_options = self.create_options_command(
            r"\fourch",
            [
                r"\par"
                r"\begin{tabular}{*{4}{@{}p{0.23\textwidth}}}"
                r"(A)~#1 & (B)~#2 & (C)~#3 & (D)~#4"
                r"\end{tabular}"
                r"\getanswer{#1}{#2}{#3}{#4}{#5}"
            ],
        )

        two_lines_options = self.create_options_command(
            r"\twoch",
            [
                r"\par"
                r"\begin{tabular}{*{2}{@{}p{0.46\textwidth}}}"
                r"(A)~#1 & (B)~#2"
                r"\end{tabular}"
                r"\par"
                r"\begin{tabular}{*{2}{@{}p{0.46\textwidth}}}"
                r"(C)~#3 & (D)~#4"
                r"\end{tabular}"
                r"\getanswer{#1}{#2}{#3}{#4}{#5}"
            ],
        )

        four_lines_options = self.create_options_command(
            r"\onech",
            [
                r"\par"
                r"(A)~#1 & (B)~#2 & (C)~#3 & (D)~#4"
                r"\getanswer{#1}{#2}{#3}{#4}{#5}"
            ],
        )

        return [one_line_options, two_lines_options, four_lines_options]


class AnswerCommand:
    def create_answer_command(
        self, option_type: str, extra_args: Union[str, UnsafeCommand]
    ):
        option_type = option_type.upper()
        equal = fr"\equal{{#5}}{{{option_type}}}"
        option_type_factory = {"A": 1, "B": 2, "C": 3, "D": 4}

        return UnsafeCommand(
            "ifthenelse",
            equal,
            extra_arguments=[
                fr"\begin{{answer}}\thequestion. ({option_type})~#{option_type_factory[option_type]}\end{{answer}}",
                extra_args,
            ],
        )

    def create(self):
        option_d = self.create_answer_command(
            "d",
            r"\begin{answer}\textbf{\thequestion. (#5)~Invalid answer choice.}\end{answer}",
        )

        option_c = self.create_answer_command("c", option_d)
        option_b = self.create_answer_command("b", option_c)
        option_a = self.create_answer_command("a", option_b)
        return UnsafeCommand(
            "newcommand*", r"\getanswer", options=5, extra_arguments=[option_a]
        )


class OptionIndentationCommand:
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
        """The create_tab_width method creates new commands that set the new width of options' indentation"""

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
