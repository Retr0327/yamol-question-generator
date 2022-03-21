from ..service import (
    AnswerCommand,
    show_all_answers,
    ChoicCommand,
    NewOptionsCommands,
    OptionIndentationCommand,
)


def create_new_commands(self):
    options = []
    options = options + show_all_answers()
    return self.preamble.extend(options)
