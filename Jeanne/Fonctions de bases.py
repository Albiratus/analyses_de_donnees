
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
        _somme = _somme + i
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
                l1.append(x)
            else:
                l2.append(x)
    return tri_rapide(l1)+[pivot]+tri_rapide(l2)


'''def tri_insertion (liste):
    for i in range (1, len(liste)):
        val = liste[i]
        pos = i'''


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
    b = ((x - a)**2 for x in liste)
    var = somme (b)/n
    return var

def covariance (X, Y):
    multiplication = []
    # supposons que len(X) = len(Y)
    for k in range (0, len(X)):
        xmoinsespx = X[k]- moyenne(X)
        ymoinsespy = Y[k]- moyenne(Y)
        multiplication.append(xmoinsespx[k]*ymoinsespy[k])
    return moyenne (multiplication)

def correlation (X, Y):
    a = variance(X)
    b = variance(Y)
    c = covariance(X,Y)
    return c/((a*b)**(1/2))

'''plt.scatter(temps, variable)
plt.title ('courbe'+ str(k))
plt.xlabel()
plt.ylabel()'''


'''plt.title("titre_graphique")
plt.plot([1,2,4,6],[2,4,6,8], "g--", linewidth = 2)
plt.xlabel("nom_axe_abscisses")
plt.ylabel("nom_axe_ordonnés")
# pour limiter la longueur du graphique
plt.axis([borne 1 axe abscisse, borne 2, borne 1 axe ordonnées, borne 2])
# pour montrer le graphique
plt.show()'''


import csv
with open ('projet.csv', 'r') as f:
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


for row in range (1, len(donnees)) :
        bruit.append(donnees[row][2])
        temp.append(donnees[row][3])
        humidite.append(donnees[row][4])
        lum.append(donnees[row][5])
        CO2.append(donnees[row][6])
        date.append(donnees[row][7][0:19])


from datetime import datetime

from time import mktime, strptime, localtime
datensec = []
for k in date :
    datensec.append(mktime(strptime (k, '%Y-%m-%d %H:%M:%S')))

print(strptime('2000:09:22 06:36:45', '%Y:%m:%d %H:%M:%S'))

print(datetime.strptime('2000:09:22 06:36:45', '%Y:%m:%d %H:%M:%S').time())



# t = temprérature en °C.
# d = dew point (point de rosée) en °C.
import math

def alpha(t, Phi):
    a = 17,27
    b = 237,7
    return a*t/(b + t) + math.log(Phi)

def point_rosee (t, Phi):
    return b*alpha(t, Phi)/(a - alpha(t, Phi))

def recherche_indice (instant):
# instant = une heure (ex : 2020-09-12 22:00:00)
    for k in range (0, len(liste_date)):
        if liste_date[k] == instant:
            return k

def humidex (instant):

    kelvin = 273,5
    temperature = t2[recherche_indice(instant)] + kelvin
    dewpoint = point_rosee(t2[recherche_indice(instant)], humidité[recherche_indice(instant)]) + kelvin
# calcul la pression de la vapeur en mbar
    e = 6,11*math.exp(5417.7530*((1/kelvin)-(1/dewpoint)))
# calcul la pression de la vapeur saturante
    h = 0,5555*(e - 10)
    humidex = temperature + h - kelvin
    return humidex



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

print(tri_insert([6,5,4,3,2,1]))


bruittri = []
temptri = []
humiditetri = []
lumtri = []
CO2tri = []
datensectri = tri_insert(datensec)
print(datensectri)


import matplotlib.pyplot as plt

plt.title("lumiere en fonction de la datensectri")
plt.plot(datensectri, lum, "g--", linewidth = 2)
plt.xlabel("date en sec")
plt.ylabel("intensité lumière")
plt.legend('lumière')
plt.plot(datensectri, bruit, "b--", linewidth = 2)
plt.legend('bruit')
# pour montrer le graphique
plt.show()
