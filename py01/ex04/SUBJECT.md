# py01 / ex04 — Panier API

| Champ | Valeur |
| --- | --- |
| Fichier à rendre | `cart.py` |
| Fonction à écrire | `summarize_cart(items: list[dict]) -> dict` |
| Version | Python 3.15 |
| Dépendances | Bibliothèque standard uniquement |

## Contexte

Tu développes une fonction de synthèse pour le panier d'une boutique en ligne. Le panier est une liste de dictionnaires : chaque dictionnaire représente une ligne de commande.

Chaque ligne possède trois champs :

- `sku` (`str`) : référence d'un produit, abréviation de *Stock Keeping Unit*. Par exemple, `"TSHIRT-RED-M"` désigne un tee-shirt rouge de taille M. Deux lignes ayant le même SKU concernent le même produit.
- `quantity` (`int`) : nombre d'unités commandées sur cette ligne, strictement positif.
- `unit_price` (`int`) : prix d'une seule unité, exprimé **en centimes**, positif ou nul.

Le prix d'une ligne est `quantity * unit_price`. Pas besoin de convertir en euros ou d'utiliser des flottants.

## Objectif

Écris `summarize_cart(items: list[dict]) -> dict`.

La fonction doit retourner un dictionnaire contenant :

- `total_cents` : montant total du panier en centimes, toutes lignes confondues ;
- `quantities` : dictionnaire associant chaque référence produit (SKU) à la quantité totale commandée. Plusieurs lignes portant le même SKU doivent avoir leurs quantités additionnées.

### Exemple

Entrée :

```python
items = [
    {"sku": "TSHIRT-RED-M", "quantity": 2, "unit_price": 1500},
    {"sku": "MUG-BLUE", "quantity": 1, "unit_price": 800},
    {"sku": "TSHIRT-RED-M", "quantity": 3, "unit_price": 1500},
]
```

Résultat attendu :

```python
{
    "total_cents": 8300,
    "quantities": {
        "TSHIRT-RED-M": 5,
        "MUG-BLUE": 1,
    },
}
```

Le montant total additionne toutes les lignes ; les quantités sont regroupées par référence.

Pour un panier vide (`[]`), retourner :

```python
{"total_cents": 0, "quantities": {}}
```

## Contraintes

- Ne pas modifier la liste `items` ni les dictionnaires d'entrée.
- Bibliothèque standard uniquement.
- On suppose que les lignes respectent les types et contraintes indiqués : pas de validation supplémentaire demandée.
- Si un SKU apparaît plusieurs fois avec des prix unitaires différents, calculer le montant de chaque ligne séparément avant d'additionner ; ne regrouper que les quantités.

## Pistes (sans solution)

- Un dictionnaire est pratique pour regrouper des valeurs par référence.
- Réutilise ce que tu as appris dans `word_counts()` et `merge_stock()`.
- Teste des lignes répétées, des références différentes et le panier vide.

## Bonus facultatif

Écrire au moins deux tests supplémentaires couvrant des cas limites.

## Autoévaluation

- [ ] Le total est correct en centimes.
- [ ] Les quantités de références identiques sont additionnées.
- [ ] Le panier vide fonctionne.
- [ ] Les données d'entrée restent inchangées.

Documentation : https://docs.python.org/3.15/
