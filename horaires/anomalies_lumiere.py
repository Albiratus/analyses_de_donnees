from variables.variables import LUM, temps_tries
from time import mktime, strptime, localtime
import datetime
from fonctions_utiles.fonctions_selections import selectionneur_de_date
import matplotlib.pyplot as plt


def transfo_heure(nbre):
    b = localtime(nbre)
    a = datetime.datetime(b.tm_year, b.tm_mon, b.tm_mday, b.tm_hour, b.tm_min, b.tm_sec)
    return nbre - mktime(strptime(str(a.date())+" 00:00:00", "%Y-%m-%d %H:%M:%S"))


def heure_max_extinction_bureau():
    horaire_max = []
    for i in selectionneur_de_date("2019-08-11 00:00:00", "2019-08-22 00:00:00")[1]:
        if LUM[i] != 0 and LUM[i + 1] == 0:
            horaire_max.append(transfo_heure(temps_tries[i + 1]))
    return max(horaire_max)


def heure_min_ouverture_bureau():
    horaire_min = []
    for i in selectionneur_de_date("2019-08-11 00:00:00", "2019-08-22 00:00:00")[1]:
        if LUM[i] == 0 and LUM[i + 1] != 0:
            horaire_min.append(transfo_heure(temps_tries[i + 1]))
    return min(horaire_min)


def oublie_lumiere(l):
    lumiere_corrig=[]
    indices_incorrectes = []
    a = heure_max_extinction_bureau()
    b = heure_min_ouverture_bureau()
    temps_heure = []
    for i in range(len(temps_tries)):
        temps_heure.append((transfo_heure(temps_tries[i])))
        lumiere_corrig.append(LUM[i])
        if (temps_heure[i] > a or temps_heure[i] < b) and l[i] != 0:
            indices_incorrectes.append(i)
            lumiere_corrig[i]=0
    return indices_incorrectes,lumiere_corrig


tps_corrig = []
point_lum_anomalique = []
for k in oublie_lumiere(LUM)[0]:
    tps_corrig.append(temps_tries[k])
    point_lum_anomalique.append(LUM[k])

plt.subplot(211)
plt.plot(temps_tries, LUM)
plt.scatter(tps_corrig, point_lum_anomalique, color='red')
plt.subplot(212)
plt.plot(temps_tries,oublie_lumiere(LUM)[1])
plt.show()
