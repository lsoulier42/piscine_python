# py02 / ex00 — Un parseur fiable

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `parse_int.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Objectif

Implémenter `parse_positive_int(text: str) -> int`, qui convertit une chaîne représentant un entier positif ou nul en `int`.

## Entrées acceptées

- Les chiffres ASCII de `0` à `9` (au moins un chiffre).
- Les espaces en début et en fin de chaîne.
- Un signe `+` facultatif, placé avant les chiffres (après les éventuels espaces initiaux).
- La valeur zéro.

## Entrées refusées

Lever `ValueError` pour :

- Les nombres négatifs (signe `-`).
- Les nombres à partie fractionnaire, comme `3.14` ou `3,14`.
- Les chaînes vides ou composées uniquement d'espaces.
- Tout autre caractère non autorisé, y compris les espaces entre les chiffres.

## Exemples

| Entrée | Résultat attendu |
| --- | --- |
| `"42"` | `42` |
| `"  +42  "` | `42` |
| `"0"` | `0` |
| `"-42"` | `ValueError` |
| `"3.14"` | `ValueError` |
| `""` | `ValueError` |
| `"   "` | `ValueError` |
| `"12 3"` | `ValueError` |
| `"+"` | `ValueError` |

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
