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
c.execute("drop view TENTATIVES;")
c.execute("create view TENTATIVES as "+
 "select fk_nom_fichier, fk_id_activite, count(*) as nb_tentatives from STATS "+
 "where tentative > 0 " +
 "group by fk_nom_fichier, fk_id_activite")
for row in c.execute("select fk_id_activite, avg(nb_tentatives) from TENTATIVES " +
 "group by fk_id_activite;"):
    x.append(row[0])
    y.append(row[1])
ax.bar(x,y,0.5,color='b')
plt.title("Nombre de tentatives moyenne par épreuves")
plt.xlabel("Id de l'activité")
plt.ylabel("Nombre de tentatives moyenne")
fig.savefig("plot4.png")
