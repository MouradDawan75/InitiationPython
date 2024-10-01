# Liste est une collection ordonnée avec doublons autorisés

#Syntaxe pour créer une liste vide:

lst = []
lst1 = list()

notes = [2,6,7,9]

print(notes)

# Modifications:

notes[0] = 9 # l'index commence à 0
print(notes)

# Ajouts:

# Types de bases: int, float,bool, str sont immuables
# Types complèxes (collections, dates, objet): sont immuables

notes.append(15)
print(notes)

notes.insert(1,15)
print(notes)

# Suppressions:

notes.remove(15)
print(notes)

notes.pop() # supprime le dernier élément par défaut
print(notes)

print(notes.index(6))
print(notes.count(9))

print(">>>>> Atteindre un élément d'une liste:")

print(f"Première note: {notes[0]}")

taille = len(notes)

print(f"Dernière note: {notes[taille - 1]}")

# Python autorise les indexs négatifs:

print(f"Dernière note: {notes[-1]}")
