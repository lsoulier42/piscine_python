# py01 / ex01 — Compter les mots

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `word_count.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Pour analyser un message ou un commentaire, on peut commencer par compter combien de fois chaque mot apparaît. Tu vas produire un récapitulatif des occurrences, sans distinguer les majuscules et les minuscules.

## Objectif

Implémente `word_counts(text: str) -> dict[str, int]`. La fonction doit compter le nombre d'occurrences de chaque mot dans un texte et retourner un dictionnaire associant chaque mot à son nombre d'apparitions. Sépare les mots par les espaces, ignore les éléments vides et considère les majuscules et minuscules comme équivalentes. En revanche, conserve la ponctuation dans les mots.

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
