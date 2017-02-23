import numpy as np
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect(r'student.db')
c = conn.cursor()
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)
d={}
requete = c.execute("select TEMPS.fk_nom_fichier,SCORE.fk_id_activite,t,s,tent from (select fk_nom_fichier,sum(temps_tentative) as t from stats where fk_id_activite <=20 group by fk_nom_fichier) as temps " +
                    ",(select fk_nom_fichier,fk_id_activite,max(tentative) as tent,score as s from stats where fk_id_activite <=20 group by fk_nom_fichier,fk_id_activite) as score " +
                    "where TEMPS.fk_nom_fichier = SCORE.fk_nom_fichier and TEMPS.fk_nom_fichier in( select distinct (fk_nom_fichier)from stats where fk_id_activite=20) and s >=0 group by TEMPS.fk_nom_fichier,SCORE.fk_id_activite")
for row in requete:
        print(row)
##    if row[0] not in d:
##        d[row[0]]=[0,row[3]]
##    if row[1] == 1:
##        d[row[0]][0]+=score
##    elif row[1] == 2:
        
##plt.scatter(x,y)
##plt.title("Score/Temps par personne")
##plt.xlabel("Temps passé")
##plt.ylabel("Score")
##plt.show()
#fig.savefig("plot10a.png")
