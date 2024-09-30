#1)
for i in range(11):
    if i != 0:
        print(i)

# sol2

for i in range(10):
    print(i+1)

# sol3: on peut aussi modifier l'index de départ qui commence à 0 par défaut

for i in range(1,11):
    print(i)

#2)
for i in range(1,11):
    if i % 2 == 0:
        print(i)

# sol2: on peut aussi modifier le pas qui est égale à 1 par défaut

for i in range(2,11,2):
    print(i)

# 3) 

while True:
    choix = input("""
        Menu:
        Votre choix:
        1) Convertir minutes en heures
        2) Quitter

        """)
    if choix == '2':
        break

    if choix == '1':
        minutes = int(input('Nombre de minutes: '))
        print(f"{minutes}m = {minutes // 60}h {minutes % 60}m")


#4)

while True:
    operation = input(""""

    Choisir une opération:
    - Addition: tapez a
    - Soustraction: tapez s
    - Multiplication: tapez m
    - Division: tapez d
    - Quitter: tapez q

    """)

    if operation == 'q':
        break

    if operation not in  'asmd': #['a','s','m','d']:
        print('Choix invalide')
        continue

    nb1 = float(input('Premier nombre: '))
    nb2 = float(input('Second nombre: '))

    match operation:
        case 'a':
            print(f"{nb1} + {nb1} = {nb1 + nb2}")

        case 's':
            print(f"{nb1} - {nb1} = {nb1 - nb2}")

        case 'm':
            print(f"{nb1} x {nb1} = {nb1 * nb2}")

        case 'd':
            print(f"{nb1} / {nb1} = {nb1 / nb2}")