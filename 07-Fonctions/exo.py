#1)

def somme_liste(entiers:list[int]) -> int:

    s = 0
    for e in entiers:
        s += e

    return s

print(somme_liste([10,20,30]))

#2)

def moyenne_liste(entiers:list[int]) -> float:

    somme = somme_liste(entiers)

    nb_elements = 0
    for e in entiers:
        nb_elements += 1

    return somme / nb_elements

print(moyenne_liste([1,2]))

#3) 
def min_liste(entiers:list[int]) -> int:

    minimum = entiers[0]
    for e in entiers:
        if e < minimum:
            minimum = e

    return minimum

print(min_liste([10,1,15,6,3]))

#4)

def table_multiplication(nombre:int, premier_mutiple:int, dernier_multiple:int) -> None:
    for i in range(premier_mutiple, dernier_multiple + 1):
        print(f"{nombre} x {i} = {nombre * i}")
    
table_multiplication(11,1,13)

#5)

def convertir_minutes_en_heures(minutes:int):
    print(f"{minutes}m = {minutes // 60}h {minutes % 60}m")

def convertir_heures_en_minutes(heures:int):
    print(f"{heures}h = {heures * 60}m")

def demander_saisie_nombre_valide(message:str) -> int:
    while True:
        nb = input(message)
        try:
            nb = int(nb)
            return nb # return fonctionne comme un break

        except:
            print('Nombre invalide.......')


def afficher_menu() -> str:

      choix = input("""

 Votre choix: 
  1) Convertir heures en minutes -> Ex: nombre saisi 90 -> affichez 90m = 1h 30m
  2) Convertir minutes en heures -> Ex: nombre saisi 6 -> affichez 6h = 180m
  3) Quitter
                  
""")
      
      return choix




while True:

    choix = input("""

 Votre choix: 
  1) Convertir heures en minutes -> Ex: nombre saisi 90 -> affichez 90m = 1h 30m
  2) Convertir minutes en heures -> Ex: nombre saisi 6 -> affichez 6h = 180m
  3) Quitter
                  
""")
    
    if choix == '3':
        break

    if choix == '1':

        minutes = int(input('Nombre de minutes: '))
        print(f"{minutes}m = {minutes // 60}h {minutes % 60}m")

    if choix == '2':
        heures = int(input("Nombres d'heures:" ))
        print(f"{heures}h = {heures * 60}m")


# Code optimisé:

while True:

    choix = afficher_menu()
    if choix == '3':
        break

    if choix == '1':

        minutes = demander_saisie_nombre_valide('Nombre de minutes: ')
        convertir_minutes_en_heures(minutes)

    if choix == '2':
        heures = demander_saisie_nombre_valide("Nombre d'heures: ")
        convertir_heures_en_minutes(heures)
            

