import matplotlib.pyplot as plt
import math
from variables.variables import temps_tries, TEMP, HUMIDITY, date_triee
from fonctions_utiles.fonctions_selections import selectionneur_de_date

# t = temprérature en °C.
# d = dew point (point de rosée) en °C.


def alpha(t, Phi):
    a = 17.27
    b = 237.7
    return a*t/(b + t) + math.log(Phi)


def point_rosee(t, Phi):
    b = 237.7
    a = 17.27
    return b*alpha(t, Phi)/(a - alpha(t, Phi))


def recherche_indice(instant):
    #  instant = une heure (ex : 2020-09-12 22:00:00)
    for k in range(0, len(temps_tries)):
        if date_triee[k] == instant:
            return k


def calcul_humidex(instant):
    temperature = TEMP[recherche_indice(instant)]
    humidite = HUMIDITY[recherche_indice(instant)]
    dewpoint = point_rosee(temperature, humidite)
# calcul la pression de la vapeur en mbar
    e = 6.11*math.exp(5417.7530*((1/273.16)-1/(273.15-dewpoint)))
# calcul la pression de la vapeur saturante
    h = 0.5555*(e - 10)
    humidex = temperature + h
    return humidex


def tracer_humidex(date_a, date_b):
    humidex = []
    for k in selectionneur_de_date(date_a, date_b)[1]:
        humidex.append(calcul_humidex(date_triee[k]))
    plt.scatter(selectionneur_de_date(date_a, date_b)[0], humidex)
    plt.show()


tracer_humidex("2019-08-11 17:48:06", "2019-08-23 23:48:02")
