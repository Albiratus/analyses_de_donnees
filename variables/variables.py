#  importation des bibliotheques
import time
import datetime
import csv
from fonctions_utiles.fonctions_stats import tri_par_insertion_upgrade

#  ouverture du fichier dans une liste "donnees
donnees = []
#  creation d'une liste vide qui va recevoir les donnees du fichier csv
fichier = csv.reader(open("EIVP_KM.csv"), delimiter=";")


#  extraction des données
for k in fichier:
    donnees.append(k)
temps, noise, temp, humidity, lum, co_deux = [], [], [], [], [], []
#  creation de liste vide qui vont recevoir les colonnes du fichier
for k in range(1, len(donnees)):
    #  on parcourt les lignes des donnees puis on remplie chaque liste avec les donnees correspondantes
    #  selection des dates sans le 0200
    temps.append(donnees[k][6][0:19])
    noise.append(float((donnees[k][1])))
    temp.append(float(donnees[k][2]))
    humidity.append(float(donnees[k][3]))
    lum.append(float(donnees[k][4]))
    co_deux.append(float(donnees[k][5]))


#  transformation des dates en nombre avec la mehode de  timestamp (unix)
#  qui designe le nombre de secondes ecoulees depuis le 1er janvier 1970 a minuit UTC precise
temps_en_seconde = []
for k in temps:
    temps_en_seconde.append(time.mktime(datetime.datetime.strptime(k, "%Y-%m-%d %H:%M:%S").timetuple()))


#  tri des listes en fonctions de la liste du temps
NOISE, TEMP, HUMIDITY, LUM, C0_DEUX = [], [], [], [], []
temps_tries, liste_indices_correspondantes = tri_par_insertion_upgrade(temps_en_seconde)
for k in liste_indices_correspondantes:
    C0_DEUX += [co_deux[k]]
    NOISE += [noise[k]]
    TEMP += [temp[k]]
    LUM += [lum[k]]
    HUMIDITY += [humidity[k]]
