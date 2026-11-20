# py03 / ex04 — Mini outil CLI

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `cli.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Le convertisseur CSV vers JSON de l'exercice précédent fonctionne comme une fonction Python. Tu vas maintenant en faire un outil utilisable directement dans un terminal : on lui fournit les chemins d'entrée et de sortie, et il indique si l'export a réussi ou échoué.

## Objectif

`python cli.py INPUT OUTPUT` : convertir CSV->JSON via ex02, imprimer `Exported N rows`, code 0 ; erreurs en stderr et code non nul.

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
