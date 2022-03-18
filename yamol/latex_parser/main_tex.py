from dataclasses import dataclass
from pylatex import Document


@dataclass
class MainTxt(Document):
    """
    The MainTxt object contains a full Latex document.
    """

    test_id: int

    def __post_init__(self):
        super().__init__(
            inputenc="utf8",
            documentclass="exam",
            document_options=["12pt", "a4paper"],
        )
