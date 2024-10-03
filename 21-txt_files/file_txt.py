
import os # permet la gestion des paths

# ######################Etape1: construire le chemin du fichier

#chemin_fichier = 'c:\.....\demo.txt'

chemin_dossier = os.path.dirname(__file__) # c:\......\21-txt_files

#print(chemin_dossier)

#chemin_fichier = chemin_dossier+'\\myfile.txt'

# join: génère un chemin valide selon l'os utilisé (Windows,Mac ou Linux)
chemin_fichier = os.path.join(chemin_dossier, 'myfile.txt') 

########################## Etape2: appeler la fonction open()
# Elle prend plusieurs paramètres:
# - chemin du fichier
# - Mode d'accès au fichier: r: read - w: write - a: append -> pour un accès en écriture (w,a)
#         si fichier inexistant -> il seré crée par la fonction open
# - encoding = 'utf-8

# Obligation: une ressource doit être libérée à la fin de son utilisation

# Ecriture dans un fichier

flux = open(chemin_fichier, 'a', encoding='utf-8')
flux.write('\nceci est le contenu du fichier')
flux.close()

# Lecture d'un fichier

flux = open(chemin_fichier,'r', encoding='utf-8')
contenu = flux.read()
flux.close()

print(contenu)

print(">>>>>>>>>>>>>>>>>>>> Context Manager:")
# Context Manager (with resource): s'occupe de libérer la ressource à la fin de son utilisation

with open(chemin_fichier,'r', encoding='utf-8') as file:
    contenu = file.read() # vous arrivez à la fin du fichier, la prochaine lecture n'aura aucune ligne à lire
    # file.close() -> ligne exécutée par le with
    print(contenu)
    print(">>>>> Autre lecture:")
    file.seek(0) 
    # seek: permet de remettre le curseur au début du fichier
    # seek(5): renvoie le 5ème caractère
    # whence = 0: partir du début du fichier
    # whence = 1: partir de la position actuelle du curseur
    # whence = 2: partir de la fin du fichier

    print(file.read())
    print(">>>> Fin lecture")


#print(file.read())

print(">>>>>>>>>>>>>>>>>>>>> seek:")

with open(chemin_fichier,'r', encoding='utf-8') as file:
    contenu = file.read(8) # lecture des 8 premiers caractères
    print(contenu)

    file.seek(4)

    contenu_suivant = file.read(8)
    print(contenu_suivant)

print(">>>>>>>>>>>>>>>>> Test des fonctions de lecture et ecriture définies dans mytools-> filetool:")

# Ajout chemin dossier principal dans sys.path

import sys

chemin_dossier_principal = os.path.dirname(chemin_dossier)
sys.path.append(chemin_dossier_principal)

from mytools.filetool import lecture_fichier_texte, ecriture_fichier_texte

chemin_fichier = os.path.join(chemin_dossier, 'demo.txt')

ecriture_fichier_texte(chemin_fichier, 'contenu de demo.txt', mode_append=True)

print(lecture_fichier_texte(chemin_fichier))

print(">>>>>>>>>>>>>>>>> Module OS:")


dossier_principal = os.getcwd() # Get Current Working Directory
print(dossier_principal)

# Créer un dossier:

chemin_rep = os.path.join(chemin_dossier, 'dossier')

if os.path.exists(chemin_rep):
    print('Dossier existant...')
else:
    os.mkdir(chemin_rep)
    print('Dossier crée....')

print(">>>>> Lister le contenu d'un répertoire:")

for f in os.listdir(chemin_dossier):
    print(f)

# Exo: Parcourir le dossier en cours, lire tous les fichiers .txt et sauvegarder le contenu dans nouveau fichier new.txt
# Le contenu de new.txt doit ressembler à ça:
# >>>>> nom du fichier trouvé
# contenu du fichier lu

chemin_nouveau_fichier = os.path.join(chemin_dossier,'new.txt')

contenu = ''

for f in os.listdir(chemin_dossier):

    if f.endswith('.txt'):
        chemin = os.path.join(chemin_dossier,f)
        with open(chemin,'r', encoding='utf-8') as flux:
            contenu += ">>>> fichier: "+f+'\n'+flux.read()+"\n"


if contenu:
    with open(chemin_nouveau_fichier,'w', encoding='utf-8') as flux:
        flux.write(contenu)

else:
    print('Aucun fichier trouvé.....')




