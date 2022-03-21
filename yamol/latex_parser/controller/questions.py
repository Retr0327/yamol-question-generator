from pylatex.package import Package
from pylatex.base_classes import Environment
from ...question import YamolQuestionGenerator


class Question(Environment):
    """A class to wrap LaTeX's question environment."""

    packages = [Package("question")]
    escape = False
    content_separator = "\n"
