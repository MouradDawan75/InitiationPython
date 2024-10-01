def convertir_minutes_en_heures(minutes:int):
    print(f"{minutes}m = {minutes // 60}h {minutes % 60}m")

def convertir_heures_en_minutes(heures:int):
    print(f"{heures}h = {heures * 60}m")

def demander_saisie_nombre_valide(message:str) -> int:
    while True:
        nb = input(message)
        try:
            nb = int(nb)
            return nb # return fonctionne comme un break

        except:
            print('Nombre invalide.......')


def afficher_menu() -> str:

      choix = input("""

 Votre choix: 
  1) Convertir heures en minutes -> Ex: nombre saisi 90 -> affichez 90m = 1h 30m
  2) Convertir minutes en heures -> Ex: nombre saisi 6 -> affichez 6h = 180m
  3) Quitter
                  
""")
      
      return choix