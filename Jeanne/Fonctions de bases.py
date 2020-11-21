import matplotlib.pyplot as plt

import csv
with open ('projet.csv', 'r') as f :
    reader = csv.reader(f, delimiter =';')
    donnees = []
    for row in reader :
        donnees.append(row)


bruit = []
temp = []
humidite = []
lum = []
CO2 = []
date = []

i = 0
for row in donnees :
    if i != 0 :
        bruit.append(row[2])
        temp.append(row[3])
        humidite.append(row[4])
        lum.append(row[5])
        CO2.append(row[6])
        date.append(row[7][0:19])
    i = i + 1

from datetime import datetime

from time import mktime, strptime, localtime
datensec = []
for k in date :
    datensec.append(mktime(strptime (k, '%Y-%m-%d %H:%M:%S')))





def minimum (liste):
    mini = liste [0]
    for i in liste :
        if i < mini :
            i = mini
    return mini

def maximum (liste):
    maxi = liste[0]
    for i in liste :
        if i > maxi :
            i = maxi
    return maxi

def somme (liste):
    _somme = 0
    for i in liste :
        _somme = _somme + float(i)
    return _somme

def moyenne (liste):
    a = len(liste)
    moy = somme(liste)/a
    return moy

def tri_rapide (liste):
    if liste == []:
        return[]
    else :
        pivot = liste.pop()
        l1,l2 = [], []
        for x in liste :
            if x<pivot:
                return l1.append(x)
            else:
                return l2.append(x)
    return tri_rapide(l1)+[pivot]+tri_rapide(l2)



def mediane (l):
    l=tri_rapide(l)
    if len(l)<1 :
        return None
    else :
        if len (l)%2 == 1 :
            return (len(l)-1)/2
        else :
            a = [len(l)/2-1, len(l)/2]
            return moyenne(a)


def variance (liste):
    a = moyenne(liste)
    n = len (liste)
    b = ((float(x) - a)**2 for x in liste)
    var = somme (b)/n
    return var

def covariance (X, Y):
    multiplication = []
    # supposons que len(X) = len(Y)
    for k in range (0, len(X)):
        xmoinsespx = float(X[k])- moyenne(X)
        ymoinsespy = float(Y[k])- moyenne(Y)
        multiplication.append(xmoinsespx*ymoinsespy)
    return moyenne (multiplication)

def correlation (X, Y):
    a = variance(X)
    b = variance(Y)
    c = covariance(X,Y)
    return c/((a*b)**(1/2))




def tri_insert (liste):
    liste_indice = [0]
    for k in range (1, len(liste)):
        liste_indice.append(k)
        a = k
        while a>0 and liste[a-1]>liste[a]:
            liste[a], liste[a-1]=liste[a-1], liste[a]
            liste_indice[a], liste_indice[a-1]= liste_indice[a-1], liste_indice[a]
            a -= 1
    return liste, liste_indice




bruittri = []
temptri = []
humiditetri = []
lumtri = []
CO2tri = []

indice = tri_insert(datensec)[1]
datensectri = tri_insert(datensec)[0]


for k in indice :
    bruittri.append(bruit[k])
    temptri.append(temp[k])
    humiditetri.append(humidite[k])
    lumtri.append(lum[k])
    CO2tri.append(CO2[k])



'''plt.subplot(211)
plt.title("bruittri en fonction de la datensectri")
plt.plot(datensectri, bruittri, label = str(moyenne(bruit)), linewidth = 2)
plt.xlabel("date en sec")
plt.ylabel("intensité bruit")
plt.legend()
plt.subplot(212)
plt.plot(datensectri, temptri, "--b", linewidth = 2)
plt.legend('temp')

# plt.show()
# pour montrer le graphique'''


def traceur_de_correlation (X, Y):
    plt.plot(datensectri, X, label = str(X))
    plt.plot(datensectri, Y, label = str(Y))
    plt.legend(str(correlation(X,Y)))
    plt.xlabel('datensec')
    plt.show()

traceur_de_correlation (bruittri, temptri)



# t = temprérature en °C.
# d = dew point (point de rosée) en °C.
import math

def alpha(t, Phi):
    a = 17,27
    b = 237,7
    return a*t/(b + t) + math.log(Phi)

def point_rosee (t, Phi):
    b = 237,7
    a = 17,27
    return b*alpha(t, Phi)/(a - alpha(t, Phi))

def recherche_indice (instant):
# instant = une heure (ex : 2020-09-12 22:00:00)
    for k in range (0, len(datensectri)):
        if datensectri[k] == instant:
            return k

def humidex (instant):

    kelvin = 273,5
    temperature = temptri[recherche_indice(instant)] + kelvin
    dewpoint = point_rosee(temptri[recherche_indice(instant)], humiditetri[recherche_indice(instant)]) + kelvin
# calcul la pression de la vapeur en mbar
    e = 6,11*math.exp(5417.7530*((1/kelvin)-(1/dewpoint)))
# calcul la pression de la vapeur saturante
    h = 0,5555*(e - 10)
    humidex = temperature + h - kelvin
    return humidex
