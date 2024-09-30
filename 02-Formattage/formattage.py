age = 30
prenom = 'Alex'

# Concaténation: on doit faire des conversion en str de tous les variables non str

print("Prénom: "+prenom+" Age: "+str(age))

# Utiliser une virgule comme séparateur:
# La virgule génère un éspace et n'impose pas de conversions en str

print("Prénom:",prenom,"Age:",age)

# A partir de Python 3: ajout de la fonction format string

print("Prénom: {} Age: {}".format(prenom,age))

# A partir de Python 3.6: fstring -> syntaxe simplifiée de la fonction format

print(f"Prénom: {prenom} Age: {age}")

# Entre accolades, on peut soit ajouter des variables, soit des expressions

print(f"{3 + 5}")  # expression

print(">>>>> Chaines multilignes:")

print("""
    ceci est une
chaine sur
plusieurs ligne.

""")

print(">>>> Caractères d'échappement:")

# \n: retour à la ligne
# \t: tabulation
# \s: space
# \b: back space
# \\: ignorer le \
# \'
# \"

print("\tceci est une\nchaine sur\nplusieurs lignes.")

chemin = "c:\\test\\notes.txt"

chaine = "ceci est \"une\" chaine"

print(chaine)