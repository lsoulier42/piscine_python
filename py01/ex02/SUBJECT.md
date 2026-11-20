# py01 / ex02 — Inventaire

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `inventory.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Un magasin possède deux inventaires, par exemple ceux de deux entrepôts. Chaque inventaire associe une référence produit à une quantité disponible. Tu vas créer un inventaire consolidé en additionnant les quantités des mêmes références, sans toucher aux données initiales.

## Objectif

Implémente `merge_stock(a: dict[str, int], b: dict[str, int]) -> dict[str, int]`. Chaque dictionnaire associe une référence de produit à sa quantité en stock. Retourne un nouveau dictionnaire contenant toutes les références présentes dans `a` ou `b`, en additionnant leurs quantités quand elles apparaissent dans les deux inventaires. Conserve les références dont la quantité vaut zéro et ne modifie aucun des dictionnaires d'origine.

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
