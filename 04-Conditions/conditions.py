print(">>>>>> Bloc conditionnel:")

# Bloc conditionnel: est un ensemble d'instrcutions qui ne s'exécute que si une condition est vérifiée

age = 15

if age < 18:
    print("mineur")
    print("Toujours mineur")

print("fin du if")

# Les : représentent le début du bloc d'instructions. Tant que les instructions sont indentées de l mm, on est toujours
# dans le bloc

if age < 18:
    print("mineur")
elif age <= 25:
    print("jeune adulte")
else:
    print("adulte")

# On peut aussi combiner des condition en utilisant les opérateurs logiques:

if age >= 18 and age <= 25:
    print("Vous avez entre 18 et 25 ans")

# Un bloc vide n'est pas valide syntaxiquement:
# pass permet de définir un bloc vide valide syntaxiquement

if True:
    pass # a compléter par la suite

print('sortie du if')

# Opérateur ternaire: permet de remplacer un if/else classique, ou bien de faire des affectations conditionnelles

# if/else classique:

if age < 18:
    print('mineur')
else:
    print('majeur')

# Equivalent en syntaxe ternaire: syntaxe simplifiée

print('mineur') if age < 18 else print('majeur')

# Affectation conditionnelle:

x = 10 if age < 18 else 15

# Depuis Python 3.10, ajout du match/case qui permet de remplacer les elif qui s'imbriquent

note = 6 

match note:

    case 0|1|2|3|4|5|6|7|8|9:
        print("En dessous de a moyenne")
    case 10|11|12|13:
        print("Juste la moyenne")

    # Pour es autres cas, 2 syntaxes possibles:
    # soit case other:
    # soit case _:

    case other:
        print('Good job')

    # case _:
    #     print('Good job')

# Pour commenter des lignes sélectionnées: ctr + k + c
# Pour décommenter des lignes sélectionnées: ctr + k + u