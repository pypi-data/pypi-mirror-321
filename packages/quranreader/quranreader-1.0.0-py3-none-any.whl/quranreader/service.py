import requests
from requests.exceptions import HTTPError, Timeout, RequestException
from quranreader.config import Config
from typing import Union

class Services:
    """
    Classe qui fournit des services pour effectuer des requêtes HTTP et manipuler les données relatives au Coran.
    """

    def __init__(self) -> None:
        pass

    def request_services(self, url: str, to_json: bool = False, to_text: bool = False) -> Union[dict, str, requests.Response]:
        """
        Effectue une requête HTTP GET vers une URL donnée et gère la réponse.

        Args:
            url (str): L'URL cible pour la requête.
            to_json (bool): Indique si la réponse doit être convertie en JSON. Par défaut à False.
            to_text (bool): Indique si la réponse doit être convertie en texte brut. Par défaut à False.

        Returns:
            Union[dict, str, requests.Response]:
                La réponse brute, en JSON (dict), ou en texte (str), selon les paramètres.

        Raises:
            Exception: En cas d'erreur HTTP, de timeout ou d'autres exceptions liées aux requêtes.
        """
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            if to_json:
                return response.json()
            elif to_text:
                return response.text
            else:
                return response

        except HTTPError as http_err:
            raise Exception(f"HTTPError: {http_err}")
        except Timeout:
            raise Exception("Request timeout")
        except RequestException as req_err:
            raise Exception(f"RequestException: {req_err}")
        except Exception as e:
            raise Exception(f"General error: {e}")


    def quran_to_json(self) -> dict:
        """
        Récupère le texte complet du Coran sous forme de JSON à partir de l'API configurée.

        Returns:
            dict: Le texte du Coran sous forme de dictionnaire JSON.

        Raises:
            Exception: En cas d'erreur lors de la requête.
        """
        return self.request_services(Config.url_data_quran(), to_json=True)

