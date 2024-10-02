# Les types de base: int, bool, float et str sont immuables

x = 10
print(id(x))
x = 11
print(id(x))

s = 'test'
s = s.upper()
print(s)

texte = " ceci est une chaine "

print(texte.upper())
print(texte.lower())
print('ceci' in texte)
print(texte.startswith('ceci')) # False
print(texte.endswith('chaine ')) # True
print(texte.strip()) # suppression des éspaces de début et de fin chaine

print(">>>> rstrip - lstrip:")

print(' chaine '.rstrip())
print(' chaine '.lstrip())

print(texte.replace('e','a'))
print(texte.replace('e','a', 2))

print(">>>>>> Split:")

print(texte.split())

chaine = 'mot1,mot2,mot3,mot4'

print(chaine.split(',', 2))

print(">>> rsplit:")

fichier = "test.note.pdf"

# Extraire l'extension du fichier:
print(fichier.rsplit('.', 1)[1])

print(">>>>> join:")

print(':'.join(['mot1','mot2','mot3']))

# Exo1 Définir une fct qui renvoie la chaine inversée

def inverser_chaine(chaine:str) -> str:
    lst = list(chaine)
    lst.reverse()
    return ''.join(lst)

# Exo2 définir une fct qui vérifie si une chaine est un palindrôme (se lit de la mm façon dans les 2 sens): sos, sms

def verif_palindrome(chaine:str) -> bool:
    chaine = chaine.upper()
    return chaine == inverser_chaine(chaine)


print(verif_palindrome('Sms'))