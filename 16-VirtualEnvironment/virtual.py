# Un environnement virtuel est une copie de Python.

# Bonnes Pratiques:

# Au début d'un projet, on crée un environnement virtuel contenant les modules externes concernant le 
# projet en question.

# Pour créer un envi. virtuel, on utilise le module de base venv.
#1-  Commande à exécuter dans le terminal:
# python -m venv myenv

# 2- Activation de l'environnement virtuel
# Commande à exécuter dans le terminal: .\myenv\Scripts\activate

# Si POwer Shell bloque l'exécution de script externe:
# 1- Démarrer Power Shell en tant qu'admin
# 2- Exécutez la commande suivante: Set-ExecutionPolicy RemoteSigned -> réponse par O (pour oui)

print('test')


# A la fin du projet, on génère un fichier contenant la liste des modules externes utilisés dans le projet
# Commande à exécuter dans le terminal: pip freeze --local > requirements.txt

# Pour installer les modules listés dans requirements.txt:
# Commande à exécuter dans le terminal: pip install -r requirements.txt