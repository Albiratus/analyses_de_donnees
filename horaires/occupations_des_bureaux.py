from fonctions_utiles.fonctions_selections import selectionneur_de_date
from variables.variables import LUM, temps_tries
from time import localtime, asctime
from horaires.anomalies_lumiere import oublie_lumiere


#  donne sous forme de liste les moments ou le bureau est occupé durant une periode arbitraire
def occupation(date_a, date_b):
    horaires_occupe = []
    for i in selectionneur_de_date(date_a, date_b)[1]:
        if oublie_lumiere(LUM)[1][i] != 0:
            horaires_occupe.append(asctime(localtime(temps_tries[i])))
    return horaires_occupe

print(occupation("2019-08-24 00:00:00","2019-08-24 23:59:59"))

