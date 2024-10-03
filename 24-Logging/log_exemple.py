import logging

# On peut logguer plusieurs types d'informations:
# - Informations de debur: c'est pour la partie dév.
# - Informations générales non problèmatiques: pour indiquer une action -> connexion d'un user -> suppression d'un objet en BD
# - Informations pour indiquer une erreur:
#   * warning: problème mineur
#   * error: pour indiquer un problème (Exception)
#   * critical: pour indiquer une erreur critique (arrêt de l'application)

# 5 niveaux de messages: debug -> info -> warning -> error -> critical

# Par défaut, ce module utilise le niveau warning pour les messages

logging.basicConfig(

    level=logging.DEBUG,
    # Formatter le message
    format="%(asctime)s - %(levelname)s - %(message)s"

)

logging.debug("Debug message....")
logging.info("Info message.....")
logging.warning("Warning message....")
logging.error("Error message.....")
logging.critical("Critical message.......")