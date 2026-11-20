# py02 / ex01 — Options PHP, kwargs Python

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `options.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Dans une application web, on a régulièrement besoin de construire des URL contenant des paramètres, par exemple pour effectuer une recherche, appliquer des filtres ou naviguer entre plusieurs pages de résultats. Tu vas créer une fonction qui prend une adresse de départ et un ensemble de paramètres, puis construit l'URL complète en les ajoutant correctement.

## Objectif

Implémente `make_url(base: str, **params: str) -> str`. La fonction reçoit une URL de départ et des paramètres nommés à ajouter dans sa chaîne de requête. Encode les noms et valeurs avec `urllib.parse.urlencode`, en conservant l'ordre dans lequel les paramètres ont été fournis. Ajoute `?` si l'URL ne contient pas encore de chaîne de requête, sinon ajoute `&`. Si aucun paramètre n'est fourni, retourne l'URL de départ sans la modifier.

Par exemple, `make_url('/search', q='chat noir', page='2')` doit retourner `'/search?q=chat+noir&page=2'`.

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
