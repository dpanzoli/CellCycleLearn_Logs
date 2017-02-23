#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd
import sqlite3
import matplotlib.ticker as mtick
from matplotlib import gridspec

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


xticks = {}
xticks[1] = [2,12,15,17,20]
xticks[2] = [22,23,28,29,33,36,40]

x = {}
x[1] = range(len(xticks[1]))
x[2] = range(len(xticks[2]))

sequence = {}
sequence[1]={}
sequence[2]={}

totaux = {}

for s in (1,2):
	sequence[s]={}
	sequence[s][1]=[0]*len(x[s])
	sequence[s][2]=[0]*len(x[s])
	sequence[s][3]=[0]*len(x[s])
	sequence[s]['b']=[0]*len(x[s])
	totaux[s]=[0]*len(x[s])

for row in c.execute(req):
	try:	
		act=row[0]
		if (act>20):
			seq=2
		else:
			seq=1
		i_act = xticks[seq].index(act)
		tent=row[1]
		count=row[2]
		sequence[seq][tent][i_act]=float(count)
		totaux[seq][i_act]+=count
	except IndexError:
		print(row)
	except KeyError:
		print(row)	

#normalisation
for s in (1,2):
	for i in range(len(x[s])):
		for j in (1,2,3):
			try:
				sequence[s][j][i] = sequence[s][j][i] *100 / totaux[s][i]
			except ZeroDivisionError:
				print('tentative',j,'activité',i)

#calcul des bottoms
for s in (1,2):
	tentative = sequence[s]
	for i in range(len(tentative[1])):
		tentative['b'][i]=tentative[1][i]+tentative[2][i]

# Two subplots, unpack the axes array immediately
#f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
fig = plt.figure(figsize=(8, 4)) 
gs = gridspec.GridSpec(1, 2, width_ratios=[len(xticks[1]), len(xticks[2])]) 
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])

#plt.bar(stacked=True)
t1=ax1.bar(x[1], sequence[1][1], color="gray", alpha=0.4, linewidth=0, align='center')
t2=ax1.bar(x[1], sequence[1][2], color="gray", alpha=0.7, linewidth=0, bottom=sequence[1][1], align='center')
t3=ax1.bar(x[1], sequence[1][3], color="gray", alpha=1, linewidth=0, bottom=sequence[1]['b'], align='center')

ax2.bar(x[2], sequence[2][1], color="gray", alpha=0.4, linewidth=0, align='center')
ax2.bar(x[2], sequence[2][2], color="gray", alpha=0.7, linewidth=0, bottom=sequence[2][1], align='center')
ax2.bar(x[2], sequence[2][3], color="gray", alpha=1, linewidth=0, bottom=sequence[2]['b'], align='center')

ax1.set_xticks(x[1])
ax1.set_xticklabels(xticks[1])
ax2.set_xticks(x[2])
ax2.set_xticklabels(xticks[2])
fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
yticks = mtick.FormatStrFormatter(fmt)
#ax = plt.gca()
ax1.yaxis.set_major_formatter(yticks)
ax2.set_yticklabels([])

#plt.xlabel('id activity')
ax1.set_ylabel('#attempt distribution')
ax1.set_xlabel('activity id')
ax2.set_xlabel('activity id')
ax1.set_title("Sequence 1")
ax2.set_title("Sequence 2")

plt.legend([t1, t2, t3], ["Activity won on $1^{st}$ attempt", "On $2^{nd}$ attempt", "On $3^{rd}$ attempt"], loc='upper center', bbox_to_anchor=(0.1, -0.1), ncol=3, frameon=False)


plt.tight_layout()
plt.show()




