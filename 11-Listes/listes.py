# Liste est une collection ordonnée avec doublons autorisés

#Syntaxe pour créer une liste vide:

lst = []
lst1 = list()

notes = [2,6,7,9]

print(notes)

# Modifications:

notes[0] = 9 # l'index commence à 0
print(notes)

# Ajouts: focntions append - insert

# Types de bases: int, float,bool, str sont immuables
# Types complèxes (collections, dates, objet): sont immuables

notes.append(15)
print(notes)

notes.insert(1,15)
print(notes)

# Suppressions: remove(element), pop(index)

notes.remove(15)
print(notes)

notes.pop() # supprime le dernier élément par défaut
print(notes)

print(notes.index(6))
print(notes.count(9))

print(">>>>> Atteindre un élément d'une liste:")

# L'index commence à 0 par défaut: 0,1...... n-1

print(f"Première note: {notes[0]}")

taille = len(notes)

print(f"Dernière note: {notes[taille - 1]}")

# Python autorise les indexs négatifs:
# Dans le sens inverse :'index commence à -1,-2.... en partant du dernier de la liste

print(f"Dernière note: {notes[-1]}")

print(">>>>> Parcourir une liste:")

notes = [2,6,7,9]

print(">> FOR:")

for e in notes:
    print(e)

print('>> WHILE:')

taille = len(notes)
index = 0

while index < taille:
    print(notes[index])
    index += 1

print(">> FOR + INDEX:")

for i in range(len(notes)):
    print(notes[i])

print(">>>>>>> Slicing:")

# Slicing: mécanisme qui permet de créer des sous listes à partir de listes existantes

prenoms = ['Julien','Marine','Louis','Aya']

list1 = prenoms[0:3] # de index 0 inclus à 2 (n - 1)
print(list1)

list2 = prenoms[:3] # du début jusqu'à index 2 (n-1)
print(list2)

list3 = prenoms[:] # du début jusqu'à la fin (une copie)
print(list3)

list4 = prenoms[0:4:2] # de index 0 à index 3 avec un pas 2
print(list4)

list5 = prenoms[::2] # du début jusqu'à la fin avec un pas de 2
print(list5)

print(">>>>> Comprehension List:")

# Liste en compréhension: mécanisme  permettant de créer de nouvelles à partir de listes existantes en modifiant 
# leur contenu

nombres = range(10)

# Créer une nouvelle liste en doublant tous les éléments de la liste de départ
# Syntaxe classique:
liste_doubles = []

for e in nombres:
    liste_doubles.append(e * 2)

# Syntaxe comprehension list:

nombres_doubles = [e * 2 for e in nombres]
print(nombres_doubles)

nombres = range(10)

# Nouvelle iste ne contenant que les nombres impairs

nombres_impairs = [e for e in nombres if e % 2 != 0]
print(nombres_impairs)

# On peut aussi utiliser des fonctions:

nombres = range(10)

# Nouvelle liste contenant tous les élements au carré

def carre(x:int):
    return x ** 2

nombres_carres = [carre(e) for e in nombres]
print(nombres_carres)

print(">>>>> Multiples conditions:")

nombres = range(10)

# Nouvelle liste ne contenant que les nombres pairs supérieurs à 4

resultat = [e for e in nombres if e % 2 == 0 and e > 4]
print(resultat)

# Autre syntaxe possible permettant de remplacer les opérateurs logiques par de if

resultat2 = [e for e in nombres if e % 2 == 0 if e > 4] # aucune limite sur e nombre de if à utiliser
print(resultat2)

print(">>>>> random pour les listes:")

from random import choice, choices, sample, shuffle

cartes = [x for x in range(1,11)]
print(cartes)

print(">>>choice: élément aléatoire")

print(choice(cartes))

print(">>>>choices: sous liste aléatoire")

print(choices(cartes,k=5))

print(">>>>sample: sous liste aléatoire")
print(sample(cartes,3))

print(">>>>shuffle: mélanger les éléments d'une liste")
shuffle(cartes)
print(cartes)