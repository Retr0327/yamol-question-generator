from ..downloader import YamolDownloader
from dataclasses import dataclass


@dataclass
class YamolScraper:
    id: int

    def download_option_tags(self):
        return YamolDownloader(self.id).download()
