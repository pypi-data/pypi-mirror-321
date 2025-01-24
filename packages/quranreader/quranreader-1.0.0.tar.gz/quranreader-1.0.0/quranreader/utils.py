from quranreader.interface import QuranSurahsData, TypeFilterVerset, QuranVersetData
from quranreader.handle_exception import VersetNotFound


def check_number_verset(surah: QuranSurahsData, number: int):
    """
    Vérifie si un numéro de verset est valide dans une sourate donnée.

    Args:
        surah (QuranSurahsData): Les données de la sourate contenant les versets.
        number (int): Le numéro du verset à vérifier.

    Returns:
        None: Si le numéro de verset est valide.

    Raises:
        VersetNotFound: Si le numéro de verset est supérieur au nombre total de versets dans la sourate.
    """
    versets = surah["versets"]
    if number < len(versets):
        return None
    else:
        raise VersetNotFound(f"Invalid number verset")


def _extract_verset(
    surah: QuranSurahsData, number: int, language: TypeFilterVerset
) -> str:
    """
    Extrait le texte d'un verset d'une sourate en fonction de son numéro et de la langue spécifiée.

    Args:
        surah (QuranSurahsData): Les données de la sourate contenant les versets.
        number (int): Le numéro du verset à extraire (position dans la sourate).
        language (TypeFilterVerset): La langue du texte à extraire ("arabic" ou "fr").

    Returns:
        str: Le texte du verset dans la langue spécifiée.

    Raises:
        VersetNotFound: Si le verset avec le numéro spécifié n'est pas trouvé dans la sourate.
    """
    for verset in surah["versets"]:
        if number == verset["position_ds_sourate"]:
            return verset["text_arabe"] if language == "arabic" else verset["text"]
    raise VersetNotFound("Verset not found")
