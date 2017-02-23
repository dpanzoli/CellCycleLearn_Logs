#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd
import sqlite3
import matplotlib.ticker as mtick

conn = sqlite3.connect(r'student.db')
c = conn.cursor()

prep = "drop view MAX_TENTATIVE;\
				create view MAX_TENTATIVE as\
					select fk_nom_fichier, fk_id_activite, max(tentative) as tentative_max from STATS\
					where tentative > 0\
					group by fk_nom_fichier, fk_id_activite;"


req =  "select fk_id_activite, tentative_max, count(*) from MAX_TENTATIVE\
				where fk_id_activite in (2,12,15,17,20,22,23,28,29,33,36,40)\
				group by fk_id_activite, tentative_max;"\


xticks = [2,12,15,17,20,22,23,28,29,33,36,40]
x = range(len(xticks))

tentative={}
tentative[1]=[0]*len(x)
tentative[2]=[0]*len(x)
tentative[3]=[0]*len(x)
tentative['b']=[0]*len(x)
totaux=[0]*len(x)

for row in c.execute(req):
	try:	
		act=row[0]
		i_act = xticks.index(act)
		tent=row[1]
		count=row[2]
		tentative[tent][i_act]=float(count)
		totaux[i_act]+=count
	except IndexError:
		print(row)

#normalisation
for i in range(len(x)):
	for j in (1,2,3):
		try:
			tentative[j][i] = tentative[j][i] *100 / totaux[i]
		except ZeroDivisionError:
			print('tentative',j,'activité',i)

#calcul des bottoms
for i in range(len(tentative[1])):
	tentative['b'][i]=tentative[1][i]+tentative[2][i]

plt.xticks(x,xticks)

#plt.bar(stacked=True)
plt.bar(x, tentative[1], color="green", align='center')
plt.bar(x, tentative[2], color="orange", bottom=tentative[1], align='center')
plt.bar(x, tentative[3], color="red", bottom=tentative['b'], align='center')


fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
yticks = mtick.FormatStrFormatter(fmt)
ax = plt.gca()
ax.yaxis.set_major_formatter(yticks)



plt.xlabel('id activity')
plt.ylabel('attempts')

plt.title("Attempts by id activity")
plt.show()
