import matplotlib.pyplot as plt
from variables.variables import C0_DEUX, TEMP, LUM, NOISE, HUMIDITY
from fonctions_utiles.fonctions_selections import selectionneur_de_date


def traceur(date_debut, date_fin):
    #  traceur de courbes entre deux dates donnees
    c0_deux_choisi, temp_choisi, lum_choisi, humidity_choisi, noise_choisi = [], [], [], [], []
    #  creation de nouvelles listes vides
    liste_tps = selectionneur_de_date(date_debut, date_fin)[0]
    #  selection du creneau
    for i in selectionneur_de_date(date_debut, date_fin)[1]:
        #  on parcoure les indices correspondant de nos listes deja triees
        c0_deux_choisi.append(C0_DEUX[i])
        temp_choisi.append(TEMP[i])
        lum_choisi.append(LUM[i])
        noise_choisi.append(NOISE[i])
        humidity_choisi.append(HUMIDITY[i])

    plt.subplot(331)
    plt.plot(liste_tps, temp_choisi)
    plt.title("Temperature des bureaux entre le " + str(date_debut) + " et le " + str(date_fin))
    plt.xlabel = "temps en seconde"
    plt.ylabel = "Temperature en degre celsius"

    plt.subplot(333)
    plt.plot(liste_tps, noise_choisi)
    plt.title(" niveau sonore des bureaux entre le " + str(date_debut) + " et le " + str(date_fin))
    plt.xlabel = "temps en seconde"
    plt.ylabel = "niveau sonore (dBA)"

    plt.subplot(335)
    plt.plot(liste_tps, humidity_choisi)
    plt.title(" humidite relative des bureaux entre le " + str(date_debut) + " et le " + str(date_fin))
    plt.xlabel = "temps en seconde"
    plt.ylabel = " humidite relative (%)"

    plt.subplot(337)
    plt.plot(liste_tps, lum_choisi)
    plt.title("niveau lumineux des bureaux entre le " + str(date_debut) + " et le " + str(date_fin))
    plt.xlabel = "temps en seconde"
    plt.ylabel = "niveau lumineux (lux)"

    plt.subplot(339)
    plt.plot(liste_tps, c0_deux_choisi)
    plt.title("quantite de CO2 des bureaux entre le " + str(date_debut) + " et le " + str(date_fin))
    plt.xlabel = "temps en seconde"
    plt.ylabel = "quantite de CO2 (ppm)"

    plt.show()


traceur("2019-08-11 00:00:00", "2019-08-25 17:47:08")
