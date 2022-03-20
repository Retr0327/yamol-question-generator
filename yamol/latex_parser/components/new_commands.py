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

    def create_commands(self, arg: str, extra_args: list) -> UnsafeCommand:
        """The create_commands method creates an unsafecommand.

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
        one_line_options = self.create_commands(
            r"\fourch",
            [
                r"\par"
                r"\begin{tabular}{*{4}{@{}p{0.23\textwidth}}}"
                r"(A)~#1 & (B)~#2 & (C)~#3 & (D)~#4"
                r"\end{tabular}"
                r"\getanswer{#1}{#2}{#3}{#4}{#5}"
            ],
        )

        two_lines_options = self.create_commands(
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

        four_lines_options = self.create_commands(
            r"\onech",
            [
                r"\par"
                r"(A)~#1 & (B)~#2 & (C)~#3 & (D)~#4"
                r"\getanswer{#1}{#2}{#3}{#4}{#5}"
            ],
        )

        return [one_line_options, two_lines_options, four_lines_options]
