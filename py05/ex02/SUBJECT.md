# py05 / ex02 — Un décorateur utile

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `timing.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Pendant le débogage ou l'observation d'une application, il peut être utile de savoir combien de fois une fonction est appelée. Tu vas construire un mécanisme réutilisable qui ajoute ce compteur à une fonction sans modifier son comportement initial : c'est l'occasion de découvrir les décorateurs.

## Objectif

Crée un décorateur `@count_calls` qui permet de connaître le nombre d'appels d'une fonction. Une fois décorée, la fonction doit disposer d'un attribut `.calls`, initialisé à `0` et incrémenté à chaque appel. Le décorateur ne doit pas changer la valeur retournée par la fonction ni son nom.

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
