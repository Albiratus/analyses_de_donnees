from variables.variables import temps_tries, LUM, NOISE
import matplotlib.pyplot as plt
from fonctions_utiles.fonctions_stats import correlation


def traceur_de_correlation(X, Y):
    plt.plot(temps_tries, X, label=str(X))
    plt.plot(temps_tries, Y, label=str(Y))
    plt.legend(str(correlation(X, Y)))
    plt.xlabel('datensec')
    plt.show()


traceur_de_correlation(NOISE, LUM)
