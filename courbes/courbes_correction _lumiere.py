from horaires.anomalies_lumiere import oublie_lumiere
from variables.variables import temps_tries, LUM
import matplotlib.pyplot as plt


tps_corrig = []
point_lum_anomalique = []
#  on parcoure les indices défectueux
for k in oublie_lumiere(LUM)[0]:
    #  on recupere les instants ainsi que les points lumineux correspondant
    tps_corrig.append(temps_tries[k])
    point_lum_anomalique.append(LUM[k])

plt.subplot(211)
plt.plot(temps_tries, LUM)
# points défectueux en rouge
plt.scatter(tps_corrig, point_lum_anomalique, color='red')
plt.subplot(212)
# correction
plt.plot(temps_tries, oublie_lumiere(LUM)[1])
plt.show()
