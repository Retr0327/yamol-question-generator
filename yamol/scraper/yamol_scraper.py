from typing import Union, List 
from dataclasses import dataclass
from ..downloader import YamolDownloader


@dataclass
class YamolScraper:
    """The YamolScraper extracts the option content from html tags downloaded by YamolDownloader"""

    id: int

    def download_option_tags(self) -> Union[str, List[str]]:
        """The download_option_tags method downloads the html tags."""
        return YamolDownloader(self.id).download()

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
