import logging

from logging.handlers import RotatingFileHandler

# La classe RotatingFileHandler dans le module logging permet au dév. de créer un gestionnaire de journalisation
# qui lui donne la possibilité de faire pivoter ses fichiers de logs en fct de leur taille.

logger = logging.getLogger("Ritating logger")
logger.setLevel(logging.INFO)


# maxBytes=0 -> taille illimitée (1 seul fichier de log) -> la rotation ne se produit jamais
# backupCount = limiter le nombre de fichiers

file_handler = RotatingFileHandler(
    
    '24-Logging/rotating.log',
    mode='a',
    maxBytes=20,
    backupCount=5,
    encoding='utf-8'
    
    )

logger.addHandler(file_handler)

for i in range(10):
    logger.info(f"Ceci est la ligne {i}")