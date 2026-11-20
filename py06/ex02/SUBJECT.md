# py06 / ex02 — Configuration immuable 3.15

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `immutable_config.py` |
| Version | Python 3.15 |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Une configuration partagée entre plusieurs parties d'une application ne doit pas pouvoir être modifiée accidentellement. Tu vas fabriquer une copie immuable d'un dictionnaire de paramètres, indépendante des changements ultérieurs de la source.

## Objectif

Implémente `freeze_config(config: dict[str, str])`. La fonction reçoit un dictionnaire de configuration et doit en retourner une copie immuable, en utilisant `frozendict` de Python 3.15. Le résultat doit rester indépendant du dictionnaire d'origine, même si celui-ci est modifié ensuite.

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
