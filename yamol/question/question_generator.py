import re
import pydantic
from typing import List, Union
from .scraper import YamolScraper
from dataclasses import dataclass


class YamolQuestionValidator(pydantic.BaseModel):
    """
    The JSLHRInfo object keeps track of an item in inventory, including question and option.
    """

    question: str
    option: str

    @pydantic.validator("question")
    @classmethod
    def is_question(cls, value: str) -> str:
        """The is_question method makes sure there is question value defined"""
        if not value:
            return "no question"

        return re.sub("[^為題組\n]\n", "", value)

    @pydantic.validator("option")
    @classmethod
    def is_option(cls, value: str) -> Union[str, List[str]]:
        """The is_option method makes sure there is option value defined"""
        if not value:
            return "題組題"

        return re.split("\(\w\)", value)[1:]


@dataclass
class YamolQuestionGenerator:
    """
    The YamolQuestionGenerator object generates a dictionary with `option` and `question` keys with
    corresponding values.
    """

    id: int

    def download_data(self) -> map:
        """The download_data method downloads the data from YamolScraper."""
        return YamolScraper(self.id).extract_data()

    def format_question(self, value: str) -> str:
        """The format_question formats the question value"""
        question_with_num = value.split("\n(A)")[0]
        return re.sub("^\d+\.", "", question_with_num)

    def create_option_form(self, data: str) -> str:
        """The create_option_form creates a dictionary with the given string data.

        Args:
            data (str): the data from `self.download_data`.

        Returns:
            a dict: {
                'question': '下列哪個選項屬於外在動機，且使用時對內在動機的負面影響可能會最小？',
                'option': [
                    '學生對工作很有興趣',
                    '使用學生非常喜愛的增強物',
                    '一開始就告知學生會得到什麼增強物',
                    '給予學生非物質性的獎賞，例如口頭讚賞'
                ]
            }
        """
        question = self.format_question(data)
        option_data = " ".join(re.findall("\(\w\).+", data))
        output = YamolQuestionValidator(question=question, option=option_data)
        return output.dict()

    def generate(self) -> map:
        """The generate method generates the dictionary with `option` and `question` keys with
           corresponding values.

        Returns:
            a map object
        """
        list_of_data = self.download_data()
        return map(self.create_option_form, list_of_data)
