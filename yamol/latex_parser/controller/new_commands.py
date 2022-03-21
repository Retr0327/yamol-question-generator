from ..service import (
    AnswerCommand,
    show_all_answers,
    ChoicCommand,
    NewOptionsCommands,
    OptionIndentationCommand,
)


def create_new_commands(self):
    choice_command = ChoicCommand().create()
    options = [choice_command]
    options = show_all_answers() + options
    return self.preamble.extend(options)
