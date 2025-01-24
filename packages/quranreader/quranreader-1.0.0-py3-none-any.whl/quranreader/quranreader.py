import re
import json
import pathlib as plib
from quranreader.interface import (
    QuranData,
    QuranSurahsData,
    QuranVersetData,
    RevelationType,
    TypeFilterSearch,
    TypeFilterVerset,
)
from typing import Optional, Dict, List, Literal, Union, overload
from quranreader.handle_exception import ByError, SurahNotFound, FormatValueGet
from quranreader.parser_quranreader import QuranServices
from quranreader.utils import check_number_verset, _extract_verset


class QuranReader:
    """
    Classe permettant de lire et d'interroger les données du Coran depuis un fichier JSON.

    Attributes:
        path_database (str): Le chemin vers le dossier contenant les données du Coran.
        path_quran (Path): Le chemin complet vers le fichier quran.json.
    """

    def __init__(self) -> None:
        """
        Initialise le lecteur du Coran avec le chemin vers la base de données.

        Args:
            path_database (str): Chemin vers le dossier de la base de données.
        """
        path_database = plib.Path(__file__).parent.joinpath(".database")
        path_database.mkdir(exist_ok=True, parents=True)
        self.path_database = path_database
        self.path_quran = plib.Path(path_database).joinpath("quran.json")

        if not self.path_quran.exists():
            quran_services = QuranServices(path_database)
            self.__quran = quran_services.resp
        else:
            self.__quran = self.__read_init()

        self.__surahs_by_number: Optional[Dict[int, QuranSurahsData]] = None
        self.__surahs_by_name_fr: Optional[Dict[str, QuranSurahsData]] = None
        self.__surahs_by_name_arabic: Optional[Dict[str, QuranSurahsData]] = None
        self.__surahs_by_name_phonetic: Optional[Dict[str, QuranSurahsData]] = None
        self.__lower_surahs_by_name_fr: Optional[Dict[str, QuranSurahsData]] = None
        self.__lower_surahs_by_name_phonetic: Optional[Dict[str, QuranSurahsData]] = (
            None
        )

    @staticmethod
    def revelation_type_enum() -> RevelationType:
        """
        Retourne l'énumération des types de révélation (Medinois ou Mecquoise).

        Returns:
            RevelationType: L'énumération des types de révélation.
        """
        return RevelationType

    def __read_init(self) -> QuranData:
        """
        Lit le fichier quran.json et initialise les données du Coran.

        Returns:
            QuranData: Les données du Coran sous forme de dictionnaire.

        Raises:
            Exception: En cas d'erreur lors de la lecture du fichier quran.json.
        """
        try:
            with open(self.path_quran, "r") as file:
                buffer = file.read()
                parser_json = json.loads(buffer)
                return parser_json
        except Exception as e:
            raise Exception(f"Error reading file quran.json {str(e)}")

    @property
    def quran(self) -> QuranData:
        """
        Retourne les données complètes du Coran.

        Returns:
            QuranData: Les données du Coran.
        """
        return self.__quran

    @property
    def surahs_by_name_phonetic(self) -> Dict[str, QuranSurahsData]:
        """
        Retourne un dictionnaire des sourates du Coran indexées par leur nom phonétique.

        Si le dictionnaire n'est pas encore initialisé, il est construit à partir des données disponibles
        dans l'attribut `quran`.

        Returns:
            Dict[str, QuranSourateData]: Un dictionnaire contenant les sourates indexées par leurs noms phonétiques.
        """
        if self.__surahs_by_name_phonetic is None:
            self.__surahs_by_name_phonetic = {
                s["nom_phonetique"]: s for s in self.quran["sourates"]
            }
        return self.__surahs_by_name_phonetic

    @property
    def surahs_by_number(self) -> Dict[int, QuranSurahsData]:
        """
        Retourne un dictionnaire des sourates indexées par leur numéro de position.

        Returns:
            Dict[int, QuranSouratetData]: Les sourates indexées par position.
        """
        if self.__surahs_by_number is None:
            self.__surahs_by_number = {s["position"]: s for s in self.quran["sourates"]}
        return self.__surahs_by_number

    @property
    def surahs_by_name_fr(self) -> Dict[str, QuranSurahsData]:
        """
        Retourne un dictionnaire des sourates indexées par leur nom en français.

        Returns:
            Dict[str, QuranSouratetData]: Les sourates indexées par nom en français.
        """
        if self.__surahs_by_name_fr is None:
            self.__surahs_by_name_fr = {
                s["nom_sourate"]: s for s in self.quran["sourates"]
            }
        return self.__surahs_by_name_fr

    @property
    def surahs_by_name_arabic(self) -> Dict[str, QuranSurahsData]:
        """
        Retourne un dictionnaire des sourates indexées par leur nom en arabe.

        Returns:
            Dict[str, QuranSouratetData]: Les sourates indexées par nom en arabe.
        """
        if self.__surahs_by_name_arabic is None:
            self.__surahs_by_name_arabic = {s["nom"]: s for s in self.quran["sourates"]}
        return self.__surahs_by_name_arabic

    @property
    def lower_surahs_by_name_fr(self) -> Optional[Dict[str, QuranSurahsData]]:
        """
        Retourne un dictionnaire des sourates du Coran indexées par leur nom en français (en minuscules).

        Si le dictionnaire n'est pas encore initialisé, il est construit à partir des données disponibles
        dans l'attribut `quran`.

        Returns:
            Optional[Dict[str, QuranSourateData]]: Un dictionnaire contenant les sourates indexées par leurs noms en français (en minuscules), ou None si non initialisé.
        """
        if self.__lower_surahs_by_name_fr is None:
            self.__lower_surahs_by_name_fr = {
                s["nom_sourate"].lower(): s for s in self.quran["sourates"]
            }
        return self.__lower_surahs_by_name_fr

    @property
    def lower_surahs_by_name_phonetic(self) -> Optional[Dict[str, QuranSurahsData]]:
        """
        Retourne un dictionnaire des sourates du Coran indexées par leur nom phonétique (en minuscules).

        Si le dictionnaire n'est pas encore initialisé, il est construit à partir des données disponibles
        dans l'attribut `quran`.

        Returns:
            Optional[Dict[str, QuranSourateData]]: Un dictionnaire contenant les sourates indexées par leurs noms phonétiques (en minuscules), ou None si non initialisé.
        """
        if self.__lower_surahs_by_name_phonetic is None:
            self.__lower_surahs_by_name_phonetic = {
                s["nom_phonetique"].lower(): s for s in self.quran["sourates"]
            }
        return self.__lower_surahs_by_name_phonetic

    def search_by_type_revelation(
        self,
        type_of_revelation: Union[RevelationType, Literal["Medinois", "Mecquoise"]],
    ) -> List[QuranSurahsData]:
        """
        Retourne toutes les sourates correspondant au type de révélation spécifié.

        Args:
            type_of_revelation (Union[RevelationType, Literal["Medinois", "Mecquoise"]]): Le type de révélation (Medinois ou Mecquoise).

        Returns:
            List[QuranSouratetData]: Liste des sourates correspondant au type de révélation.
        """
        if isinstance(type_of_revelation, RevelationType):
            return [
                sourate
                for sourate in self.quran["sourates"]
                if sourate["revelation"] == type_of_revelation.value
            ]
        else:
            return [
                sourate
                for sourate in self.quran["sourates"]
                if sourate["revelation"] == type_of_revelation
            ]

    @overload
    def select_one(
        self, filterby: Literal["arabic"], value: str
    ) -> Optional[QuranSurahsData]: ...
    @overload
    def select_one(
        self, filterby: Literal["phonetic"], value: str
    ) -> Optional[QuranSurahsData]: ...
    @overload
    def select_one(
        self, filterby: Literal["fr"], value: str
    ) -> Optional[QuranSurahsData]: ...
    @overload
    def select_one(
        self, filterby: Literal["number"], value: int
    ) -> Optional[QuranSurahsData]: ...

    def select_one(
        self,
        filterby: Literal["arabic", "phonetic", "fr", "number"],
        value: Union[str, int],
    ) -> Optional[QuranSurahsData]:
        """
        Retourne une sourate en fonction du type de filtre et de la valeur spécifiée.

        Args:
            filterby (Literal["arabic", "phonetic", "fr", "number"]): Le type de filtre à utiliser.
            value (Union[str, int]): La valeur du filtre.

        Returns:
            Optional[QuranSurahsData]: La sourate correspondante ou None si non trouvée.
        """
        if filterby == "arabic":
            return self.surahs_by_name_arabic.get(value, None)
        elif filterby == "phonetic":
            return self.lower_surahs_by_name_phonetic.get(value.lower(), None)
        elif filterby == "fr":
            return self.lower_surahs_by_name_fr.get(value.lower(), None)
        elif filterby == "number":
            return self.surahs_by_number.get(value, None)
        else:
            return None

    @overload
    def select(
        self, filterby: Literal["arabic"], values: Union[tuple[str], list[str]]
    ) -> tuple[QuranSurahsData]: ...

    @overload
    def select(
        self, filterby: Literal["fr"], values: Union[tuple[str], list[str]]
    ) -> tuple[QuranSurahsData]: ...

    @overload
    def select(
        self, filterby: Literal["phonetic"], values: Union[tuple[str], list[str]]
    ) -> tuple[QuranSurahsData]: ...

    @overload
    def select(
        self, filterby: Literal["number"], values: Union[tuple[int], list[int]]
    ) -> tuple[QuranSurahsData]: ...

    def select(
        self,
        filterby: TypeFilterSearch,
        values: Union[list[str], list[int], tuple[str], tuple[int]],
    ) -> tuple[QuranSurahsData]:
        """
        Sélectionne plusieurs sourates en fonction d'un type de filtre et d'une liste ou d'un tuple de valeurs.

        Args:
            filterby (TypeFilterSearch): Type de filtre ("arabic", "fr", "phonetic", ou "number").
            values (Union[list[str], list[int], tuple[str], tuple[int]]): Liste ou tuple des valeurs à rechercher.

        Returns:
            tuple[QuranSurahsData]: Tuple contenant les sourates correspondantes.
        """
        result = [
            i
            for value in values
            if (
                i := self.select_one(
                    filterby, value.lower() if filterby in ["fr", "phonetic"] else value
                )
            )
        ]
        return tuple(result)

    def get_names_surahs(
        self, by: Literal["arabic", "fr", "phonetic"], tolower: bool = False
    ) -> List[str]:
        """
        Récupère les noms des sourates en fonction du filtre spécifié.

        Args:
            by (Literal["arabic", "fr", "phonetic"]): Type de noms ("arabic", "fr", ou "phonetic").
            tolower (bool, optional): Si True, retourne les noms en minuscules (applicable pour "fr" et "phonetic").

        Returns:
            List[str]: Liste des noms de sourates.
        """
        elements = (
            self.lower_surahs_by_name_fr
            if tolower and by == "fr"
            else (
                self.lower_surahs_by_name_phonetic
                if tolower and by == "phonetic"
                else (
                    self.surahs_by_name_arabic
                    if by == "arabic"
                    else (
                        self.surahs_by_name_fr
                        if by == "fr"
                        else self.surahs_by_name_phonetic
                    )
                )
            )
        )
        return list(elements.keys())

    @overload
    def get_versets(
        self,
        surah: QuranSurahsData,
        language: TypeFilterVerset,
        type_return: Literal["str"],
    ) -> str: ...

    @overload
    def get_versets(
        self,
        surah: QuranSurahsData,
        language: TypeFilterVerset,
        type_return: Literal["list"],
    ) -> List[str]: ...

    def get_versets(
        self,
        surah: QuranSurahsData,
        language: TypeFilterVerset,
        type_return: Literal["str", "list"],
    ) -> Union[str, List[str]]:
        """
        Récupère les versets d'une sourate dans une langue spécifique.

        Args:
            surah (QuranSurahsData): Les données de la sourate.
            language (TypeFilterVerset): La langue des versets ("fr" ou "arabic").
            type_return (Literal["str", "list"]): Format de retour ("str" pour une chaîne, "list" pour une liste).

        Returns:
            Union[str, List[str]]: Les versets au format spécifié.
        """
        if type_return == "str":
            return "\n".join(
                verset["text"] if language == "fr" else verset["text_arabe"]
                for verset in surah["versets"]
            )
        elif type_return == "list":
            return [
                verset["text"] if language == "fr" else verset["text_arabe"]
                for verset in surah["versets"]
            ]

    @overload
    def get_verset(
        self, language: TypeFilterVerset, surah: QuranSurahsData, number: int
    ) -> str: ...

    @overload
    def get_verset(
        self, language: TypeFilterVerset, surah: QuranSurahsData, number: list[int]
    ) -> list[str]: ...

    def get_verset(
        self,
        language: TypeFilterVerset,
        surah: QuranSurahsData,
        number: Union[int, list[int]],
    ) -> Union[str, list[str]]:
        """
        Extrait un ou plusieurs versets d'une sourate dans une langue spécifique.

        Args:
            language (TypeFilterVerset): La langue du verset ("fr" ou "arabic").
            surah (QuranSurahsData): La sourate contenant les versets.
            number (Union[int, list[int]]): Le numéro du verset ou une liste de numéros.

        Returns:
            Union[str, list[str]]: Le texte du verset (str) ou une liste de textes (list[str]).

        Raises:
            Exception: Si le type de `number` est invalide ou si un numéro de verset est incorrect.
        """
        if isinstance(number, int):
            check_number_verset(surah, number)
            return _extract_verset(surah, number, language)
        elif isinstance(number, list):
            for i in number:
                check_number_verset(surah, i)  # Vérifie si les versets sont valides
            versets = map(lambda x: _extract_verset(surah, x, language), number)
            return list(versets)
        raise Exception("Invalid type: must be int or list[int]")

    def check_format_get(self, value: str) -> bool:
        """
        Vérifie si une chaîne suit le format attendu pour un verset ou une sourate.

        Args:
            value (str): La chaîne à vérifier (exemple : "1:1" ou "2").

        Returns:
            bool: True si le format est valide, sinon False.
        """
        pattern = r"^\d+(?::\d+)?$"
        return bool(re.match(pattern, value))

    def get(
        self, surah_and_verset: str, language: TypeFilterVerset = "fr"
    ) -> Union[tuple[QuranSurahsData, QuranVersetData], tuple[QuranSurahsData, None]]:
        """
        Récupère une sourate et éventuellement un verset en fonction d'une chaîne au format "surah:verset".

        Args:
            surah_and_verset (str): La chaîne contenant le numéro de la sourate et éventuellement le numéro du verset.
            language (TypeFilterVerset, optional): La langue du verset ("fr" ou "arabic"). Par défaut, "fr".

        Returns:
            Union[tuple[QuranSurahsData, QuranVersetData], tuple[QuranSurahsData, None]]:
                Un tuple contenant la sourate et le verset (si fourni). Si aucun verset n'est indiqué, retourne `None`.

        Raises:
            FormatValueGet: Si le format de la chaîne est invalide.
            SurahNotFound: Si la sourate n'est pas trouvée.
        """
        if not self.check_format_get(surah_and_verset):
            raise FormatValueGet("Format value not matched")

        values = surah_and_verset.split(":")
        surah = None
        verset = None

        if len(values) > 1:
            surah = self.select_one("number", int(values[0]))
            if surah is not None:
                verset = self.get_verset(language, surah, int(values[1]))
                return surah, verset
            else:
                raise SurahNotFound(f"Surah not found for number {values[0]}")
        else:
            surah = self.select_one("number", int(values[0]))
            if surah is None:
                raise SurahNotFound(f"Surah not found for number {values[0]}")
            return surah, None

    def get_simple_page(self, page: int) -> List[QuranSurahsData]:
        """
        Récupère toutes les sourates contenant des versets situés sur une page spécifique.

        Args:
            page (int): Le numéro de la page.

        Returns:
            List[QuranSurahsData]: Une liste de sourates contenant des versets situés sur la page spécifiée.
        """
        data_pages: List[QuranSurahsData] = []
        seen_surahs = set()

        for sourate in self.quran['sourates']:
            if sourate["nom"] in seen_surahs:
                continue
            for verset in sourate["versets"]:
                if verset["page"] == page:
                    data_pages.append(sourate)
                    seen_surahs.add(sourate["nom"])
                    break  
        return data_pages


    def get_last_page(self) -> List[QuranSurahsData]:
        """
        Récupère toutes les sourates contenant des versets situés sur la dernière page du Coran.

        Returns:
            List[QuranSurahsData]: Une liste de sourates contenant des versets situés sur la dernière page.
        
        Raises:
            SurahNotFound: Si la sourate numéro 114 n'est pas trouvée.
        """
        last_surahs = self.select_one("number", 114)
        len_versets = len(last_surahs["versets"])
        last_verset = last_surahs["versets"][len_versets - 1]
        last_page = last_verset["page"]
        
        last_pages: List[QuranSurahsData] = []
        seen_surahs = set()

        for sourate in self.quran["sourates"]:
            if sourate["nom"] in seen_surahs:
                continue
            for verset in sourate["versets"]:
                if verset["page"] == last_page:
                    last_pages.append(sourate)
                    seen_surahs.add(sourate["nom"])
                    break
        return last_pages
