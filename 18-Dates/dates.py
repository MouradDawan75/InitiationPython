# Pour créer des dates, il y'à 3 classes à importer depuis le package datetime

from datetime import date, datetime, timedelta

print(">>>> date:")

# Création de date:

today = date.today()
print(today)

before = date(2018,5,28)
print(before)

# Création de datetime:

print(">>> datetime:")

now = datetime.now()
print(now)

other = datetime(2015,8,21,14,35,55)
print(other)

print(">>>> Formattage de dates:")

# Doc: https://strftime.org/

print(other.strftime("%Y"))
print(other.strftime("%B"))
print(other.strftime("%d"))

print(other.strftime("%d/%m/%Y %H:%M:%S"))

print(today.strftime('%d %B %Y'))

print(">>>> timedelta:")

interval = timedelta(days=5)

print(today + interval)

print(">>>> Planification de tâches:")

now = datetime.now()
interval = timedelta(seconds=2)

start_time = now + interval

while now < start_time:
    print('attente.........')
    now = datetime.now()


print('>>>> Exécution la tâche planifiée........')

# L'heure Unix ou heure Posix (aussi appelée Unix Timestamp)
# est une mesure du temps fondée sur le nombre de secondes écoulées depuis le 01 Janvier 1970 00:00:00
# Le module time de Python permet de gérer l'horodatage de façon Unix, affiche un nombre à virgule sans aucune mentien 
# de jours, de mois ou d'années

print(">>>>>>>>>>>>>>>>> time - module pour Unix:")

import time


current_time = time.time()

print(current_time) # nombre de secondes depuis le 01/01/1970

# 60.0 est équivalent à la première minute du 01/01/1970

# Conversions:

time_format = time.gmtime(current_time)

print(time_format.tm_hour)
print(time_format.tm_year)

