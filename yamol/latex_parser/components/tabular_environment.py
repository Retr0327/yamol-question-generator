from pylatex.package import Package
from pylatex.base_classes import Environment


class Tabular(Environment):
    """A class to wrap LaTeX's tabular environment."""

    packages = [Package("tabular")]
    escape = False
    content_separator = "\n"
