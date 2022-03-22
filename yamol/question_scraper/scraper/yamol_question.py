from typing import Union, List
from dataclasses import dataclass
from .soup_downloader import YamolDownloader


@dataclass
class YamolQuestionScraper:
    """The YamolScraper extracts the option content from html tags downloaded by YamolDownloader"""

    test_id: int

    def __post_init__(self) -> None:
        self.soup = YamolDownloader(self.test_id).download()

    def download_option_tags(self) -> Union[str, List[str]]:
        """The download_option_tags method downloads the html tags."""
        question_tag = self.soup.find_all("div", class_="col-lg-12 reponse-card")
        has_content = len(question_tag)

        if not has_content:
            return "no content"

        return question_tag

    def clean_data(self, tag) -> str:
        """The clean_data method cleans the html tags from the argument `tag`.

        Args:
            tag (BeautifulSoup): the BeautifulSoup object with option info.

         Returns:
            a str
        """
        return tag.find("span", class_="itemcontent").text

    def extract_data(self):
        option_tags = self.download_option_tags()
        return map(self.clean_data, option_tags)
