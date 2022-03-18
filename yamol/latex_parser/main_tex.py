from pylatex import Document
from .components import Title
from dataclasses import dataclass


@dataclass
class MainTxt(Document):
    """
    The MainTxt object contains a full Latex document.
    """

    test_id: int
    title_name: str

    def __post_init__(self):
        super().__init__(
            inputenc="utf8",
            documentclass="exam",
            document_options=["12pt", "a4paper"],
        )

    def fill_title(self):
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
