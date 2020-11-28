from fonctions_utiles.fonctions_stats import tri_insert


#  renvoie la valeur de l'indice du 3eme quartile
def troisiemequartile(liste):
    if len(liste) < 1:
        return None
    else:
        if len(liste) % 4 == 0:
            a = 3*len(liste)/4 - 1
            return int(a)
        else:
            b = 3*(len(liste)/4)
            return int(b)


#  renvoie l'indice du 1er quartile
def premierquartile(liste):
    if len(liste) < 1:
        return None
    else:
        if len(liste) % 4 == 0:
            a = (len(liste))/4 - 1
            return int(a)
        else:
            b = len(liste)/4
            return int(b)


#  selectionne seulement les valeurs qui semblent coherentes et renvoies egalement les indices anormales
def ejecter_anomalies(liste):
    #  liste etant evidemment triee en fonction du temps
    liste_sans_anomalies = []
    indice_sans_anomalies = []
    indices_anormales = []
    #  tri de liste en fonction de ses valeurs
    liste_triee = tri_insert(liste)[0]
    valeur1quart = liste_triee[premierquartile(liste)]
    valeur3quart = liste_triee[troisiemequartile(liste)]
    ecart_inter_quart = valeur3quart - valeur1quart
    #  determination des valeurs basses et hautes à garder
    valeur_basse = valeur1quart - 1.5 * ecart_inter_quart
    valeur_haute = valeur3quart + 1.5 * ecart_inter_quart
    #  renvoie la liste entre les deux valeurs statistiques et les indices anormales
    for k in range(len(liste)):
        if valeur_basse <= liste[k] <= valeur_haute:
            liste_sans_anomalies.append(liste[k])
            indice_sans_anomalies.append(k)
        else:
            indices_anormales.append(k)
    return liste_sans_anomalies, indices_anormales, indice_sans_anomalies
