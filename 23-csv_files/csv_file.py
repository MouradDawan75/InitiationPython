import os
import csv

chemin_dossier = os.path.dirname(__file__)

chemin_csv = os.path.join(chemin_dossier,'demo_file.csv')

# Lecture d'un csv:

contenu = []

with open(chemin_csv,'r',encoding='utf-8') as flux:
    curseur = csv.reader(flux,delimiter=',')
    # reader est une sorte de curseur vers toutes les lignes du fichiers

    for ligne in curseur:
        contenu.append(ligne)


print(contenu) # contenu est une liste de listes, où chaque liste correspond à une ligne du fichier csv

# Ecriture dans fichier csv:

chemin_fichier = os.path.join(chemin_dossier, 'copie.csv')

# Le contenu doit être une liste de listes, où chaque liste est convertie en ligne dans le fichier csv

with open(chemin_fichier,'w', encoding='utf-8') as file:
    curseur = csv.writer(file, delimiter=';', lineterminator='\n')

    # Soit une insertion ligne/ligne: writerow
    for ligne in contenu:
        curseur.writerow(ligne)

    # Soit insérer toutes les lignes en une seule opération: writerows()
    #curseur.writerows(contenu)

print(">>>>>>>>>>>>>>>> Analyse d'un fichier csv:")

chemin_csv = os.path.join(chemin_dossier, 'deces_usa.csv')

with open(chemin_csv,'r', encoding='utf-8') as flux:
    curseur = csv.reader(flux)
    data = list(curseur)

print(">>>> les 5 premières lignes:")

print(data[:5])

# Suppression de l'entête:
headers = data[:1]
data = data[1:]

print(headers)

print(">>>> Nombre de décès par année:")

years = [e[1] for e in data]

years_counts = {}

for y in years:

    # Créer la clé 1 seule fois
    if y not in years_counts:
        years_counts[y] = 0

    #A chaque passage on incrémente
    years_counts[y] += 1

print(years_counts)