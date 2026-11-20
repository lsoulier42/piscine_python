# py05 / ex01 — Flux paresseux

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `chunks.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Une application peut devoir traiter une longue liste de résultats par petits groupes, par exemple pour les envoyer à une API ou les afficher progressivement. Tu vas créer un outil qui fournit ces groupes les uns après les autres, sans préparer toute la liste des groupes à l'avance.

## Objectif

Implémente `chunks(items: list, size: int)` sous la forme d'un générateur. Il doit fournir successivement des sous-listes de `items`, contenant au maximum `size` éléments chacune, jusqu'à épuisement de la liste. Ne construis pas à l'avance la liste complète des groupes. Si `size` est inférieur ou égal à `0`, lève `ValueError`.

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
