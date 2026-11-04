# py07 / ex00 — Projet de synthèse

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `etl.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Objectif

CLI `python etl.py INPUT_CSV OUTPUT_JSON` : CSV date/customer/amount_cents/status, ignorer status != paid, refuser montants invalides ou négatifs, agréger par client, trier, JSON customers + grand_total_cents ; pas de sortie si erreur, stderr/code non nul ; cinq tests et README.

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
