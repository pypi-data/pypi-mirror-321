import pathlib as plib
class Config:
    @staticmethod
    def url_data_quran() -> str:
        return "https://raw.githubusercontent.com/mehdi-stark/Coran-Quran/refs/heads/master/quran.json"

    @staticmethod
    def author_quran_github() -> str:
        return "https://github.com/mehdi-stark"

class PathConfig:
    cwd = plib.Path(__file__).parent
