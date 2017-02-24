#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import csv
import matplotlib.ticker as mtick

conn = sqlite3.connect(r'student.db')
c = conn.cursor()
x=[]
y=[]

data={}

individus = []
for row in c.execute("select distinct(fk_nom_fichier) from STATS where fk_id_activite=20;"):
		individus.append(row[0])

activites = []
scores_max = []
for row in c.execute("select id_activite, score_max from ACTIVITE where score_max>0 and fk_id_sequence=1;"):
		activites.append(row[0])
		scores_max.append(row[1])

#dummy data
#cecyle_1480349705096----(1, 90000, 1.0)
#cecyle_1480954372118----(3, 80000, 0.2962962962962963)
#cecyle_1480954432722----(2, 90000, 0.5)

#individus=['cecyle_1480349705096','cecyle_1480954372118','cecyle_1480954432722']
#activites=[2,9,10]
#scores_max=[90000,40000,10000]

for ind in individus:
	score_somme=0
	for i in range(len(activites)):
		act = activites[i]
		score_max = scores_max[i]
		subreq = "select fk_nom_fichier, max(tentative), score from STATS where fk_id_activite="+str(act)+" and fk_nom_fichier='"+ind+"';"
		#print("---"+ind+"----")
		for tentative in c.execute(subreq):
			try:		
				tent = tentative[1]
				score = float(tentative[2])/score_max/tent
				score_somme += score
				#print(tentative[1], tentative[2], score)
			except TypeError:
				pass
			except IndexError:
				pass
				#print("n/a")
		#print("-------")
	score_somme /= len(activites)	
	#print(ind, score_somme)
	data[ind]=[score_somme,0]


#Récupération maintenant des temps de jeu.
requete="select fk_nom_fichier, sum(temps_tentative) as temps_total\
			from STATS \
			group by fk_nom_fichier"

for row in c.execute(requete):
	ind=row[0]
	temps=row[1]
	if ind in data:
		data[ind][1] = temps

x=[]
y=[]
#création des séries
for k in data.keys():
	d = data[k]
	x.append(d[1])
	y.append(d[0]*100)


#print(x,y)

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)
ax.plot(x,y, 'D')

ax.set_xlim(0,)

fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
yticks = mtick.FormatStrFormatter(fmt)
ax.set_ylim(0,100)
ax.set_yticks(np.arange(0,100,10))
ax.yaxis.set_major_formatter(yticks)
ax.set_ylabel("Score (%)")
ax.set_xlabel("Times (s)")
plt.tight_layout()
plt.show()













