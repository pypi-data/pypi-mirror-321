from quranreader.config import Config
from quranreader.service import Services
from quranreader.handle_exception import (
    ByError,
    SurahNotFound,
    VersetNotFound,
    FormatValueGet,
)
from quranreader.interface import (
    QuranData,
    QuranSurahsData,
    QuranVersetData,
    TypeNamesFr,
    TypeNamesFrLower,
    TypeNamesPhonetic,
    TypeNamesPhoneticLower,
)
from quranreader.quranreader import QuranReader

from typing import Union, overload, Literal, Tuple


class SuperQuranReader(QuranReader):
    """
    Classe principale pour effectuer des recherches avancées dans le Coran.

    Hérite de QuranReader et ajoute une interface plus flexible avec la méthode __call__.
    """

    def __init__(self):
        """
        Initialise une instance de SuperQuranReader.
        """
        super().__init__()

    @overload
    def __call__(
        self, by: Literal["fr"], *surahs: TypeNamesFrLower, tolower: Literal[True]
    ) -> Tuple[QuranSurahsData]: ...

    @overload
    def __call__(
        self,
        by: Literal["fr"],
        *surahs: TypeNamesFr,
        tolower: Literal[False],
    ) -> Tuple[QuranSurahsData]: ...

    @overload
    def __call__(
        self,
        by: Literal["phonetic"],
        *surahs: TypeNamesPhoneticLower,
        tolower: Literal[True],
    ) -> Tuple[QuranSurahsData]: ...

    @overload
    def __call__(
        self,
        by: Literal["phonetic"],
        *surahs: TypeNamesPhonetic,
        tolower: Literal[False],
    ) -> Tuple[QuranSurahsData]: ...

    def __call__(
        self,
        by: Literal["fr", "phonetic"],
        *surahs: Union[
            TypeNamesFr, TypeNamesFrLower, TypeNamesPhonetic, TypeNamesPhoneticLower
        ],
        tolower: bool = True,
    ) -> Tuple[QuranSurahsData]:
        """
        Permet de rechercher des sourates en fonction de leur nom.

        Args:
            by (Literal["fr", "phonetic"]): La langue utilisée pour la recherche.
            *surahs (Union[TypeNamesFr, TypeNamesFrLower, TypeNamesPhonetic, TypeNamesPhoneticLower]):
                Les noms des sourates à rechercher.
            tolower (bool, optional): Indique si les noms des sourates doivent être considérés en minuscules.

        Returns:
            List[QuranSurahsData]: Liste des données des sourates correspondantes.

        Raises:
            SurahNotFound: Si une ou plusieurs sourates ne sont pas trouvées.
        """
        # Valider l'argument `tolower` en fonction des types de `surahs`
        if tolower and not all(isinstance(s, (TypeNamesFrLower, TypeNamesPhoneticLower)) for s in surahs):
            raise ValueError("tolower=True nécessite des noms en minuscules.")
        if not tolower and not all(isinstance(s, (TypeNamesFr, TypeNamesPhonetic)) for s in surahs):
            raise ValueError("tolower=False nécessite des noms en majuscules ou mixtes.")

        # Appel interne à `select`
        resp_surahs = self.select(by, *surahs)
        if not resp_surahs:
            raise SurahNotFound(f"Aucune sourate trouvée pour : {surahs}")
        return resp_surahs
