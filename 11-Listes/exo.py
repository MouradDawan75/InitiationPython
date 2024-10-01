# 1) 
# Nouvelle liste ne contenant que les 
# nombres positifs

nombres = range(-10,10)

nombres_positifs = [e for e in nombres if e > 0]# Pour un if seul, le for arrive en premier
print(nombres_positifs)

# 2) 
# Nouvelle liste en inversant uniquement les 
# nombres impairs. Résultat [0,-1,2,-3,4......]

nombres = range(10)

nombres_inverses = [e if e % 2 == 0 else -e for e in nombres] # Pour un if/else, le for arrive en dernier
print(nombres_inverses)

# 3)
# Affichez le nombre d'éléments supérieurs à 3 
# (Comprehension List)
lst = [1,5,3,7,9]
print(len([e for e in lst if e > 3]))

# Sol2:
print(sum(1 for e in lst if e > 3))

#4)
# Affichez la différence entre ces 2 liste (listA - listB)
listA = [1,2,3,4]
listB = [1,2]

difference = [e for e in listA if e not in listB]
print(difference)

# 5)
# Définir une fonction qui prends en paramètre une liste 
# d'entiers et qui renvoie la somme des entiers 
# pairs distincts
# Ex: lst = [2,3,2,2,4,6,4] -> résulat attendu = 12

def somme_pairs_distincts(entiers:list[int]) -> int:

    # Construire une liste ne contenant que les nombres pairs distincts
    # lst = [e for e in entiers if e != 0 and e not in lst] -> Exception car lst n'existe pas encore
    # Solution: utiliser la syntaxe classique
    lst = []
    for e in entiers:
        if e % 2 == 0 and e not in lst:
            lst.append(e)

    return sum(lst)

print(somme_pairs_distincts([2,3,2,2,4,6,4]))

