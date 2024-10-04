import logging
import sqlite3
import sys
import os
import json

dossier_principal = os.getcwd()
sys.path.append(dossier_principal)

from myclasses.produit import Produit

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(filename)s - %(message)s",
    filename="app.log", # si fichier inexistant -> il sera crée par la fct
    filemode='a',
    encoding='utf-8',

    # formattage de la date
    datefmt="%d/%m/%Y - %H:%M"
)

CHEMIN_DATABASE = 'db.sqlite3'

def init(db_chemin):

    cnx = sqlite3.connect(db_chemin)
    curseur = cnx.cursor()

    try:

        curseur.execute("""
            CREATE TABLE IF NOT EXISTS produit(
            id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
            description varchar(30) NOT NULL,
            prix real NOT NULL                                  
            )

            """)
        
        # Insertion de données de test
        
        sql = 'insert into produit (id,description,prix) values (NULL,:description,:prix)'
        p1 = Produit(1,"PC Dell", 1500)
        p2 = Produit(2,"Ecran HP", 99)
        p3 = Produit(3,"Table", 45)

        curseur.execute(sql,{'id':p1.id, 'description':p1.description, 'prix':p1.prix})
        curseur.execute(sql,{'id':p2.id, 'description':p2.description, 'prix':p2.prix})
        curseur.execute(sql,{'id':p3.id, 'description':p3.description, 'prix':p3.prix})

        cnx.commit()
        logging.info('Table produit créée........')


    except Exception as e:
        logging.error(e)
        cnx.rollback()

    finally:
        curseur.close()
        cnx.close()



def get_all_produits(db_chemin):

    cnx = sqlite3.connect(db_chemin)
    curseur = cnx.cursor()

    produits = []
    try:

        
        
        sql = 'select * from produit'

        produits = curseur.execute(sql).fetchall()
        logging.info('Lecture de tous les produit OK')


    except Exception as e:
        logging.error(e)

    finally:
        curseur.close()
        cnx.close()

    return produits

def get_produit_by_id(db_chemin,id:int):

    cnx = sqlite3.connect(db_chemin)
    curseur = cnx.cursor()

    produit = None
    try:

        sql = 'select * from produit where id=?'

        resultat = curseur.execute(sql,(id,)).fetchone()


    except Exception as e:
        logging.error(e)

    else:
        if resultat:
            id,description,prix = resultat
            produit = Produit(id,description,prix)
            logging.info(f"Produit avec id = {id} trouvé.")
        else:
            logging.info(f"Produit avec id = {id} introuvable.")

    finally:
        curseur.close()
        cnx.close()

    return produit

def insert_produit(db_chemin,p:Produit):

    cnx = sqlite3.connect(db_chemin)
    curseur = cnx.cursor()
    try:

        sql = 'insert into produit (id,description,prix) values (NULL,:description,:prix)'

        curseur.execute(sql,{'id':p.id, 'description':p.description, 'prix':p.prix})
        cnx.commit()
        logging.info(f"Produit {p} inséré en base.")


    except Exception as e:
        logging.error(e)
        cnx.rollback()


    finally:
        curseur.close()
        cnx.close()

def update_produit(db_chemin,p:Produit):

    cnx = sqlite3.connect(db_chemin)
    curseur = cnx.cursor()
    try:

        sql = 'update produit set description=:description,prix=:prix where id=:id'

        curseur.execute(sql,{'id':p.id, 'description':p.description, 'prix':p.prix})
        cnx.commit()
        logging.info(f"Produit {p} maj en base.")


    except Exception as e:
        logging.error(e)
        cnx.rollback()


    finally:
        curseur.close()
        cnx.close()

def delete_produit(db_chemin,id:int):

    cnx = sqlite3.connect(db_chemin)
    curseur = cnx.cursor()
    try:

        sql = 'delete from produit where id=?'

        curseur.execute(sql,(id,))
        cnx.commit()
        logging.info(f"Produit avec id={id} supprimé")


    except Exception as e:
        logging.error(e)
        cnx.rollback()


    finally:
        curseur.close()
        cnx.close()

def export_all_produits_json(db_chemin):

    try:
        produits = get_all_produits(db_chemin)
        # Construction du contenu: list[dict]

        lst_dict = []
        for p in produits:
            d = {
                'id': p[0],
                'description': p[1],
                'prix': p[2]
            }

            lst_dict.append(d)

        chemin_json = os.path.join(os.getcwd(), 'produits.json')
        with open(chemin_json,'w',encoding='utf-8') as flux:
            json.dump(lst_dict,flux,indent=4,ensure_ascii=False)

        logging.info('Export json ok........')

    except Exception as e:
        logging.error(e)


# Test des fcts:

#init(CHEMIN_DATABASE)

#print(get_all_produits(CHEMIN_DATABASE))
#print(get_produit_by_id(CHEMIN_DATABASE,1))

#p = Produit(4,'new_Souris',55)
#update_produit(CHEMIN_DATABASE,p)
#delete_produit(CHEMIN_DATABASE,4)
#print(get_all_produits(CHEMIN_DATABASE))
#export_all_produits_json(CHEMIN_DATABASE)

    