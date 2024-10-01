# fonction: un ensemble d'instructions réutilisable
# Il existe 2 types de méthodes:
# Procédure: est une méthode qui ne renvoie aucun résultat (ex: print())
# Fonction: est une méthode qui renvoie un résultat (ex: input())


# Syntaxe pour créer une fonction: def nom_fonction(paramètres): instructions

def fonction1():
    print('fonction1.........')

# Appel de la fonction1:

fonction1()

# Sans les parenthèses, il s'agit d'une variable contenant l'id de la fonction en mémoire
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
# Depuis Python 3.5, le langage propose aux développeurs un moyen d'indiquer le type attendu des variables ou 
# des paramètres d'une fonction. Le typage reste dynamique même en partiquant les annotations de types.

x:int = 10
s:str = 'test'
b:bool = True

x = 'test'

def somme(x:int, y:int) -> int:
    return x+y

print(somme('chaine1','chaine2'))
#print(somme('chaine1',5))

print(">>>>> Fonction avec des paramètres optionnels:")

def fct(x, alpha=10, beta=15):
    print(x,alpha,beta)

# Les paramètres optionnels possèdent des valeurs par défaut qu'on peut modifiées en cas de besoin et sont définis
# à la suite des paramètres obligatoires

fct(55)
fct(55,40,60)

print('test1', end=" ")
print('test2')

def prix_ttc(prix_ht:float, tva:float = 0.2) -> float:
    return prix_ht * (1 + tva)

prix_ttc(100)

prix_ttc(100, tva=0.35)

# Appel d'une fonction avec des paramètres nommés sans tenir compte de leur position dans la fonction

fct(beta=77, x=99)

print(">>>>>>> Fonction qui renvoie plusieurs résultats:")

def calculs(x:int, y:int):
    somme = x+y
    produit = x*y
    return somme,produit
    
resulat = calculs(10,5)
print(resulat)
print(type(resulat)) # resultat est tuple (liste en lecture seule)

# Eclater un tuple:
s,p = resulat
print(s)
print(p)

print(">>>>> Fonction avec un nombre variable de paramètres:")

print(10,'chaine',True,10.5)

def somme_variable(*entiers:int) -> int:
    #print(type(entiers)) -> entiers: est un tupe à taille variable

    s = 0
    for e in entiers:
        s += e

    return s

print(somme_variable(10,20))
print(somme_variable(10,20,30))
print(somme_variable(10,20,30,40))

print(">>>>> Fonction qui prend en paramètre une autre fonction:")

def add(x,y):
    return x+y

def soustraction(x,y):
    return x-y

def multi_calculs(fct:None,x,y):
    return fct(x,y)

print(multi_calculs(add,10,20))
print(multi_calculs(soustraction,10,20))
print(multi_calculs(lambda x,y: x*y ,10,20))

print(">>>>> Fonctions natives de Python:")

lst = [10,20,30]

sum(lst)
min(lst)
max(lst)
len(lst) # nombre d'éléments
round(2.45899, 2)

def sup10(x):
    return x > 10

print(list(filter(sup10, lst)))
print(list(filter(lambda x: x > 10, lst)))

print(">>>>> Variables locales - globales: ")

# b et c sont des variables gloables -> visibles dans tout le script
b = 10
c = 10

def my_fct():
    global b # demande explicite de manipulation de la variable globale b
    b = 15

    # c et v sont des variables locales -> visibles uniquement dans la fonction
    c = 15
    v = 55
    print("********************************************")
    print(locals())
    print("********************************************")

my_fct()



print(f"b = {b}")
print(f"c = {c}")

print(globals())

def somme(x,y):
    return x+y

# Expression lambda: fonction anonyme -> fonction à 1 seule instruction

f = lambda x,y : x+y

print(f(10,5))

# Les expressions Lambda sont utilisées dans des fonctions prenant en paramètres d'autres fonctions
