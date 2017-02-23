#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd
import sqlite3

conn = sqlite3.connect(r'student.db')
c = conn.cursor()

prep = "drop view MAX_TENTATIVE;\
				create view MAX_TENTATIVE as\
					select fk_nom_fichier, fk_id_activite, max(tentative) as tentative_max from STATS\
					where tentative > 0\
					group by fk_nom_fichier, fk_id_activite;"

#				where fk_id_activite in (2,12,15,17,20,22,23,28,29,33,36,40)\
req =  "select fk_id_activite, tentative_max, count(*) from MAX_TENTATIVE\
				group by fk_id_activite, tentative_max;"\


x = range(1,41)

tentative={}
tentative[1]=[0]*len(x)
tentative[2]=[0]*len(x)
tentative[3]=[0]*len(x)
tentative['b']=[0]*len(x)
totaux=[0]*len(x)

for row in c.execute(req):
	try:	
		act=row[0]
		tent=row[1]
		count=row[2]
		tentative[tent][act-1]=float(count)
		totaux[act-1]+=count
	except IndexError:
		print(row)

#normalisation
for i in x:
	for j in (1,2,3):
		try:
			tentative[j][i-1] = tentative[j][i-1] / totaux[i-1]
		except ZeroDivisionError:
			print('tentative',j,'activité',i)

#calcul des bottoms
for i in range(len(tentative[1])):
	tentative['b'][i]=tentative[1][i]+tentative[2][i]

#plt.bar(stacked=True)
plt.bar(x, tentative[1], color="green")
plt.bar(x, tentative[2], color="orange", bottom=tentative[1])
plt.bar(x, tentative[3], color="red", bottom=tentative['b'])

plt.xlabel('score')
plt.ylabel('population')

plt.title("Repartition du nombre de scores par individu et par sequence")
plt.show()
