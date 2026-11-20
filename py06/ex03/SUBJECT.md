# py06 / ex03 — Sentinelle explicite 3.15

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `sentinel_config.py` |
| Version | Python 3.15 |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Dans une configuration, une clé absente ne signifie pas la même chose qu'une clé présente dont la valeur est `None`. Tu vas créer un accès aux paramètres capable de distinguer ces situations, même lorsqu'aucune valeur par défaut n'a été fournie.

## Objectif

Crée une valeur sentinelle `MISSING` avec `sentinel` de Python 3.15, puis implémente `get_setting(mapping: dict, key: str, default=MISSING)`. Si la clé existe dans le dictionnaire, retourne sa valeur, même lorsqu'elle vaut `None`. Si la clé est absente et qu'un argument `default` a été fourni, retourne ce défaut. Si la clé est absente et qu'aucun défaut n'a été fourni, lève `KeyError`.

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
