from analyses_de_donnees.fonctions_utiles.fonctions_stats import tri_insert
from analyses_de_donnees.variables.variables import temps_tries, C0_DEUX
import matplotlib.pyplot as plt


def troisiemequartile(liste):
    if len(liste)<1 :
        return None
    else :
        if len(liste)%4 == 0 :
            a = 3*len(liste)/4 - 1
            return int(a)
        else :
            b = 3*(len(liste)/4)
            return (int(b))


def premierquartile (liste):
    if len(liste)<1 :
        return None
    else :
        if len(liste)%4 == 0:
            a = (len(liste))/4 -1
            return int(a)
        else :
            b = len(liste)/4
            return int(b)

def ejecter_anomalies (liste):
    list = tri_insert(liste)
    a = premierquartile(liste)
    b = troisiemequartile(liste)
    return(liste[a:b+1])


def traceur_bonnes_valeurs (X):
    a = premierquartile(X)
    b = troisiemequartile(X)
    plt.plot(temps_tries[a:b+1], ejecter_anomalies(X), label=str(X))
    plt.legend('bonnes valeurs')
    plt.xlabel('datensec')
    plt.show()

traceur_bonnes_valeurs(C0_DEUX)