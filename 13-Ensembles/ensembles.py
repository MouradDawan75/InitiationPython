# Ensemble (set) est une collection non ordonnée sans doublons. De plus, le type set supporte les opérations
# sur les ensembles, telles l'union, l'intersection, la différence et la différence symétrique

# Syntaxe pour créer un ensemble vide:
e = set()

panier = {"pomme","orange","pomme","banane"}
print(panier)


a = set('abracadabra') # conversion d'une chaine en set
b = set('alacazam')

print(a)
print(b)

print(">>> Union:")
# Lettres dans a ou dans b ou dans les 2
# 2 syntaxes:

print(a | b)
print(a.union(b))

print(">>> Intersection:")
# Lettres dans a et dans b
# 2 syntaxes:

print(a & b)
print(a.intersection(b))

print(">>>> Différence:")
# Lettre dans a mais pas dans b
# 2 syntaxes:
print(a - b)
print(a.difference(b))

print(">>>> Difference symétrique:")
# Lettres dans a ou dans b mais pas dans les 2 
# 2 syntaxes:
print(a ^ b)
print(a.symmetric_difference(b))

print(">>>>> Ensemble en compréhension:")

ensemble = set('abracadabra')
print(ensemble)

# Nouvel ensemble ne contenant que les lettres différentes de a,b et c

# Syntaxe classique:
resultat = set()

for lettre in ensemble:
    if lettre not in 'abc':
        resultat.add(lettre)




# Syntaxe Ensemble en compréhension:
new_set = {lettre for lettre in ensemble if lettre not in 'abc'}
print(new_set)

# Suppression des doublons dans une liste

lst = [1,1,2,2,3,3]
lst = set(lst) # conversion en set pour supprimer les doublons
lst = list(lst) # conversion en liste
print(lst)