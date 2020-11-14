from time import mktime
from datetime import datetime
from variables.variables import temps_tries


def selectionneur_de_date(date_a, date_b):
    #  renvoie la liste des temps entre les dates a et b
    #  renvoie ls indices qui ont été sélectionnés

    #  selection d'un creneau de temps a partir d'une liste triee
    c, d = 0, 0
    #  indices des dates a et b dans la liste L (il faut donc que ces dates soient comprise entre min et max de L)
    liste_tps = []
    indices = []
    #  on change les dates en nombre avec la methode du timestamp
    tps_a = mktime(datetime.strptime(date_a, "%Y-%m-%d %H:%M:%S").timetuple())
    tps_b = mktime(datetime.strptime(date_b, "%Y-%m-%d %H:%M:%S").timetuple())
    while temps_tries[c] < tps_a:
        #  determination de l'indice du tps a
        c += 1
    while temps_tries[d] < tps_b:
        #  determination de l'indice du tps b
        d += 1
    for i in range(c, d+1):
        #  on parcoure les indices des temps entre les dates a et b
        liste_tps.append(temps_tries[i])
        #  on ne considere que les temps entre les dates a et b
        indices.append(i)
        #  on ne considere que les indices entre les dates a et b
    return liste_tps, indices



