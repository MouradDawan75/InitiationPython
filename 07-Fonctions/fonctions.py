# fonction: un ensemble d'instructions réutilisable
# Il existe 2 types de méthodes:
# Procédure: est une méthode qui ne renvoie aucun résultat (ex: print())
# Fonction: est une méthode qui renvoie un résultat (ex: input())


# Syntaxe pour créer une fonction: def nom_fonction(paramètres): instructions

def fonction1():
    print('fonction1.........')

# Appel de la fonction1:

fonction1()

# Sans les parenthèses, il s'agit d'une contenant l'id de la fonction en mémoire
print(fonction1)

f = fonction1
f()

# Exemple d'une fonction avec des paramètres:

def repeter(message,nombre_de_fois):
    # for i in range(nombre_de_fois):
    #     print(message)

    i = 0
    while i < nombre_de_fois:
        print(message)
        i += 1


repeter('hello', 5)

# Exemple d'une fonction qui renvoie un résultat:

def carre(nombre):
    return nombre ** 2

r = carre(5)
print(r)

# Annotation de types:
# Depuis Python 3.5, le langage propose aux dévelopeur un moyen d'indiquer le type attendu de variables ou 
# de paramètres d'une fonction. Le typage dynamique même en partiquant les annotations de types

x:int = 10
s:str = 'test'
b:bool = True

x = 'test'

def somme(x:int, y:int) -> int:
    return x+y

print(somme('chaine1','chaine2'))
#print(somme('chaine1',5))