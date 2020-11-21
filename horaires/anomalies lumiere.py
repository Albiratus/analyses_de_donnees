from variables.variables import LUM, temps_tries
from time import mktime, strptime, localtime
import datetime
from fonctions_utiles.fonctions_selections import selectionneur_de_date
import matplotlib.pyplot as plt


def transfo_heure(nbre):
    b = localtime(nbre)
    print(b)
    a = datetime.datetime(b.tm_year, b.tm_mon, b.tm_mday, b.tm_hour, b.tm_min, b.tm_sec)
    print(a)
    print("1970-01-01 " + str(a.time()))
    print(strptime("1970-01-01 " + str(a.time()), "%Y-%m-%d %H:%M:%S"))
    return mktime(strptime("1970-01-01 " + str(a.time()), "%Y-%m-%d %H:%M:%S"))
print(transfo_heure(temps_tries[274]))
print(transfo_heure(temps_tries[275]))

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
    indices_incorrectes = []
    a = heure_max_extinction_bureau()
    b = heure_min_ouverture_bureau()
    temps_heure = []

    for i in range(len(temps_tries)):
        temps_heure. append((transfo_heure(temps_tries[i])))
        print(len(temps_heure))
        if temps_heure[0] > a or temps_heure[0] < b:

            l[i] = 0
            indices_incorrectes.append(i)

    return indices_incorrectes, l
print(oublie_lumiere(LUM))

lumiere_corrigee = oublie_lumiere(LUM)[1]
tps_corrig = []
for k in oublie_lumiere(LUM)[0]:
    tps_corrig.append(temps_tries[k])

plt.plot(temps_tries, LUM)
plt.scatter(tps_corrig, lumiere_corrigee, "color=red")
plt.show()

