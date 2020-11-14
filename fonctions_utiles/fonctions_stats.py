
def etendue(L):
    return max(L) - min(L)


def correlation(l1, l2):
    m1 = moyenne(l1)
    m2 = moyenne(l2)
    v1 = variance(l1)
    v2 = variance(l2)
    s = 0
    for i in range(len(l1)):
        s += (l1[i] - m1) * (l2[i] - m2)
    return s / (v1 * v2) ** (1 / 2)


#  renvoie la liste des temps triees et la disposition sous forme de liste de ses indices apres le tri
def tri_par_insertion_upgrade(liste):
    #  retourne la liste triee et son ordre indiciel
    li = []
    for i in range(len(liste)):
        li.append(i)
        #  ordre non triee des indices de la liste des temps
    for i in range(1, len(liste)):
        j = i
        while j > 0 and liste[j-1] > liste[j]:
            liste[j-1], liste[j] = liste[j], liste[j-1]
            #  on deplace 2 par 2 les elements des 2 listes
            li[j-1], li[j] = li[j], li[j-1]
            j -= 1
    return liste, li


def moyenne_glissante(liste):
    moyenne = []
    for i in range(len(liste) - 1):
        moyenne.append((liste[i] + liste[i + 1]) / 2.0)
    moyenne.append((liste[-1]))
    return moyenne
