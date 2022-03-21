from ..base import CommandCreater
from pylatex import UnsafeCommand


class ChoicCommand(CommandCreater):

    option_width = r"\ifdim\widthch<\widthchb\relax\setlength{\widthch}{\widthchb}\fi"

    def set_to_width(self, option_type: str):
        option_type = option_type.upper()
        option_type_factory = {"A": 1, "B": 2, "C": 3, "D": 4}

        return fr"\settowidth\widthchb{{{option_type}M.#{option_type_factory[option_type]}}}"

    def set_each_option(self, number: str):
        return fr"{number}{{#1}}{{#2}}{{#3}}{{#4}}{{#5}}"

    def create(self):
        extra_arguments = fr"""
        {self.set_to_width('a')}

        \setlength{{\widthch}}{{\widthcha}} 

        {self.set_to_width('b')}

        {self.option_width}
        
        {self.set_to_width('c')}

        {self.option_width}

        {self.set_to_width('d')}

        {self.option_width}

        \ifdim\widthch>\halftabwidth
            {self.set_each_option('onech')}
        \else\ifdim\widthch<\halftabwidth
            {self.set_each_option('twoch')}
        \ifdim\widthch>\fourthtabwidth
            {self.set_each_option('fourch')}
        \else

        \fi\fi\fi        
        """

        return UnsafeCommand(
            "newcommand", r"\choice", options=5, extra_arguments=extra_arguments
        )
