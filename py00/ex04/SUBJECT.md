# py00 / ex04 — Mini facture

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `invoice.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Une application de facturation doit calculer le montant TTC d'un ensemble de prix. Pour éviter les imprécisions des nombres décimaux, les montants sont représentés en centimes. Tu vas calculer un total avec taxe et un arrondi adapté aux montants monétaires.

## Objectif

Implémente `total_with_tax(prices: list[int], tax_percent: int) -> int`. La fonction reçoit une liste de prix exprimés en centimes et un taux de taxe exprimé en pourcentage. Elle doit retourner le montant total TTC en centimes, avec un arrondi au centime le plus proche et les demi-centimes arrondis vers le haut. Si un prix ou le taux est négatif, lève `ValueError`.

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
