# py06 / ex01 — match/case

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `router.py` |
| Version | Python 3.15 |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Un petit programme interactif reçoit des commandes textuelles comme « help », « status » ou « quit ». Tu vas écrire le répartiteur qui associe à chaque commande une réponse, y compris lorsqu'un utilisateur saisit une commande inconnue.

## Objectif

Implémente `route(command: str) -> str` en utilisant `match`. La fonction reçoit une commande textuelle et retourne la réponse correspondante : `help` donne `Available: help, status, quit`, `status` donne `OK` et `quit` donne `Bye`. Pour toute autre commande, retourne `Unknown command`. Les espaces en début ou fin de commande et les différences de casse ne doivent pas influencer le résultat.

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
