from .controller import (
    create_packages,
    create_title,
    create_new_commands,
    create_options,
)
from pylatex import Document
from dataclasses import dataclass
from pylatex.base_classes import Arguments
from .base import QuestionEnvironment, CJKEnvironment

GEOMETRY_OPTIONS = {
    "left": "1.91cm",
    "right": "1.91cm",
    "top": "2.54cm",
    "bottom": "2.54cm",
}


@dataclass
class MainTex(Document):
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
            geometry_options=GEOMETRY_OPTIONS,
        )

    def create_questions(self):
        with self.create(QuestionEnvironment()):
            content = create_options(self.test_id)
            self.append(content)

    def write(self):
        create_packages(self)
        create_new_commands(self)

        with self.create(CJKEnvironment(arguments=Arguments("UTF8", "bsmi"))) as env:
            create_title(self, self.title_name)
            self.create_questions()

        return self.generate_tex()
