from variables.variables import LUM, temps_tries
from time import localtime, mktime, strptime
from fonctions_utiles.fonctions_selections import selectionneur_de_date
import matplotlib.pyplot as plt


def transfo_heure(l):

    return localtime()

def heure_max_extinction_bureau():
    horaire_max = []
    for k in selectionneur_de_date("2019-08-11 00:00:00", "2019-08-22 00:00:00")[1]:
        if LUM[k] != 0 and LUM[k+1] == 0:
            horaire_max.append(transfo_heure(temps_tries[k+1]))
    return max(horaire_max)

def heure_min_ouverture_bureau():
    horaire_min = []
    for k in selectionneur_de_date("2019-08-11 00:00:00", "2019-08-22 00:00:00")[1]:
        if LUM[k] == 0 and LUM[k+1] != 0:
            horaire_min.append(transfo_heure(temps_tries[k + 1]))
    return min(horaire_min)


def oublie_lumiere(l):
    indices_incorrectes = []
    a = heure_max_extinction_bureau()
    b = heure_min_ouverture_bureau()
    temps_heure=[]

    for k in range(len(temps_tries)):
        temps_heure. append((transfo_heure(temps_tries[k])))
        print(k)
        print(temps_heure[k])
        print(len(temps_heure))

    print(len(temps_heure))
    return indices_incorrectes, l


"""
tps_corrig=[]
for k in oublie_lumiere(LUM)[0]:
    tps_corrig.append(temps_tries[k])

plt.plot(tps_corrig,LUM)
plt.scatter(tps_corrig,lumiere_corrigee,"color=red")
plt.show()"""

plt.plot([1,2,3],[1,3,2])
plt.show()