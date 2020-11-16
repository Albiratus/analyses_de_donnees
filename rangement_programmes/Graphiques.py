#liste des abscisses = la 1ère de matplot = x
#liste des ordonnées = la 2ème de matplot = y
import matplotlib.pyplot as plt

with open ('projet.csv','r') as file :
    for line in file :
        print(line)

plt.title("titre_graphique")
plt.plot([1,2,4,6],[2,4,6,8], "g--", linewidth = 2)
plt.xlabel("nom_axe_abscisses")
plt.ylabel("nom_axe_ordonnés")
# pour limiter la longueur du graphique
plt.axis([borne 1 axe abscisse, borne 2, borne 1 axe ordonnées, borne 2])
# pour montrer le graphique
plt.show()