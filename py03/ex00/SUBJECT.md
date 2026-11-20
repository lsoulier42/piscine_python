# py03 / ex00 — Compter un fichier

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `line_stats.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Un outil de documentation ou d'analyse peut avoir besoin d'afficher quelques statistiques sur un fichier texte, comme son nombre de lignes, de mots et de caractères. Tu vas écrire une fonction qui ouvre un fichier et renvoie ces trois informations.

## Objectif

Implémente `line_stats(path: str) -> dict[str, int]`. La fonction doit lire le fichier texte situé à `path` en UTF-8 et retourner un dictionnaire avec trois statistiques : `lines` pour le nombre de lignes (selon `splitlines()`), `words` pour le nombre de mots (selon `split()`) et `characters` pour le nombre total de caractères, sauts de ligne compris.

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
