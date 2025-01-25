
# Isa Malagasy
Isa Malagasy est une bibliothèque python qui permet de convertir des nombres en lettres en malagasy.
Elle supporte les entiers et les nombres décimaux, avec ou sans unité (comme Ariary, fmg, MGA, euro, etc.).

## Installation
Pour installer la bibliothèque, exécutez cette commande : 
```bash
pip install isa-malagasy
```

## Utilisation
### Exemple de base
```python
from isa_malagasy import num2wordsmalagasy

# Exemple avec un entier
print(num2wordsmalagasy(83)) 
# Affiche "telo amby valopolo"

# Exemple avec un nombre décimal
print(num2wordsmalagasy(110.19)) 
# Affiche "folo amby zato faingo sivy ambin'ny folo"
```

### Exemple avec une unité
``` python
print(num2wordsmalagasy(2500, "Ariary")) 
# Affiche "dimanjato sy roa arivo Ariary"

print(num2wordsmalagasy(900.60, "Ariary")) 
# Affiche "sivinjato faingo enimpolo Ariary"

print(num2wordsmalagasy(150.498, "Ariary")) 
# Affiche "dimampolo amby zato faingo dimampolo Ariary"
```

### Syntaxe
Résultat = num2wordsmalagasy(Nombre à transformer [, Unité])

1. Résultat : Chaîne de caractères

    Nombre exprimé en lettres.

2. Nombre à transformer : Entier ou Décimal

    Nombre à transformer en chaîne de caractères. Le nombre à exprimer en lettres a les caractéristiques suivantes :
        18 chiffres significatifs : 12 chiffres maximum pour la partie entière, 6 chiffres maximum pour la partie décimale.

3. Unité : Chaîne de caractères optionnelle

    Unité à utiliser dans le résultat : ariary, fmg, MGA, euro, ...


## Limites
La bibliothèque supporte les nombres jusqu'à 999 999 999 999. Au-delà, un message d'erreur sera affiché.
Les nombres en chaîne de caracrères ne sont pas pris en charge.

## Remarque
La partie décimale est arrondie à 2 chiffres.


# Auteur
Développé par Day Lamiy

Contact :
hatsudai1@gmail.com