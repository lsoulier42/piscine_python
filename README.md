# Piscine Python 3.15 — PHP → Python

Parcours pratique inspiré du format des sujets de l'École 42 pour une développeuse PHP/Symfony connaissant aussi C et C++. Projet original, non affilié à l'École 42.

**Objectif : coder immédiatement, apprendre en résolvant des problèmes concrets et avancer à son rythme.**

## Démarrer

1. Installer Python 3.15.x et vérifier `python3.15 --version`.
2. Lire `py00/ex00/SUBJECT.md`.
3. Écrire le code dans `py00/ex00/hello.py`.
4. Exécuter `python3.15 py00/ex00/hello.py`.
5. Poursuivre exercice par exercice ; aucun corrigé n'est fourni.

## Règles

- Ex00 à ex04 dans l'ordre ; les bonus sont facultatifs.
- 15–60 minutes par exercice à titre indicatif ; chercher dans la documentation officielle quand une notion bloque.
- Bibliothèque standard uniquement.
- Tests partiels : `python3.15 -m unittest discover -s tests -v` depuis la racine.

## Programme

- [py00](py00/README.md) — Réflexes Python
- [py01](py01/README.md) — Collections et données
- [py02](py02/README.md) — Fonctions, erreurs et tests
- [py03](py03/README.md) — Fichiers et automatisation
- [py04](py04/README.md) — Objets sans théorie excessive
- [py05](py05/README.md) — Python idiomatique
- [py06](py06/README.md) — Python moderne 3.15
- [py07](py07/README.md) — Examen final — Mini ETL

## Pont PHP → Python

| PHP | Python | À retenir |
| --- | --- | --- |
| `$array = []` | `values = []` | Liste ordonnée, distincte du dict. |
| Tableau associatif | `dict` | Dictionnaire de clés/valeurs. |
| `foreach ($xs as $x)` | `for x in xs:` | Indentation significative. |
| `isset($a['x'])` | `'x' in a` | Distinguer clé absente et valeur None. |
| `??` | `get()` ou test de clé | `get()` peut confondre None et absence. |
| `array_map` | compréhension / `map` | Compréhension souvent plus lisible. |
| `array_filter` | compréhension | Filtrer sans réindexation. |
| `===` | `==` / `is` | Égalité de valeur / identité. |
| `__construct()` | `__init__()` | Dataclasses pour moins de boilerplate. |
| `try/catch` | `try/except` | Exceptions précises. |

## Références

- https://github.com/goffauxs/CPP_Piscine
- https://github.com/semx2a/piscine-python
- https://docs.python.org/3.15/

Une piscine avancée pourra ensuite couvrir APIs, SQL, Pandas et automatisation.
