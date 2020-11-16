from fonctions_utiles.fonctions_selections import selectionneur_de_date
from variables.variables import LUM, temps_tries
from time import localtime, asctime


def occupation(date_a, date_b):
    horaires_occupe = []
    for i in selectionneur_de_date(date_a, date_b)[1]:
        if LUM[i] != 0:
            horaires_occupe.append(asctime(localtime(temps_tries[i])))
    return horaires_occupe



