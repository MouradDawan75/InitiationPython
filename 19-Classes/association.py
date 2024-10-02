# Association - Composition d'objets

class Adresse:

    def __init__(self, numero, street) -> None:
        self.numero = numero
        self.street = street


class Client:

    # Association: c'est qu'un objet donné puisse faire partie des attributs d'un autre objet

    def __init__(self, nom:str, adresse:Adresse) -> None:
        self.nom = nom
        self.adresse = adresse



c = Client('Carrefour', Adresse(15, 'rue machin 75015 Paris'))

# Exo: Un client souhaite gérer le salaire de ses employés.
# Tous les employés possèdent un nom, un prénom et un âge
# Ceux qui sont affectés à la vente: leur salaire mensuel est le 20% du CA qu'ils réalisent plus un bonus de 200
# Ceux qui sont affectés à la représentation: leur salaire mensuel est le 20% du CA qu'ils réalisent 
# plus un bonus de 400
# Ceux qui sont affectés à la prod: leur salaire mensuel est le nombre d'heures qu'ils réalisent multiplié par 65

# Définir le modèle objet en respectant les conditions suivantes:
# Employe est la classe mère. Elle contient les attributs communs, plus 2 fonctions
#  une fonction calculer_salaire() -> float
#  une fonction get_nom() qui renvoie la chaine L'employé concaténée au nom et au prénom 
# Chaque classe fille doit avoir les attributs qui lui sont spécifiques plus un codage approprié des fonctions 
# calculer_salaire et get_nom en remplaçant la chaine L'employé par la catégorie de l'employé 

# Besoins fonctionnels:
# Afficher la liste des employés
# Insérer un employé dans la liste
#  Afficher le salaire de chacun des employés
# Afficher le salaire moyen de tous les employés

# Ajoutez un module de fonctions nommé fonctions.py (que des fonctions polymorphiques)
# Utilisez une liste globale (visible par toutes les fonctions)
