from detection_par_vars_stats.anomalies_stats import ejecter_anomalies
import matplotlib.pyplot as plt
from variables.variables import temps_tries, LUM, C0_DEUX, HUMIDITY, NOISE


def traceur_bonnes_valeurs(X):
    tps_corrig = []
    instant_anomalies = []
    point_anormale = []
    #  on parcoure les indices anormales
    for k in ejecter_anomalies(X)[1]:
        #  on recupere les instants ainsi que les points anormales correspondants
        instant_anomalies.append(temps_tries[k])
        point_anormale.append(X[k])
    for k in ejecter_anomalies(X)[2]:
        tps_corrig.append(temps_tries[k])
    plt.subplot(211)
    plt.plot(temps_tries, X)
    # points défectueux en rouge
    plt.scatter(instant_anomalies, point_anormale, color='red')
    plt.xlabel = "date en seconde"
    plt.subplot(212)
    plt.plot(tps_corrig, ejecter_anomalies(X)[0])
    plt.xlabel = "date en seconde"
    plt.show()


traceur_bonnes_valeurs(LUM)
