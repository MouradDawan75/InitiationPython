# Variable: est une zone mémoire contenant une valeur typée

# Types numériques: int, float, complex
# type textuel: str (string)
# type boolean: True/False
# type listes: range, tuple, list
# type ensemble: set
# type mapping: dictionnaire (dict)

# Déclaration de variables:
# En Python le typage est dynamique. Pas besoin de spécifier le type de la variable. x = 10
# Java utilise le typage statique: int x = 10

entier = 10
texte = "chaine"
texte2 = 'autre chaine'
floattant = 10.55
erreur = True
complexe = 4 + 2j # j est le nombre imaginaire

print(entier)
print(texte)
print(floattant)
print(erreur)
print(complexe.real)
print(complexe.imag)

# C'est le compilateur qui détermine le type de la variable selon la velur qu'on lui a affecté

floattant = 'chaine'

# Convention de nommage pour les variables:
# Le nom d'une variable commence par une lettre
# doit être en miniscules 
# PascalCase: MaVariable
# camelCase: maVariable
# snake_case: ma_variable -> convention utilisée par Python
# Python est case sensitive (sensibe à la casse): age et Age sont 2 variables différentes

# Constante: est une variable dont on ne peut pas modifier le contenu. Cette notion n'existe pas réellement, c'est 
# plus une convention de nommage.

MA_CONSTANTE = 10

# MA_CONSTANTE = 'chaine'

print(MA_CONSTANTE)

# Variables nulles: 

x = None # None = Null
print(x)

print(">>>>>>>> Vérifier le type d'une variabe:")

y = 15
s = 'chaine'

print(type(y))
print(type(s))

print(">>>>>> ID des variables:")

x = 10
print(id(x))

y = x
print(id(y))

x = 99
print(id(x))

# On a une certiane liberté dans l'écriture des nombres floattants:

i = 0.99
i = 00.99
i = .99

# Pour les grands nombres, on peut utiliser cette syntaxe pour des questions de lisibilité:

x = 456_789_569

print(">>>>> Conversion de types: ")

b = 10
f = float(b)

print(f)

k = 10.55
l = int(k)

print(l)

s = '99'
i = int(s)

print(i)

nb1 = int(input("Premier nombre: "))
nb2 = int(input("Second nombre: "))

somme = nb1 + nb2
print("somme = " + str(somme)) # En Python, on ne peut concaténer que des chaines

print(">>>>>>> Module random:")

import random

aleatoire = random.randint(1,10)

print(aleatoire)