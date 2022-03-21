from pylatex import UnsafeCommand
from pylatex.position import Center


def create_title(self, title_name: str) -> None:
    """The create_title method adds a title within a box to the document."""

    with self.create(Center()):
        parbox_command = UnsafeCommand(
            "parbox",
            "3.5in",
            extra_arguments=fr"\centering\vspace{{5pt}}\Large \textbf{{{title_name}}}\vspace{{5pt}}",
        )

        fbox_command = UnsafeCommand("fbox", parbox_command)
        self.append(UnsafeCommand("fbox", fbox_command))
