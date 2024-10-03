import sqlite3

cnx = sqlite3.connect('25-Database/db.sqlite3')

curseur = cnx.cursor()

print(">>>> select * from person")

# * pour prendre toutes les colonnes

sql = "select * from person"
curseur.execute(sql)
personnes = curseur.fetchall()

print(personnes) # c'est liste de tuples -> chaque ligne de la table est convertie en tuple

for p in personnes:
    print(p) # p est un tuple

# Eclater le tuple p:

for id,nom,prenom,age in personnes:
    print(f"ID: {id} - Nom: {nom} - Prénom: {prenom} - Age: {age}")

print(">>> Nouvelle lecture du curseur:")
print(curseur.fetchall()) # Une fois le contenu du curseur consommé (ligne 13), ce dernier est réinitialisé par Python

print(">>>> select nom,prenom from person")

sql = 'select nom,prenom from person'

curseur.execute(sql)
print(curseur.fetchone()) # ligne supprimée dans le curseur
print(curseur.fetchone()) # ligne supprimée dans le curseur
print(curseur.fetchone()) # ligne supprimée dans le curseur
print(curseur.fetchone()) # curseur vide

print(">>>> select * from person where id=?")

sql = 'select * from person where id=?'

param = (1,)
print(type(param))
curseur.execute(sql,param)
print(curseur.fetchone())

print(">>> select * from person where nom like ?")

sql = 'select * from person where nom like ?'

# n% -> les noms qui commence par n
# %n -> les noms se terminant par n
# %n% -> tous es nom contenant n quelque soit sa position dans le nom

param = ["%b%"]

curseur.execute(sql,param)

print(curseur.fetchall())