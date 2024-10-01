# Un module doit être importé avant son utilisation

import random

random.randint(1,10)

# On peut aussi modifier le nom du module importé -> définir un alias

import random as rd

rd.randint(1,10)

# On peut aussi importer des éléments spécifiques à partir d'un module

from math import sqrt

sqrt(25)

# On peut aussi modifier le nom des élémenys spécifiques importés

from math import sqrt as racine_carree

racine_carree(25)

# On peut aussi importer tous éléments d'un module

from math import * 
# pas besoin de spécifier le nom du module -> on doit connaitre toutes les fonctions du module
# Pas très utilisée dans la pratique

sqrt(25)


import math

#math.acos(10)

# Un module est un fichier Python (.py) contenant généralement des fonctions, des classes ou des constantes
# Un package est un répertoire contenant des modules.
# Pour convertir un répertoire en package, il suffit d'ajouter le fichier __init__.py qu'on peut laisse vide.

# Version Python < 3.3: __init__.py est obligatoire
# Version Python >= 3.3: __init__.py n'est plus obligatoire, mais il est recommandé de le générer comme mm.

# Important: le nom d'un package ou d'un module, doit être en miniscules, sans éspaces et sans underscore(_)
# et doit commencer par une lettre

# Appel de my_fonction1:

#import mypackage.mymodule

from mypackage.mymodule import my_fonction1

# Un module importé est toujours exécuté
# Comment empêcher l'exécution d'un module importé?

#my_fonction1()

# __name__ = '__main__' pour un module exécuté
# __name__ = 'nom du module importé'

#print(__name__)

import mypackage.myconstantes as constantes

print(constantes.SERVER)
print(constantes.PORT)
print(constantes.USER)
print(constantes.PASSWORD)

# Exo: dans le dossier principal:
# définir un package nommé mytools, contenant le module myfonctions.py avec une fonction add(x,y)
# Testez cette fonction dans ce module


# Les chemins des packages (modules) visibles par Python sont listés dans sys.path
# Par défaut, il y'à que le dossier en cours qui est visible par Python

import sys
import os # module permettant la gestion des chemins

print(sys.path)

print(__file__) # c:\.......\modules.py

chemin_dossier_en_cours = os.path.dirname(__file__) # c:\......\08-Modules
chemin_dossier_principal = os.path.dirname(chemin_dossier_en_cours) # c:\....\InitiationPython
sys.path.append(chemin_dossier_principal)

# Solution: ajouter le chemin du dossier principal dans sys.path

#chemin_dossier_principal = "c:\.....\InitiationPython"

from mytools.myfonctions import add

print(add(5,10))

# Exception: ModuleNotFound: gestion du sys.path