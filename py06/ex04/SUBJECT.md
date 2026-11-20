# py06 / ex04 — Un outil de contrôle

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `audit.py` |
| Version | Python 3.15 |
| Dépendances | Bibliothèque standard uniquement |

## Contexte et finalité

Pour auditer rapidement un projet Python, tu veux connaître le nombre de lignes non vides de chaque fichier source et le total du projet. Tu vas créer un outil en ligne de commande qui explore un dossier et produit ce bilan en ignorant les répertoires techniques.

## Objectif

Crée un programme `audit.py` qui s'exécute avec `python audit.py PATH`. Il doit explorer récursivement le dossier fourni, repérer les fichiers `*.py` et compter, pour chacun, les lignes non vides. Affiche les résultats triés par chemin relatif, puis une dernière ligne au format `TOTAL: N` avec la somme des lignes non vides. Ignore les dossiers `.venv` et `__pycache__`.

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
