import json
import pathlib as plib
from quranreader.interface import QuranData
from quranreader.service import Services


class QuranServices:
    def __init__(self, path_database: str) -> None:
        self.path_database = path_database
        self.__services = Services()
        self.__response = self._request_quran_json()
        self.__save()

    def _request_quran_json(self) -> dict:
        return self.__services.quran_to_json()

    def __save(self) -> None:
        with open(plib.Path(self.path_database).joinpath("quran.json"), "w", encoding="utf-8") as file:
            file.write(json.dumps(self.__response, indent=4))
        return None

    @property
    def resp(self) -> QuranData:
        return self.__response
