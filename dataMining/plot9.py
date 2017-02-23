#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd
import sqlite3

conn = sqlite3.connect(r'student.db')
c = conn.cursor()

req = "select nb_scores,count(fk_nom_fichier) from (\
					select fk_nom_fichier, count(score) as nb_scores from STATS\
					where fk_nom_fichier in (\
						select nom_fichier from LOGS\
						where fk_sequence = 1)\
					group by fk_nom_fichier)\
				group by nb_scores;"

req2 = "select nb_scores,count(fk_nom_fichier) from (\
					select fk_nom_fichier, count(score) as nb_scores from STATS\
					where fk_nom_fichier in (\
						select nom_fichier from LOGS\
						where fk_sequence = 2)\
					group by fk_nom_fichier)\
				group by nb_scores;"

x=range(0,40)
y=[0]*len(x)
z=[0]*len(x)

for row in c.execute(req):
	y[row[0]]=row[1]
	
for row in c.execute(req2):
	z[row[0]]=row[1]

fig, ax = plt.subplots()

line1, = ax.plot(x, y)
line2, = ax.plot(x, z)

plt.xlabel('score')
plt.ylabel('population')

plt.title("Repartition du nombre de scores par individu et par sequence")
plt.show()
