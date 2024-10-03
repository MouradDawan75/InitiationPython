import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(filename)s - %(message)s",
    filename="24-Logging/app.log", # si fichier inexistant -> il sera crée par la fct
    filemode='a',
    encoding='utf-8',

    # formattage de la date
    datefmt="%d/%m/%Y - %H:%M"
)

def addition(x,y):

    logging.info(">>> Appel de la fct addition......")
    return x+y

addition(10,5)

try:
    10/0
except Exception as e:
    logging.error(e)