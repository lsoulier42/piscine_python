# py04 / ex00 — Une entité simple

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `user.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Dans une application, un utilisateur possède plusieurs informations qui vont ensemble : son identifiant, son adresse e-mail et son état actif ou non. Tu vas représenter cet utilisateur par une petite entité Python, pour manipuler ces données comme un seul objet.

## Objectif

Crée une classe `User` avec `@dataclass`. Chaque utilisateur possède un identifiant `id` de type `int`, un e-mail `email` de type `str` et un indicateur `active` de type `bool`, qui vaut `True` par défaut. Deux instances ayant les mêmes valeurs de champs doivent être considérées comme égales.

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
