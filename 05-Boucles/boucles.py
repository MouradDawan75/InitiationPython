print(">>>>> Bloc itératif")
# 2 types de bloc itératifs:
# Si on connait le nombre d'itérations: on utilise la boucle for
# Si on connait pas le nombre d'itérations, et que le boc dépend d'une condition, on utilise la boucle while
# 
# For: permet de parcourir tous les éléments d'une collection
# While (boucle conditionnelle): permet de réexecuter le bloc d'instructions tant qu'une condition est vérifiée 

#### For:
nombres = range(10) # renvoie une collection de int allants de 0 à 9 (n - 1)

for e in nombres:
    if e == 5:
        break
    print(e)

prenom = "Marc"
for lettre in prenom:
    print(lettre)

#### While:

x = 1

while x < 5:
    print(f"x = {x}")
    if x == 3:
        break
    x += 1

print(">>>> break, continue:")

prenom = "sylvain"

for lettre in prenom:

    if lettre == 'y':
        continue # force le passage à l'itération suivante - la suite de la boucle n'est pas exécutée

    if lettre == 'i':
        break

    print(lettre) # slva

