import random

aleatoire = random.randint(1, 100)
TENTATIVE_MAX = 6
nb_tentative = 0

while True:

    nombre = input('Votre nombre: ')
    
    try:
        nombre = int(nombre)
        nb_tentative += 1

        if nombre == aleatoire:
            print(f"Trouvé en {nb_tentative} tentatives. Aléatoire = {aleatoire}")
            break

        if nb_tentative == TENTATIVE_MAX:
            print(f"Perdu! Aléatoire = {aleatoire}")
            break

        if nombre < aleatoire:
            print('Supérieur')
        else:
            print('Inférieur')

    except:
        print('Nombre invalide......')

print("Fin du programme...........")

# Solution2 -> Nombre d'itérations = 6: boucle for

for i in range(6):

    nombre = input('Votre nombre: ')
    
    try:
        nombre = int(nombre)

        if nombre == aleatoire:
            print(f"Trouvé en {nb_tentative} tentatives. Aléatoire = {aleatoire}")
            break

        if nombre < aleatoire:
            print('Supérieur')
        else:
            print('Inférieur')

    except:
        print('Nombre invalide......')
