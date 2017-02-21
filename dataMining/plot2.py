import numpy as np
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect(r'student.db')
c = conn.cursor()

fig = plt.figure(figsize=(20,5))
ax = fig.add_subplot(111)
axis=[0]
y=[]
for i in range(3,90,3):
    x = i * 60
    cpt = 0
    for row in c.execute("SELECT fk_nom_fichier,sum(temps_tentative)as t from stats,activite where STATS.fk_id_activite = ACTIVITE.id_activite and ACTIVITE.fk_id_sequence = 2 group by fk_nom_fichier having t < ? and t>= ?",[x,x-180]):
        cpt+=1
    ax.bar(i,cpt,3,color='b')
plt.title("Sequence 1 : Temps moyen")
plt.grid(True)
plt.show()
fig.savefig("plot2b.png")
