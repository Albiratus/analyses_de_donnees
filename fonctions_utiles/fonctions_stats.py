def minimum(liste):
    mini = liste[0]
    for i in liste:
        if i < mini:
            i = mini
    return mini


def maximum (liste):
    maxi = liste[0]
    for i in liste:
        if i > maxi:
            i = maxi
    return maxi


def somme (liste):
    _somme = 0
    for i in liste:
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