from dataclasses import dataclass
from pylatex.position import Center
from .components import LatexPackages
from pylatex import Document, UnsafeCommand


@dataclass
class MainTxt(Document):
    """
    The MainTxt object contains a full Latex document.
    """

    test_id: int
    title_name: str

    def __post_init__(self) -> None:
        super().__init__(
            inputenc="utf8",
            documentclass="exam",
            document_options=["12pt", "a4paper"],
        )

    def fill_title(self) -> None:
        """The fill_title method adds a title within a box to the document."""

        with self.create(Center()):
            parbox_command = UnsafeCommand(
                "parbox",
                "3.5in",
                extra_arguments=[
                    r"\centering\vspace{5pt}\Large \textbf{"
                    + self.title_name
                    + r"}\vspace{5pt}"
                ],
            )

            fbox_command = UnsafeCommand("fbox", parbox_command)
            self.append(UnsafeCommand("fbox", fbox_command))
