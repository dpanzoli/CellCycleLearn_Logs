import numpy as np
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect(r'student.db')
c = conn.cursor()
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)
x=[]
y=[]
requete = c.execute("select TEMPS.fk_nom_fichier,t,sum(s) from (select fk_nom_fichier,sum(temps_tentative) as t from stats where fk_id_activite <=20 group by fk_nom_fichier) as temps " +
                    ",(select fk_nom_fichier,fk_id_activite,max(tentative),score as s from stats where fk_id_activite <=20 group by fk_nom_fichier,fk_id_activite) as score " +
                    "where TEMPS.fk_nom_fichier = SCORE.fk_nom_fichier group by TEMPS.fk_nom_fichier")
for row in requete:
    y.append(row[2])
    x.append(row[1])
plt.scatter(x,y)
plt.title("Score/Temps par personne")
plt.xlabel("Temps passé")
plt.ylabel("Score")
#plt.show()
fig.savefig("plot8a.png")