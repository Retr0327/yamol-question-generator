import requests
from bs4 import BeautifulSoup


class YamolDownloader:
    """The YamolDownloader object downloads the option tags from the Yamol based on a given id"""

    def __init__(self, test_id: int) -> None:
        self.url = f"https://yamol.tw/exam.php?id={test_id}"

    def download(self) -> BeautifulSoup:
        res = requests.get(self.url)
        return BeautifulSoup(res.text, "lxml")
