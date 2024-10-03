import sqlite3

cnx = sqlite3.connect('25-Database/db.sqlite3')

curseur = cnx.cursor()

sql = 'insert into person values (NULL,:nom,:prenom,:age)'

# params nommés -> dictionnaire

d = {
    'nom': 'DAWAN',
    'prenom': 'Jehann',
    'age': 20
}

curseur.execute(sql,d)
cnx.commit()
curseur.close()
cnx.close()