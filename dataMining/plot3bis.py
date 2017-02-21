from pylab import figure, show, legend, ylabel
import matplotlib.mlab as mlab
import sqlite3
 
conn = sqlite3.connect(r'student.db')
c = conn.cursor()

L=[]
sumL=0
for row in c.execute("select fk_nom_fichier, sum(temps_tentative) from STATS, ACTIVITE where STATS.fk_id_activite = ACTIVITE.id_activite and ACTIVITE.fk_id_sequence = 1 and fk_nom_fichier in (select distinct(fk_nom_fichier) from STATS where fk_id_activite = 20) group by fk_nom_fichier;"):
	L.append(row[1])
	sumL+=row[1]
ecarttypeL=0
moyenneL=sumL/len(L)
for l in L:
	ecarttypeL+=(l-moyenneL)**2
ecarttypeL=(ecarttypeL/len(L))**0.5

L2=[]
sumL2=0
for row in c.execute("select fk_nom_fichier, sum(temps_tentative) from STATS, ACTIVITE where STATS.fk_id_activite = ACTIVITE.id_activite and ACTIVITE.fk_id_sequence = 2 and fk_nom_fichier in (select distinct(fk_nom_fichier) from STATS where fk_id_activite = 40) group by fk_nom_fichier;"):
	L2.append(row[1])
	sumL2+=row[1]
ecarttypeL2=0
moyenneL2=sumL2/len(L2)
for l in L2:
	ecarttypeL2+=(l-moyenneL2)**2
ecarttypeL2=(ecarttypeL2/len(L2))**0.5


# create the general figure
fig1 = figure()

# and the first axes using subplot populated with data 
ax1 = fig1.add_subplot(111)
#n, bins, patches = ax1.hist(L, 30, facecolor='grey', alpha=1)
n, bins, patches = ax1.hist(L2, 30, facecolor='grey', alpha=1)
ylabel("Population (n)")
ax1.yaxis.tick_left()
ax1.yaxis.set_label_position("left")
ax1.set_xlabel("Time (s)")

# now, the second axes that shares the x-axis with the ax1
ax2 = fig1.add_subplot(111, sharex=ax1, frameon=False)
#y = mlab.normpdf( bins, moyenneL, ecarttypeL)
#line2 = ax2.plot(bins, y, 'r--', linewidth=2)
y = mlab.normpdf( bins, moyenneL2, ecarttypeL2)
line2 = ax2.plot(bins, y, 'r--', linewidth=2)
ylabel("")
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")

# for the legend, remember that we used two different axes so, we need 
# to build the legend manually
#legend((bins1, line2), ("1", "2"))
show()
