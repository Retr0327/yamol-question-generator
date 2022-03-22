from itertools import chain
from ..service import (
    AnswerCommand,
    show_all_answers,
    ChoicCommand,
    NewOptionsCommands,
    OptionIndentationCommand,
)
from pylatex import UnsafeCommand


def create_new_commands(self) -> list[UnsafeCommand]:
    """The create_new_commands creates a list of LaTex commands"""

    all_answer = show_all_answers()
    answer = AnswerCommand().create()
    new_options = NewOptionsCommands().create()
    option_indentation = OptionIndentationCommand().create()
    choice = ChoicCommand().create()

    options = [all_answer, [answer], new_options, option_indentation, [choice]]

    return self.preamble.extend(list(chain(*options)))
