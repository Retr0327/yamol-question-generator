from typing import Union
from pylatex import UnsafeCommand


class AnswerCommand:
    """
    The AnswerCommand object creates a list of Unsafecommands that are related to
    answers' format.
    """

    def create_answer_command(
        self, option_type: str, extra_args: Union[str, UnsafeCommand]
    ) -> UnsafeCommand:
        """The create_answer_command method creates the answer command based on `option_type`
           and `extra_args`.

        Args:
            option_type (str): the type of options (e.g. A, B, C and D)
            extra_args (str or UnsafeCommand): the extra argument

        Returns:
            a UnsafeCommand object
        """

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

    def create(self) -> UnsafeCommand:
        """The create method creates the new commands."""

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
