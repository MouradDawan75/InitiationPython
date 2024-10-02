
from modelobjet import Employe

employes:list[Employe] = []

def insert(e: Employe):
    employes.append(e)

def afficher_salaire_de_chaque_employe():
    if employes:
        for e in employes:
            print(f"{e.get_nom()} gagne {e.calculer_salaire()} euros.")
            print("***********************")
    else:
        print('Aucun employé trouvé.....')

def afficher_tous_les_employes():
    if employes:
        print(f"Il existe {len(employes)} employés.")
        for e in employes:
            print(e.get_nom())
            print("***********************")

    else:
        print('Aucun employé trouvé.....')


def salaire_moyen() -> float:
    if employes:
        s = 0
        for e in employes:
            s += e.calculer_salaire()

        return s / len(employes)
    
    else:
        return 0
