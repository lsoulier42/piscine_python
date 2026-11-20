# py04 / ex04 — Exporter le repository

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `export.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Ton repository peut maintenant contenir plusieurs utilisateurs. Pour sauvegarder ou transmettre ces données à une autre application, tu vas exporter la liste des utilisateurs vers un fichier JSON. Cet exercice réutilise les composants construits précédemment.

## Objectif

Implémente `export_users(repo: UserRepository, path: str) -> int`. La fonction reçoit un repository d'utilisateurs et le chemin d'un fichier de sortie. Écris dans ce fichier un tableau JSON en UTF-8 : chaque utilisateur doit être représenté par un dictionnaire contenant `id`, `email` et `active`. Retourne le nombre d'utilisateurs exportés.

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
