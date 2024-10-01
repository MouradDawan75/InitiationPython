# Tuple est une collection ordonnée avec doublons autorisés. Il s'agit d'une liste en lecture (non modifiable)
# 
# Syntaxe pour créer un tuple vide:

t = ()
t1 = tuple() 

prenoms = ("Marc","Jean","David","Dawan")
print(prenoms.count('David'))
print(prenoms.index('David'))

#prenoms[0] = "Dawan"

# Eclatemene t d'un tuple: Extraction des éléments d'un tuple

p1,p2,*reste = prenoms
print(p1)
print(p2)
print(reste) # reste est une liste

# Modification d'un tuple:

#1- Conversion en liste:

lst = list(prenoms)
lst.append("Paris")
lst.remove("Dawan")

#2- Revenir au tuple:
prenoms = tuple(lst)
print(prenoms)


