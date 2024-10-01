# Dict: est une collection non ordonnée qui fonction par association clé:valeur.
# Dans un dictionnaire physique, le mot est la clé, sa définition est la valeur.
# Dans un dict Python les clés sont unique

# Synatxe pour créer un dict vide:

d = dict()
d1 = {}

# Un dict peut être utilisé pour regrouper les caractéristiques d'un objet

user = {
    'nom': 'DUPONT',
    'prenom': 'Jean',
    'age': 65
}

print(user['nom'])
#print(user['Nom']) -> si clé inexistante -> exception

print(user.get('nom'))
print(user.get('Nom')) # si clé inexistante -> renvoie None

# On peut aussi avoir un dictionnaire complèxe:

utilisateur = {
    'nom': 'DUPONT',
    'prenom': 'Jean',
    'age': 65,
    'telephones': ['06060606','07070707'],
    'adresse': {
        'rue': '15 rue Machin',
        'code_postal': 75015
    }
}

# Afficher chaque numéro de tél:
for t in utilisateur.get('telephones'):
    print(t)

# Afficher la rue:
print(utilisateur.get("adresse").get('rue'))

utilisateur['contrat'] = 'CDD' # si clé inexistante -> elle est créée
print(utilisateur)

utilisateur['contrat'] = 'CDI' # si la clé existe -> elle est écrasée
print(utilisateur)

# API Rest (Web Service Rest): un ensemble de ressources (images, article d'un journal...) où chaque ressource
# possède un ID (URI: Uniform Resource Identifier - End Point), une méthode d'accès (GET-POST-DELETE-PUT) et elle 
# peut être publique ou privée.

# Toutes ces infos sont fournies dans la documentation de l'api
# Une API Rest n'est pas limitée au format. Elle peut renvoyée du xml, texte, fichier......

print(">>>>> Appel d'une API Rest")

# On doit installer le module requests
# pip : gestionnaire des modules externes
# pip install nom_module
# pip uninstall nom_module
# pip list
# pip install requests

# import requests

# URI = "https://restcountries.com/v3.1/all"

# reponse = requests.get(URI).json()

# # print(reponse) -> liste de dictionnaires

# country = input("Votre pays: ")

# for pays in reponse:
#     if country == pays.get('name').get('common'):
#         print(f"Nom: {pays.get('name').get('common')} - Capitale: {pays.get('capital')}")

print(">>>> Parcourir un dictionnaire: ")

d = {
    'a': 1,
    'b': 2
}

# Par défaut, le for renvoie uniquement les clés du dictionnaire:
print(">>> For par défaut:")
for e in d:
    print(e)


# For explicite sur les clés
print(">>> For sur les clés:")
for cle in d.keys():
    print(f"Clé: {cle} - Valeur: {d.get(cle)}")


# For explicite sur les valeurs du dict:
print(">>> For sur les valeurs:")
for v in d.values():
    print(v)

print(">>> For sur les items:")
for i in d.items():
    print(i) # i est un tuple (clé, valeur)


# Eclater le tuple:

for k,v in d.items():
    print(f"Clé: {k} - Valeur: {v}")

print(">>>> Dictionary Comprehension:")

# Construire de nouveaux dict à partir de dict existants

d = {
    'a':1,
    'b':2
}

# Construire un dict en inversant les clés et les valeurs

result = {v:k for k,v in d.items()}
print(result)

# Autre synatxe:

result1 = {(v,k) for k,v in d.items()}
print(result1)

nombres  = range(10)

# Construire un dict dont les clés sont les nombres pairs et les valeurs dont les clés puissances 2

r = {n: n ** 2 for n in nombres if n % 2 == 0}

# Multiples conditions:

d = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5
}

# Nouveau dict avec les valeurs supérieures à 2 et paires

new_dict = {k:v for k,v in d.items() if v % 2 == 0 if v > 2}
print(new_dict)


