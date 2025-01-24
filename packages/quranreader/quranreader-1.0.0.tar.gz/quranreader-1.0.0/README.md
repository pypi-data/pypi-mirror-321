
# QuranReader Documentation

**QuranReader** est une bibliothèque Python pour interagir avec les données du Coran. Ce projet vise à fournir une interface intuitive pour la recherche, l'extraction, et la manipulation des sourates et des versets.

---

## Table des Matières
- [Introduction](#introduction)
- [Installation](#installation)
- [Fonctionnalités Clés](#fonctionnalités-clés)
- [Classes et Méthodes](#classes-et-méthodes)
  - [QuranReader](#quranreader)
  - [SuperQuranReader](#superquranreader)
- [Exemples](#exemples)
- [Contribuer](#contribuer)
- [License](#license)

---

## Introduction

Le package **QuranReader** est conçu pour faciliter l'accès programmatique au texte du Coran et à ses métadonnées. Il est idéal pour les développeurs cherchant à intégrer des fonctionnalités liées au Coran dans leurs projets.

---

## Installation

Pour installer **QuranReader**, utilisez pip :

```bash
pip install quranreader
```

---

## Fonctionnalités Clés

- Recherche par nom de sourate (français, phonétique, arabe).
- Extraction des métadonnées des sourates et des versets.
- Support multilingue (arabe et français).
- Recherche avancée avec `SuperQuranReader`.

---

## Classes et Méthodes

### QuranReader

#### `__init__()`
- **Description** : Initialise une instance de `QuranReader` et configure l'accès aux données du Coran.
- **Arguments** : Aucun.
- **Retour** : Aucun.

#### `revelation_type_enum()`
- **Description** : Retourne les types de révélations (`Medinois`, `Mecquoise`).
- **Arguments** : Aucun.
- **Retour** : `RevelationType`.

#### `quran`
- **Description** : Retourne les données complètes du Coran.
- **Arguments** : Aucun.
- **Retour** : `QuranData`.

#### `search_by_type_revelation(type_of_revelation)`
- **Description** : Retourne toutes les sourates d'un type de révélation spécifique.
- **Arguments** :
  - `type_of_revelation` : `Literal["Medinois", "Mecquoise"]`.
- **Retour** : Liste de `QuranSurahsData`.

#### `get_verset(language, surah, number)`
- **Description** : Récupère un ou plusieurs versets d'une sourate.
- **Arguments** :
  - `language` : `Literal["fr", "arabic"]`.
  - `surah` : `QuranSurahsData`.
  - `number` : Numéro ou liste de numéros des versets.
- **Retour** : Chaîne ou liste de chaînes.

---

### SuperQuranReader

#### `__call__(by, *surahs, tolower)`
- **Description** : Recherche des sourates en fonction de leur nom et du type de recherche.
- **Arguments** :
  - `by` : `Literal["fr", "phonetic"]`.
  - `*surahs` : Liste des noms de sourates.
  - `tolower` : Si `True`, les noms sont traités en minuscules.
- **Retour** : Liste de `QuranSurahsData`.

#### `get(surah_and_verset, language)`
- **Description** : Récupère une sourate et un verset (si spécifié) au format `sourate:verset`.
- **Arguments** :
  - `surah_and_verset` : Chaîne au format `sourate:verset` ou `sourate`.
  - `language` : `Literal["fr", "arabic"]`.
- **Retour** : Tuple contenant la sourate et éventuellement le verset.

---

## Exemples

### Exemple 1 : Recherche de Sourates
```python
from quranreader import SuperQuranReader

reader = SuperQuranReader()

# Recherche par nom en français
sourah = reader("fr", "al-fatiha", tolower=True)
print(sourah)
```

### Exemple 2 : Extraction de Versets
```python
# Recherche d'un verset spécifique
sourah, verset = reader.get("2:255", language="fr")
print(f"Sourah : {sourah}")
print(f"Verset : {verset}")
```

---

## Contribuer

Les contributions sont les bienvenues ! Merci de suivre les étapes suivantes pour contribuer :
1. Forkez le dépôt GitHub.
2. Clonez votre fork en local.
3. Créez une branche pour vos modifications.
4. Envoyez une Pull Request (PR).

---

## License

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.
