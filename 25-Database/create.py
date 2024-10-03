
# Etape1:
import sqlite3

# Quelque soit le type de BD utilisé, il ya 3 étapes à effectuer:
# 1- installer le connecter (module externe de Python) pip install nom_connecter
# 2- Appeler la fonction connect(param de connexion)
# 3- Récupérer le stream en appelant la fct cursor()

# Etape2:
cnx = sqlite3.connect('25-Database/db.sqlite3') # si fichier inexistant -> il est crée par la fct

# Etape3:
curseur = cnx.cursor()

# Exécution des commandes SQL:
# 2 types de commanes SQL:
# Commandes LDD: Langage de définition de données (concerne la structure de la BD): CREATE - DROP - ALTER
# Commandes LMD: Langage de manipulation de données: SELECT - INSERT - DELETE - UPDATE

#CONSTRAINT email_unique UNIQUE email

curseur.execute("""
CREATE TABLE IF NOT EXISTS person(
  id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  nom varchar(30) NOT NULL,
  prenom varchar(30) NOT NULL,
  age int unsigned NOT NULL,
  CONSTRAINT unique_names UNIQUE (nom,prenom)
                                          
)

""")

# Insertion de données de test:
# Les opérations d'écriture s'exécutent en mode transactionnel

try:

    curseur.execute("INSERT INTO person(nom,prenom,age) VALUES ('DUPONT', 'Jean', 60)")

    # Dans la pratique il est recommander d'utiliser des commandes SQL paramétrées:
    # c'est une protection contre les injections SQL
    # Une commande SQL paramétrée est pré-compilée, chargée en mémoire en attente de params

    curseur.execute("INSERT INTO person values(NULL,?,?,?)",('CONNERY','Sean',75))
    curseur.execute("INSERT INTO person values(NULL,?,?,?)",('BOUQUET','Carole',48))

    cnx.commit() # commit() -> valide toutes les commandes sql

except Exception as e:
    print(e)
    cnx.rollback() # rollback() -> annule toutes les commandes SQL

finally:
    curseur.close()
    cnx.close()

# Pour afficher le contenu d'un DB sqlite:
# Soit installer un client externe (sqlite browser)
# Soit ajouter dans VS Code l'extension sqlite viewer

