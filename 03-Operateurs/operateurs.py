print(">>>>>> Opérateurs arithmétiques:")

print("**** Addition: ")

a = 5
b = 2
c = a + b
c += 2 # syntaxe simpifiée: c = c + 2
print(f"c = {c}")

print("**** Soustraction: ")

a = 5
b = 2
c = a - b
c -= 2 # syntaxe simpifiée: c = c - 2
print(f"c = {c}")

print("**** Multiplication: ")

a = 5
b = 2
c = a * b
c *= 2 # syntaxe simpifiée: c = c * 2
print(f"c = {c}")

print("**** Division: ")

a = 5
b = 2
c = a / b
c /= 2 # syntaxe simpifiée: c = c / 2
print(f"c = {c}")

print("**** Division entière: ")

a = 5
b = 2
c = a // b
c //= 2 # syntaxe simpifiée: c = c // 2
print(f"c = {c}")

print("**** Modulo: reste de la division entière ")

a = 5
b = 2
c = a % b
c %= 2 # syntaxe simpifiée: c = c + 2
print(f"c = {c}")

print("**** Puissance: ")

a = 5
b = 2
c = a ** b # a puissance b
c **= 2 # syntaxe simpifiée: c = c + 2
print(f"c = {c}")

print(">>>>>>>> Opérateurs de comparaison:")

# Renvoient True/False: >, >=, <, <=, == (égalité), != (différent)
# Renvoient True/False: >, >=, <, <=, == (égalité), != (différent)

x = 5
y = 7

print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
print(x == y)
print(x != y)

print(">>>>>> Opérateurs logiques: ")

# Renvoient un True/False: and, or et not
# 
#Table logique:
# A     B   A and B     A or B
# v     v      v           v
# v     f      f           v
# f     f      f           f
# f     v      f           v

print((x < 7) and (x > 0)) # True       
print((x > 7) and (x > 0)) # False       
print((x > 7) or (x > 0)) # True       

print(">>>>> Affectations multiples:")

# Si des variables sont du mm avec la mm valeur, on peut faire:

v1 = v2 = v3 = 10

# Si des variables ne sont pas du mm types, on peut faire:

# Syntaxe non recommandée en pratique

var1,var2,var3 = 10, True, 'test'

print(">>>> Opérateurs: is et in")

# S'utilisent avec des collections

list1 = [1,2,3]
list2 = [1,2,3]

print(list1 == list2) # True: car mm contenu
print(list1 is list2) # False: car 2 objets différents en mémoire

print(id(list1))
print(id(list2))

list3 = list1

print(list3 is list1)

print(2 in list1)
print(5 in list2)

prenom = "sylvain" # une chaine est une collection de carcatères

print('v' in prenom)
print('syl' in prenom)

print(">>>>> Modules: math, statistics:")

import math,statistics

print(math.sqrt(16))
print(math.ceil(16)) # renvoie l'entier immédiatement supérieur

print(statistics.mean(list1))

print(math.pi)