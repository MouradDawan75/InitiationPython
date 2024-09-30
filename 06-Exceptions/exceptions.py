# Il existe 3 types d'erreurs possibles:

# - Erreurs de syntaxes (de compilation): elles sont détectées automatiquement par l'IDE
# - Exceptions: se sont des erreurs qui provoquent l'arrêt de l'application
# - Code fonctionnel, mais qui renvoie un résultat inattendu (debuggage)


# Pour éviter m'arret de 'application, on doit gérer l'exception.
# Pour gérer l'exception, on utilise le bloc try-except

# Il existe plusieurs d'exceptions possibles, chacune d'elles porte le nom de l'erreur qu'elle génère.
# Il existe aussi un type générique d'exception (Exception) qui inclus tous les types d'exceptions.



try:
    chaine = 'test' + 5
    print(10 / 0)
    

except ZeroDivisionError:
    print('Division Exception gérée.......')

except TypeError:
    print("TypeError exception gérée......")

print('suite du script')

print('>>>>> Type générique Exception:')

# Obligation: une ressource (fichier, base de données) doit être libérée à la fin de son utilisation.

try:
    chaine = 'test' + 5
    print(10 / 2)
    # Ouverture d'un fichier en lecture
    
        
    

except Exception as e:
    print("Générique Exception gérée......")
    print(e)
    

else:
    # bloc optionnel qui s'exécute si le try n'a pas générer d'erreurs
    print("bloc else.........")
    

finally:
    # bloc optionnel qui s'exécute tout le temps
    print('finally......')
    # Fermeture du fichier
    # Ce bloc sert dans la pratique à libérer les ressources utilisées dans le try.

print('suite du script')

while True:
    nombre = input('Votre nombre: ')
    try:
        nombre = int(nombre)
        #break

    except: # syntaxe simplifiée de except Exception:
        print("Saisie invalide....")

    else:
        break

print(nombre)
