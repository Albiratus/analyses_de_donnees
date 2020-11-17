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
                return l1.append(x)
            else:
                return l2.append(x)
    return tri_rapide(l1)+[pivot]+tri_rapide(l2)


def tri_insertion (liste):
    for i in range (1, len(liste)):
        vol = liste[i]
        pos = i


    liste_vide = []
    #faire une liste avec les indices de départ
    for k in range (1, len(liste)-1):
        append.k
    # mettre les indices de liste dans notre liste


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

print(strptime('2000:09:22 06:36:45', '%Y:%m:%d %H:%M:%S'))

print(datetime.strptime('2000:09:22 06:36:45', '%Y:%m:%d %H:%M:%S').time())

import matplotlib.pyplot as plt

plt.title("lumiere en fonction de la datensec")
plt.plot(datensec, lum, "g--", linewidth = 2)
plt.xlabel("date en sec")
plt.ylabel("intensité lumière")
plt.legend('lumière')
plt.plot(datensec, bruit, "b--", linewidth = 2)
plt.legend('bruit')

# pour montrer le graphique
plt.show()
