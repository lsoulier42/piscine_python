# py02 / ex02 — Découpage en pages

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `paginate.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Imagine une application qui affiche plusieurs centaines de produits ou d'utilisateurs. Plutôt que de tout afficher simultanément, on souhaite présenter les résultats par groupes de taille fixe, avec un système de pagination. Tu vas créer une fonction permettant de récupérer uniquement les éléments correspondant à une page donnée.

## Objectif

Implémente `paginate(items: list, page: int, per_page: int) -> list`. La fonction reçoit une liste, le numéro de la page demandée et le nombre d'éléments à afficher par page. Elle doit retourner uniquement les éléments de cette page, sans modifier la liste originale. La première page porte le numéro `1`. Si la page demandée dépasse les éléments disponibles, retourne une liste vide. Si `page` ou `per_page` est inférieur ou égal à zéro, lève `ValueError`.

Par exemple, `paginate([10, 20, 30, 40, 50], 2, 2)` doit retourner `[30, 40]`.

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
