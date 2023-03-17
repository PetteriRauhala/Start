# Esimerkkejä päivämäärien, tiedostojen ja JSON-tietojen käytöstä

import datetime # Sisäänrakennettu kirjasto aikamääreille
import json # Sisäänrakennettu kisrjasto JSON-objektien käsittelyä varten

# Päiväyksen muodostaminen

year = 2023
month = 3
day = 17

date = datetime.datetime(year, month, day)

print(date)

# Kuluvan päivän ja kellonajan selvittäminen
just_now = datetime.datetime.now()
print(just_now)

# Aika ero kahden päivämäärän välillä

# Funktio, joka laskee päivämäärien eron päivinä
def datediff(d1,d2):
    """Calculates the difference between two dates in days

    Args:
        d1 (str): A date in ISO format YYYY/MM/DD
        d2 (str): A date in ISO format YYYY/MM/DD

    Returns:
        int: absolute difference in days
    """
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    difference =abs((d2 - d1).days)
    return difference

ero = datediff('2023-03-17', '1995-11-04')
print(ero)

# Funktio, joka laskee kahden kellonajan välisen eron tunteina
def timediff(t1, t2):
    """Calculates the difference between two time values

    Args:
        t1 (str): Time value in format HH:MM:SS
        t2 (str): Time value in format HH:MM:SS

    Returns:
        int: time difference in hours
    """
    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")
    seconds = ((t2 - t1).seconds) # Vain sekunnit ja mikrosekunnin on tuettu timedeltassa
    hours = seconds / 3600
    return hours

aikaero = timediff('10:00:00', '14:30:00')
print(aikaero)

# Määritellään Python-sanakirja
jumppari = {'nimi': 'Erkki', 'Pituus': 171, 'Paino': 75.5}

# Luodaan JSON-merkkijono (objekti)
json_jumppari = json.dumps(jumppari)

print(json_jumppari)

