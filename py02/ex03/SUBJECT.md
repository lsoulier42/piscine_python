# py02 / ex03 — Valider un payload

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `validation.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Lorsqu'une API reçoit des informations pour créer un compte utilisateur, elle ne peut pas supposer que les données envoyées sont valides. Certains champs peuvent manquer, contenir des valeurs incorrectes ou avoir un type inattendu. Tu vas développer une fonction qui vérifie les informations essentielles d'un utilisateur et retourne des données normalisées, prêtes à être utilisées par l'application.

## Objectif

Implémente `validate_user(data: dict) -> dict`. La fonction reçoit un dictionnaire contenant les informations d'un utilisateur, par exemple `{'email': ' Alice@Example.com ', 'age': 24}`. Elle doit vérifier les champs `email` et `age`, puis retourner un nouveau dictionnaire ne contenant que ces deux informations.

- **E-mail** : la valeur doit être une chaîne (`str`) contenant exactement un caractère `@`, avec au moins un caractère avant et après. Retire les espaces en début et en fin de chaîne, puis convertis l'adresse en minuscules.
- **Âge** : la valeur doit être un entier (`int`) supérieur ou égal à `18`. Attention : en Python, `bool` est une sous-classe de `int`, mais les booléens doivent être refusés ici.
- **Données invalides** : si un champ est manquant ou ne respecte pas ces règles, lève `ValueError`.

Par exemple, `validate_user({'email': ' Alice@Example.com ', 'age': 24, 'admin': True})` doit retourner `{'email': 'alice@example.com', 'age': 24}`. Le champ `admin` ne doit pas figurer dans le résultat.

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
