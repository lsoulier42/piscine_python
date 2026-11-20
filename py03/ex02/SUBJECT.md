# py03 / ex02 — CSV vers JSON

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `csv_export.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Un service reçoit des données sous forme de tableau CSV, alors qu'une autre application attend un fichier JSON. Tu vas créer un petit convertisseur qui lit les lignes du CSV, les transforme en objets et écrit le résultat dans un nouveau fichier.

## Objectif

Implémente `csv_to_json(csv_path: str, json_path: str) -> int`. Lis le fichier CSV indiqué par `csv_path` et transforme chaque ligne en dictionnaire en utilisant les noms de colonnes comme clés (`csv.DictReader`). Écris ensuite la liste de ces dictionnaires dans le fichier `json_path`, en JSON UTF-8, avec `ensure_ascii=False` et une indentation de deux espaces (`indent=2`). Retourne le nombre de lignes de données exportées.

## Contraintes

- Ne pas modifier les arguments fournis, sauf demande explicite.
- Respecter les signatures, sorties et exceptions demandées.
- Éviter les bibliothèques tierces.

## Méthode

1. Identifier ce que tu sais déjà faire en PHP.
2. Trouver l'équivalent Python dans la documentation officielle.
3. Implémenter l'exercice sans copier une solution complète.
4. Tester le cas normal, le cas vide et les entrées invalides pertinentes.

## Bonus facultatif

Écrire au moins deux tests supplémentaires qui couvrent des cas limites.

## Autoévaluation

- [ ] J'obtiens le résultat demandé.
- [ ] J'ai testé les cas limites.
- [ ] Je peux expliquer mon code.
- [ ] J'ai consulté la documentation Python.

Documentation : https://docs.python.org/3.15/
