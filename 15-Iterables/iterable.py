# Les collections Python sont des itérables
# 2 types d'itérables: ordonnés (list,tuple,str), non ordonnés (set, dictionnaire)

print(">>> Fonction Enumerate:")

# enumerate s'applique uniquement aux itérables ordonnés:

chaine = "test"

for i in enumerate(chaine):
    print(i) # i est un tuple (element, index)

lst = [1,2,3]

for e in enumerate(lst):
    print(e)

# Eclater le tuple:
for element,index in enumerate(lst):
    print(f"Nombre: {element} - Index: {index}")

print(">>>>> Valeurs vraies:")

print(bool(1))
print(bool(-1))
print(bool("test"))
print(bool([1,2])) # collection non vide: list, tuple, dict, set
print(bool(True))

x = ""

if x:
    print('x chaine non vide')

else:
    print('x chaine vide')

print(">>>> Valeurs fausses:")

print(bool(0))
print(bool(""))
print(bool([])) # collection vide
print(bool(False))
print(bool(None))

print(">>>>> Fonctions natives: any, all")

print(">>>>> Fonction all:")

# Permet de vérifier que toutes les valeurs d'une collection sont vraies

iterable1 = [0,1,0,1]
iterable2 = [1,1,1,1]
iterable3 = [0,0,0,0]
iterable4 = ['a','b','c','d']
iterable5 = [0,1,2,3]

print(all(iterable1)) # False
print(all(iterable2)) # True
print(all(iterable3)) # False
print(all(iterable4)) # True
print(all(iterable5)) # False

print(">>>> Fonction any:")

# Permet de vérifier si au moins une valeur est vraie dans une collection

print(any(iterable1)) # True
print(any(iterable2)) # True
print(any(iterable3)) # False
print(any(iterable4)) # True
print(any(iterable5)) # True

# Autres fonctions natives:

sum(iterable1)
min(iterable1)
max(iterable1)
len(iterable1)