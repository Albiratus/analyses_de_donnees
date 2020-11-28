from variables.variables import LUM, temps_tries
from time import mktime, strptime, localtime
import datetime
from fonctions_utiles.fonctions_selections import selectionneur_de_date


# on recupere d'une date donnee en secondes l'horaire de la date
def transfo_heure(nbre):
    b = localtime(nbre)
    a = datetime.datetime(b.tm_year, b.tm_mon, b.tm_mday, b.tm_hour, b.tm_min, b.tm_sec)
    #  difference entre la date complete et la date a minuit
    return nbre - mktime(strptime(str(a.date())+" 00:00:00", "%Y-%m-%d %H:%M:%S"))


#  Avant les anomalies on recupere l'heure maximale d'extinction des bureaux
def heure_max_extinction_bureau():
    horaire_max = []
    for i in selectionneur_de_date("2019-08-11 00:00:00", "2019-08-22 00:00:00")[1]:
        #  detection d'une extinction de la lumiere
        if LUM[i] != 0 and LUM[i + 1] == 0:
            horaire_max.append(transfo_heure(temps_tries[i + 1]))
    return max(horaire_max)


#  Avant les anomalies on recupere l'heure minimale d'arrivee dans les bureaux
def heure_min_ouverture_bureau():
    horaire_min = []
    for i in selectionneur_de_date("2019-08-11 00:00:00", "2019-08-22 00:00:00")[1]:
        #  detection de l'allumage de la lumiere dans les bureaux
        if LUM[i] == 0 and LUM[i + 1] != 0:
            horaire_min.append(transfo_heure(temps_tries[i + 1]))
    return min(horaire_min)


def oublie_lumiere(l):
    lumiere_corrig = []
    indices_incorrectes = []
    a = heure_max_extinction_bureau()
    b = heure_min_ouverture_bureau()
    temps_heure = []
    for i in range(len(temps_tries)):
        #  on recupere l'heure sous forme de nombres de chaque instants donnes par les capteurs
        temps_heure.append((transfo_heure(temps_tries[i])))
        #  on effectue une correction de la lumiere sans changer notre liste contenant les anomalies
        lumiere_corrig.append(LUM[i])
        if (temps_heure[i] > a or temps_heure[i] < b) and l[i] != 0:
            #  si l'on se trouve avant l'heure minimale d'ouverture ou apres l'heure de fermeture
            #  Si la lumiere est restée allumée, on récupere l'indice de ces anomalies et on la corrige
            indices_incorrectes.append(i)
            lumiere_corrig[i] = 0
    return indices_incorrectes, lumiere_corrig
