# py07 / ex00 — Projet de synthèse

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `etl.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Tu travailles sur un export de ventes provenant d'une application métier. Le fichier CSV contient des transactions, mais toutes ne correspondent pas à des paiements confirmés. Tu vas construire un petit pipeline ETL qui lit ces données, écarte les transactions non payées, vérifie les montants et produit un bilan JSON agrégé par client. Ce mini-projet rassemble les notions de fichiers, de validation, de collections, de CLI et de tests abordées les jours précédents.

## Objectif

Crée un programme en ligne de commande utilisable avec `python etl.py INPUT_CSV OUTPUT_JSON`. Il reçoit un fichier CSV comportant les colonnes `date`, `customer`, `amount_cents` et `status`, puis produit un bilan des ventes payées au format JSON.

Le programme doit :

1. Lire les transactions du CSV et ignorer celles dont le statut n'est pas `paid`.
2. Refuser les montants invalides ou négatifs.
3. Additionner les montants payés par client et trier les résultats.
4. Écrire un fichier JSON contenant les données `customers` et le total général `grand_total_cents`.
5. Ne pas produire de fichier de sortie en cas d'erreur ; signaler celle-ci sur `stderr` et terminer avec un code non nul.

Accompagne le programme d'au moins cinq tests et d'un `README` expliquant son utilisation.

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
