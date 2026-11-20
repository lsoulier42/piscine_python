# py05 / ex04 — Un pipeline lisible

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `pipeline.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Quand on traite de nombreux enregistrements utilisateurs, on ne veut pas forcément constituer une seconde grande liste en mémoire. Tu vas construire un traitement progressif qui ignore les utilisateurs inactifs et fournit les noms valides et normalisés un à un.

## Objectif

Implémente `process_records(records)` sous forme de générateur. La fonction reçoit des dictionnaires représentant des utilisateurs, contenant notamment les champs `name` et `active`. Elle doit produire progressivement les noms normalisés, non vides, des utilisateurs actifs, en ignorant les autres enregistrements. Ne construis pas de liste complète des résultats.

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
