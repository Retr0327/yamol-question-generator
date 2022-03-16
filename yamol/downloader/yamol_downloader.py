import requests
from bs4 import BeautifulSoup
from typing import Union, List


class YamolDownloader:
    "The YamolDownloader object downloads the option tags from the Yamol based on a given id"

    def __init__(self, id: int) -> None:
        self.id = id

    @property
    def url(self) -> str:
        return f"https://yamol.tw/exam.php?id={self.id}"

    def download(self) -> Union[str, List[str]]:
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, "lxml")
        question_tag = soup.find_all("div", class_="col-lg-12 reponse-card")
        has_content = len(question_tag)

        if not has_content:
            return "no content"

        return question_tag
