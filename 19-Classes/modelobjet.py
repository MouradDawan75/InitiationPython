
class Employe:

    def __init__(self,nom,prenom,age) -> None:
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def calculer_salaire(self):
        return 0
    
    def get_nom(self):
        return f"L'mployé {self.nom} {self.prenom}"
    

class Commercial(Employe):

    def __init__(self, nom, prenom, age, ca) -> None:
        super().__init__(nom, prenom, age)
        self.ca = ca
    

class Vendeur(Commercial):

    BONUS_VENDEUR = 200
    POURCENT_VENDEUR = 0.2

    def __init__(self, nom, prenom, age,ca) -> None:
        super().__init__(nom, prenom, age, ca)
        

    def calculer_salaire(self):
        return self.ca * Vendeur.POURCENT_VENDEUR + Vendeur.BONUS_VENDEUR
    
    def get_nom(self):
        return f"Le venduer {self.nom} {self.prenom}"
    
class Representant(Commercial):

    BONUS_REPRESENTANT = 400
    POURCENT_REPRESENTANT = 0.2

    def __init__(self, nom, prenom, age, ca) -> None:
        super().__init__(nom, prenom, age, ca)
        

    def calculer_salaire(self):
        return self.ca * Representant.POURCENT_REPRESENTANT + Representant.BONUS_REPRESENTANT
    
    def get_nom(self):
        return f"Le représentant {self.nom} {self.prenom}"
    

class Technicien(Employe):

    TAUX_HORAIRE = 65

    def __init__(self, nom, prenom, age, heures) -> None:
        super().__init__(nom, prenom, age)
        self.heures = heures

    def calculer_salaire(self):
        return self.heures * Technicien.TAUX_HORAIRE
    
    def get_nom(self):
        return f"Le technicien {self.nom} {self.prenom}"