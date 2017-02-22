import numpy as np
import matplotlib.pyplot as plt
import sqlite3



conn = sqlite3.connect(r'student.db')
c = conn.cursor()
fig = plt.figure(figsize=(40,10))
ax = fig.add_subplot(111)
x=[]
y=[]
requete = c.execute("select fk_id_activite,avg(temps_tentative) from activite,stats " +
 "where STATS.fk_id_activite = ACTIVITE.id_activite and type != 'Transition' and fk_id_section != 1 and tentative = -1 "
  +"group by fk_id_activite")
for row in requete:
    y.append(row[0])
    x.append(row[1])
yvals = range(len(y))
ax.barh(yvals,x,0.75,align='center',color=['r','b','g','#12345678'])
plt.title("Temps passé sur une fiche mémo après un retour en arrière")

plt.yticks(yvals,y)
plt.xlabel("Temps passé")
plt.ylabel("ID de l'acitivté")
#plt.show()
fig.savefig("plot6.png")
