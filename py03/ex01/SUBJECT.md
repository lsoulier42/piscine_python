# py03 / ex01 — Configuration JSON

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `config.py` |
| Version | Python 3.15 (compatible 3.11+ hors nouveautés) |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Une application démarre avec des paramètres par défaut, mais certains peuvent être personnalisés dans un fichier JSON. Tu vas charger ce fichier et produire la configuration finale : les valeurs du fichier prennent le dessus, tandis que les paramètres absents gardent leur valeur par défaut.

## Objectif

Implémente `load_config(path: str, defaults: dict) -> dict`. La fonction lit un fichier JSON de configuration et le combine avec le dictionnaire `defaults`. Elle doit retourner un nouveau dictionnaire contenant les valeurs par défaut, mais les remplacer par celles du fichier JSON lorsque les mêmes clés y figurent. La fusion se fait uniquement au premier niveau : ne fusionne pas récursivement les dictionnaires imbriqués. Ne modifie pas `defaults`. Si la racine du JSON n'est pas un objet, lève `ValueError`.

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
