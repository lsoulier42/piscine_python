# py04 / ex03 — Un repository mémoire

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `repository.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Après avoir créé une entité `User`, tu veux pouvoir gérer plusieurs utilisateurs sans mélanger le reste de l'application avec les détails du stockage. Tu vas créer un petit repository en mémoire permettant d'ajouter, consulter, lister et supprimer des utilisateurs.

## Objectif

Crée une classe `UserRepository` pour conserver des objets `User` en mémoire. Elle doit permettre d'ajouter un utilisateur (`add`), de rechercher un utilisateur par identifiant (`get(id)`), de récupérer tous les utilisateurs (`all()`) et d'en supprimer un (`delete(id)`). `get` retourne l'utilisateur trouvé ou `None`. `all` retourne une liste dans l'ordre d'insertion. `delete` retourne un booléen indiquant si une suppression a eu lieu. L'ajout d'un identifiant déjà présent doit lever `ValueError`.

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
