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
