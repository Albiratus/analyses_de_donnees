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
