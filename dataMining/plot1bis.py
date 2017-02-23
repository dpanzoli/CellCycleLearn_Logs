#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import math


conn = sqlite3.connect(r'student.db')
c = conn.cursor()

"""
req="select fk_nom_fichier, fk_id_activite, sum(temps_tentative) as temps_total\
			from STATS \
			where tentative>0 \
			and fk_nom_fichier in (\
					select LOGS.nom_fichier from LOGS, LOGS as LOG2, ETUDIANT\
					where LOGS.fk_id_etudiant = ETUDIANT.id_etudiant\
					and LOG2.fk_id_etudiant = LOGS.fk_id_etudiant\
					and LOGS.fk_sequence = 1\
					and LOG2.fk_sequence = 2)\
			group by fk_nom_fichier, fk_id_activite;"
"""
req="select fk_nom_fichier, fk_id_activite, sum(temps_tentative) as temps_total\
			from STATS \
			where tentative>0 \
			group by fk_nom_fichier, fk_id_activite;"

activites={}
moyennes={}

for row in c.execute(req):
	act=row[1]
	temp=row[2]
	if act not in activites:
		activites[act]=[]
		moyennes[act]=0
	activites[act].append(temp)
	moyennes[act] += temp

#calul des moyennes
for k in moyennes.keys():
	moyennes[k] /= len(activites[k])

ind = []
means = []
std = []

for k in activites.keys():
	print(k, activites[k])

#calcul des écart-types
for k in activites.keys():
	L = activites[k]
	e = 0;
	m = moyennes[k]
	for l in L:
		e += (l-m)**2
	e = (e/len(L))**0.5
	#print(k, moyennes[k], e)
	ind.append(k)
	means.append(moyennes[k])
	std.append(e)

fig = plt.figure(figsize=(10,15))

#N = 5
#menMeans   = (20, 35, 30, 35, 27)
#menStd     = (2, 3, 4, 1, 2)
#ind = np.arange(N)    # the x locations for the groups

width = 0.9
p1 = plt.barh(ind, means, width, color='#c0c0c0', xerr=std, align='center')
plt.gca().invert_yaxis()
plt.xlim((-0,1000))
plt.ylim((-1,41))
plt.ylabel('Activity id')
plt.xlabel('Time (s)')
plt.title('Time per activity')
#plt.xticks(ind+width/2., ('G1', 'G2', 'G3', 'G4', 'G5') )
plt.yticks(activites.keys(), )
#plt.legend( [p1[0]], ['Time (s)'] )

plt.tight_layout()
plt.show()
#fig.savefig("plot1.png")
