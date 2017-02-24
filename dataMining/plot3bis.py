from pylab import figure, show, legend, ylabel
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import sqlite3
import numpy as np
 
conn = sqlite3.connect(r'student.db')
c = conn.cursor()

requete1 = "select fk_nom_fichier, sum(temps_tentative) from STATS, ACTIVITE\
					where STATS.fk_id_activite = ACTIVITE.id_activite\
					and ACTIVITE.fk_id_sequence = 1\
					and fk_nom_fichier in (select distinct(fk_nom_fichier)\
							from STATS where fk_id_activite = 20)\
					group by fk_nom_fichier;"

requete2 = "select fk_nom_fichier, sum(temps_tentative) from STATS, ACTIVITE\
					where STATS.fk_id_activite = ACTIVITE.id_activite\
					and ACTIVITE.fk_id_sequence = 2\
					and fk_nom_fichier in (select distinct(fk_nom_fichier)\
							from STATS where fk_id_activite = 40)\
					group by fk_nom_fichier;"


L=[]
sumL=0
for row in c.execute(requete1):
	L.append(row[1])
	sumL+=row[1]
ecarttypeL=0
moyenneL=sumL/len(L)
for l in L:
	ecarttypeL+=(l-moyenneL)**2
ecarttypeL=(ecarttypeL/len(L))**0.5


# create the general figure
fig1 = figure()

# and the first axes using subplot populated with data 
ax1 = fig1.add_subplot(111)
#n, bins, patches = ax1.hist(L, 30, facecolor='grey', alpha=1)
n, bins, patches = ax1.hist(L, 30, facecolor='gray', alpha=0.5)
ylabel("Population (n)")
ax1.yaxis.tick_left()
ax1.yaxis.set_label_position("left")
ax1.set_xlabel("Time (s)")

# now, the second axes that shares the x-axis with the ax1
ax2 = fig1.add_subplot(111, sharex=ax1, frameon=False)
#y = mlab.normpdf( bins, moyenneL, ecarttypeL)
#line2 = ax2.plot(bins, y, 'r--', linewidth=2)
y = mlab.normpdf( bins, moyenneL, ecarttypeL)
line2, = ax2.plot(bins, y, 'b--', linewidth=2)
ylabel("")
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
ax2.set_yticks(np.arange(0.0000, 0.0006, 0.0001))

plt.legend([patches[0], line2], ["Population/time slice", "Gaussian fit"], loc=1, frameon=False)
show()
