from myclasses.produit import Produit
from repositories.produitrepository import get_all_produits,get_produit_by_id,insert_produit,delete_produit,update_produit,export_all_produits_json

CHEMIN_DATABASE = 'db.sqlite3'

while True:

    choix = input("""
        Choisir une opération:
        1- Afficher tous les produits
        2- Rechercher un produit par son id
        3- Insérer un produit
        4- Mettre à jours un produit
        5- Supprimer un produit
        6- Exporter la liste des produits dans un fichier json
        7 - Quitter
        """)

    if choix == '7':
     print('Fin du programme....')
     break

    match choix:
        case '1':
            produits = get_all_produits(CHEMIN_DATABASE)
            if produits:
                print(f"{len(produits)} trouvés.")
                print(produits)
            else:
                print('Aucun produit trouvé.')


        case '2':
            id = int(input('Id du produit: '))
            p = get_produit_by_id(CHEMIN_DATABASE,id)
            if p:
                print(p)
            else:
                print('Aucun produit trouvé.')

        case '3':
            description = input('Nom du produit: ')
            prix = float(input('Prix du produit: '))
            p = Produit(5000,description,prix)
            insert_produit(CHEMIN_DATABASE,p)
            print('Produit inséré.....')

        case '4':
            id = int(input('Id du produit: '))
            p = get_produit_by_id(CHEMIN_DATABASE,id)
            if p:
                description = input('Nom du produit: ')
                prix = float(input('Prix du produit: '))
                p = Produit(id, description,prix)
                update_produit(CHEMIN_DATABASE,p)
                print('Produit maj.....')

            else:
                print('Produit non trouvé.....')


        case '5':
            id = int(input('Id du produit: '))
            p = get_produit_by_id(CHEMIN_DATABASE,id)
            if p:
                delete_produit(CHEMIN_DATABASE,id)
                print('Produit supprimé....')
            else:
                print('Produit introuvable............')

        case '6':
            export_all_produits_json(CHEMIN_DATABASE)
            print('Export json ok.............')