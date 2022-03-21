from ..base import LatexPackages
from pylatex.package import Package


def generate_latex_package(packages: list[tuple[str, str]]) -> map:
    """
    The generate_latex_package function generates a map object that
    maps packages to pylatex's Package() function.
    """

    return map(lambda item: Package(item[0], item[1]), packages)


def create_packages(self) -> None:
    """The create_packages adds a list of packages to the document."""

    package_info = LatexPackages.get_packages_info()
    package_list = list(generate_latex_package(package_info))
    for package in package_list:
        self.packages.append(package)
