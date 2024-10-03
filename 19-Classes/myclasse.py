# Approche procédurale: repose sur l'utilisation de paramètres et de fonctions
# Approche objets: repose sur l'utilisation de classes et d'objets

# C'est une approche de résoution de problèmes algorithmétique permettant de produire des programmes modulaires.

# Objectifs:
# - Développer de l'application sans qu'il soit nécessaire de connaitre es détails internes des autres partie
# - Réutiliser des fragmements de codes dans un cadre différents
# - Apporter des modifications à un module sans que cela n'affètre le reste du programme

# Objet: est élément identifiable du monde réel: abstrait ou concrèt
# - possède une identité
# - un état: les propriété de l'objet
# - un comportement: les fonctions de l'objet

# Classe: est un type de donnée, dont la tâche principale est de décrire la structure d'un objet. Elle définie de 
# tempate à partir duquel on crée nos objet

# Elle contient généralement 3 éléments:
# - attributs (propriété)
# - fonctions
# - fonction spéciale qui porte le nom de la classe appelée constructeur (initialisateur), permettant d'instancier
# la classe en question.

class User:

    # Attributs de classe: partagés par tous les objets
    profil = 'admin'


    # Attributs d'instance
    def __init__(self,nom:str,prenom:str):
        # self: mot clé qui pointe vers l'objet en cours d'utilisation
        self.nom = nom
        self.prenom = prenom
        print('>>>> init <<<<<<<')

    # fonction d'instance: concerne une instance particulière
    def afficher_nom(self):
        print(self.nom)

    @classmethod
    def modifier_profil(cls, new_profil):
        cls.profil = new_profil
        




# User.__init__(u, 'DUPONT','Jean') -> code exécuté par Python en arrière plan
u = User('DUPONT','Jean')

u.afficher_nom()

u1 = User('NOM_U1', 'Prenom_u1')
u1.afficher_nom()

print(u.profil)
print(u1.profil)

print(User.profil) # Les attributs sont accéssibles via la classe

User.modifier_profil('RH') # les méthodes de classes, sont appelées à partir de la classe

print(u.profil)
print(u1.profil)

class CompteBancaire:

    banque = 'BNP'


    def __init__(self,numero,solde) -> None:
        self.numero = numero
        self.solde = solde

    def depot(self,montant):
        self.solde += montant

    def retrait(self, montant):
        if self.solde >= montant:
            self.solde -= montant
        else:
            print('Solde insuffisant.......')

    @classmethod
    def changer_banque(cls, nom_banque):
        cls.banque = nom_banque


    # fonction qui permet de personaliser l'affichage des objets: choisir les attributs à afficher
    def __str__(self) -> str:
        return f"Numéro: {self.numero} - Solde: {self.solde}"
    
    # permte de vérifier l'égalité de objets
    def __eq__(self, other) -> bool:
        return self.numero == other.numero
    
    # En cas de besoin, on peut ajouter ces fonctions:
    def __ne__(self, value: object) : pass # Not Equal !=
    def __lt__(self, value: object) : pass # Less Than <
    def __le__(self, value: object) : pass # Les Equal <=
    def __gt__(self, value: object) : pass # Greater Than >
    def __ge__(self, value: object) : pass # Greater Equal >=


cpt1 = CompteBancaire('sdqsd15', 1000)
cpt2 = CompteBancaire('rter59', 999)

print(cpt1.banque)
print(cpt2.banque)

CompteBancaire.changer_banque('LCL')

print(cpt1.banque)
print(cpt2.banque)

cpt1.depot(500)
print(cpt1.solde)

cpt1.retrait(15000)

print(cpt2)

compte1 = CompteBancaire('sqdqsd15', 1500)
compte2 = CompteBancaire('sqdqsd15', 150000000)

print(compte1 == compte2)

# Exo: A la racine du projet principal:
# Créez un package nommé myclasses contenant le module produit dans lequel on crée la classe Produit
# Un produit possède un id, une description et un prix
# On souahite afficher tous les attributs d'un produit
# 2 produits sont égaux si les 2 possèdent le mm id

# Importez et testez cette classe dans le module en cours.

# Le package myclasses et le fichier en cours ne sont pas au mm niveau -> package non visible par Python
# Solution: ajouter le chemin du dossier principal dans sys.path

import sys
import os

chemin_dossier_en_cours = os.path.dirname(__file__) # c:\.....\19-Classes
chemin_dossier_principal = os.path.dirname(chemin_dossier_en_cours) # c:\.....\InitiationPython
sys.path.append(chemin_dossier_principal)

from myclasses.produit import Produit

p = Produit(1,'PC Dell', 1500)
print(p)

p1 = Produit(1, 'Ecran HP', 99)

print(p == p1)

print(p1.__dict__) # __dict__: permet de convertir un objet en dict.






