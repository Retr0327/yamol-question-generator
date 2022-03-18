from pylatex.package import Package
from pylatex.base_classes import Environment


class Title(Environment):
    """
    The Title object wraps LaTeX's center environment and creates a title.
    """

    packages = [Package("center")]
    escape = False
    content_separator = "\n"
