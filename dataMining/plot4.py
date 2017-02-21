import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import math


conn = sqlite3.connect(r'student.db')
c = conn.cursor()

fig = plt.figure(figsize=(40,10))
ax = fig.add_subplot(111)
x=[]
y=[]
c.execute("drop view if exists TENTATIVES;")
c.execute("create view TENTATIVES as "+
 "select fk_nom_fichier, fk_id_activite, count(*) as nb_tentatives from STATS "+
 "where tentative > 0 " +
 "group by fk_nom_fichier, fk_id_activite")
for row in c.execute("select fk_id_activite, avg(nb_tentatives) from ACTIVITE,TENTATIVES " +
 " where fk_id_section != 1 and type != 'Transition' and type != 'Fiche Mémo' and ACTIVITE.chrono =0 and ACTIVITE.id_activite = TENTATIVES.fk_id_activite "
                     +"group by fk_id_activite;"):
    y.append(row[0])
    x.append(row[1])
yvals = range(len(y))
ax.barh(yvals,x,0.75,align='center',color=['r','b','g','#12345678'])
plt.title("Nombre de tentatives moyenne par épreuves")

plt.yticks(yvals,y)
plt.xlabel("Nombre de tentatives moyenne")
plt.ylabel("ID de l'acitivté")
fig.savefig("plot4.png")
