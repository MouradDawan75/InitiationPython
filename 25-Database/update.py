import sqlite3

cnx = sqlite3.connect('25-Database/db.sqlite3')

curseur = cnx.cursor()

# Commade sql paramétrée avec des params nommés
sql = 'UPDATE person set nom=:last_name,prenom=:fisrt_name,age=:age where id=:id'

# Pour les params nommés: utilisez un dictionnaire

params = {
    'last_name': 'new_nom',
    'fisrt_name': 'new_prenom',
    'age': 99,
    'id': 1
}

curseur.execute(sql,params)
cnx.commit()
curseur.close()
cnx.close()