from pylatex import UnsafeCommand


class NewOptionsCommands:
    """
    The NewOptionsCommands object creates a list of Unsafecommands that are related to
    options' format.
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
        """The create method creates the new commands."""

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
