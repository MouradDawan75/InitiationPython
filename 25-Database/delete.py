import sqlite3

cnx = sqlite3.connect('25-Database/db.sqlite3')

curseur = cnx.cursor()

sql = 'delete from person where id=?'
param = (3,)

curseur.execute(sql,param)
cnx.commit()
curseur.close()
cnx.close()

