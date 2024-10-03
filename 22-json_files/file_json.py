import os
import json

# Contrairement à un fichier texte, un fichier json en plus du texte contient des données 
# (chaines, listes, dict, valeurs numériques......)

# Etape1 : construction du chemin du fichier à manipuler

chemin_dossier = os.path.dirname(__file__)
chemin_json = os.path.join(chemin_dossier,'users.json')

# Etape 2 : appel de la fct open

# Lecture d'un fichier json:

with open(chemin_json,'r', encoding='utf-8') as flux:
    contenu = json.load(flux)

#print(contenu) -> il s'agit d'une liste de dictionnaires

for user in contenu:

    print(f"Name: {user.get('name')}")
    print(f"Latitude: {user.get('address').get('geo').get('lat')}")
    print("==============================")


# Ecriture dans un fichier json:

chemin_fichier_json = os.path.join(chemin_dossier, 'sortie.json')

with open(chemin_fichier_json,'w',encoding='utf-8') as flux:

    # Le contenu à fournir doit être un dict ou une liste de dict
    donnee = {
        "python": "Langage de programmation",
        "version": 3.12
    }

    json.dump(donnee,flux,indent=4,ensure_ascii=False) # ensure_ascii=True -> tous les caractères non ascii seront ignorés

# Exo: à partir de users.json, construire un fichier json (resultat.json) ne contenant que username et email

# Contenu doit être une liste de dictionnaires

lst = []

for u in contenu:
    d = {
        'username': u.get('username'),
        'email': u.get('email')
    }

    lst.append(d)

chemin_resulat = os.path.join(chemin_dossier,'resulat.json')

with open(chemin_resulat, 'w', encoding='utf-8') as flux:

    json.dump(lst, flux, indent=4, ensure_ascii=False)

# Solution2: utilisation d'une classe

class Utilisateur:

    def __init__(self,username,email) -> None:
        self.username = username
        self.email = email

    # Permet de choisir les attributs à inclure dans le dictionnaire
    # __dict__: inclue tous les attributs

    def convert_to_dict(self):
        d = {
            'username': self.username
        }

        return d


liste_dict = []

for user in contenu:
    u = Utilisateur(user.get('username'), user.get('email'))
    liste_dict.append(u.__dict__)

chemin_resultat2 = os.path.join(chemin_dossier,'resultat2.json')

with open(chemin_resultat2, 'w', encoding='utf-8') as flux:
    json.dump(liste_dict,flux,indent=4,ensure_ascii=False)


ut = Utilisateur('admin','admin@dawan.fr')

print(ut.__dict__)
print(ut.convert_to_dict())
