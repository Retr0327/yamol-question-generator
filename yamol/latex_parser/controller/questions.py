from pylatex.package import Package
from pylatex.base_classes import Environment


class Question(Environment):
    """A class to wrap LaTeX's question environment."""

    packages = [Package("question")]
    escape = False
    content_separator = "\n"
