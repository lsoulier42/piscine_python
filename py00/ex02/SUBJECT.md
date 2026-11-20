# py00 / ex02 — Normaliser un identifiant

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `slug.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Dans un blog ou un catalogue, on transforme souvent un titre lisible en identifiant court utilisable dans une URL. Tu vas écrire une fonction qui rend une expression plus régulière en uniformisant les espaces et les majuscules, sans chercher à supprimer les accents.

## Objectif

Implémente `slugify(text: str) -> str`. La fonction reçoit un texte et retourne une version adaptée à un identifiant : retire les espaces au début et à la fin, passe les lettres en minuscules et remplace chaque groupe d'espaces internes par un seul tiret (`-`). Conserve les caractères accentués.

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
