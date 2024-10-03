"""
Ce module est une bibliothèque de fonctions très intéressantes

Il contient des fonctions très utiles qu'on peut utiliser dans les autres modules
"""

print(__doc__)

import math

print(math.__doc__)

print(help(math.acos))

# EN Python, on peut documenter des modules, des classes et des fonctions.

def ma_fonction():

    """
    Une fonction à titre d'exemple
    Documentation de la fonction.
    """

    print('test')


print(ma_fonction.__doc__)

##### Syntaxe EpyText

"""
DocString de type EpyText
@param param1: décrire param1
@param param2: décrire param2
@return: Décrire ce qui retourné
"""

##### Syntaxe reST

"""
DocString de type reST
:param param1: décrire param1
:param param2: décrire param2
:return: Décrire ce qui retourné
"""

##### Syntaxe Google

"""
DocString de type Google - plus lisible car elle sépare les params du résultat renvoyé
Args:
    param1: décrire param1
    param2: décrire param2

returns:
    Décrire ce qui est retourné
"""

# Dans Vs Code: installez l'extension autodocstring

def somme(x:int, y:int) -> int:
    """Fonction qui renvoie la somme de deux entiers

    Args:
        x (int): est un entier
        y (int): est un entier

    Returns:
        int: la somme de x et y
    """

    return x+y

# module de base de Python: pydoc

# Dans le terminal, exécutez la commande suivante: python -m pydoc
# Testez python -m pydoc -b
# Testez python -m pydoc -w nom_du_module -> pour générer un fichier html pour la doc

# Commande: python -m pydoc -w 20-Documentation\\documentation.py