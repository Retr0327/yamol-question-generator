from pylatex import Document
from dataclasses import dataclass
from .components import LatexPackages


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

        with self.create(Title()):
            content = (
                "\\fbox{\\fbox{\\parbox{3.5in}{\\centering\n"
                "\\vspace{5pt}\\Large\n"
                "\\textbf{"
                + f"{self.title_name}"
                + "}\\vspace"
                + "{5pt}}}}\\vspace\{10pt}"
            )

            self.append(content)
