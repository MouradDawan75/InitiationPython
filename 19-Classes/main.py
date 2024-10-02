from modelobjet import Vendeur,Technicien,Representant
from fonctions import insert,afficher_salaire_de_chaque_employe,afficher_tous_les_employes,salaire_moyen


while True:

    choix = input("""
                    Choisir une opération:
                            1- Afficher la liste des employés
                            2- Insérer un employé
                            3- Afficher le salaire de chacun des employé
                            4- Afficher le salaire moyen
                            5- Quitter

                    """)
    
    if choix == '5':
        print('Fin du programme.............')
        break

    match choix:
        case '1':
            afficher_tous_les_employes()

        case '2':
            employe = None
            nom = input('Nom: ')
            prenom = input('Prénom: ')
            age = int(input('Age: '))
            rep = input('Vender, Représentant ou Technicien ? tapez (v, r ou t)')
            if rep == 'v':
                ca = float(input('CA: '))
                employe =Vendeur(nom,prenom,age,ca)

            if rep == 'r':
                ca = float(input('CA: '))
                employe = Representant(nom,prenom,age,ca)

            if rep == 't':
                heures = float(input("Nombre d'heures: "))
                employe = Technicien(nom,prenom,age,heures)

            insert(employe)
            print('Employé inséré........')


        case '3':
            afficher_salaire_de_chaque_employe()

        case '4':
            print(f"Le salaire moyen est: {salaire_moyen()}")