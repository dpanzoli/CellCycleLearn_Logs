#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import random
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.markers as mmarkers

conn = sqlite3.connect(r'student.db')
c = conn.cursor()
fig = plt.figure(figsize=(10,7))

dico = {}
dico[2]=41.5
dico[7]=27.75
dico[8]=25.25
dico[9]=40.25
dico[10]=22.25
dico[11]=12.25
dico[12]=59
dico[15]=17.5
dico[16]=19.25
dico[17]=30.25
dico[18]=34.75
dico[22]=80.5
dico[23]=36
dico[28]=47.5
dico[29]=26.5
dico[30]=51.25
dico[31]=9.75
dico[32]=58.75
dico[33]=40.25
dico[36]=20.25
dico[37]=18.5
dico[38]=19.25



t=[]
x=[]
y=[]
z=[]
requete = c.execute("select fk_id_activite,avg(temps_tentative) from activite,stats " +
 "where STATS.fk_id_activite = ACTIVITE.id_activite and type != 'Transition' and fk_id_section != 1 and (tentative = 0 or (type = 'Fiche Mémo' and tentative =1)) "
  +"group by fk_id_activite")
i=0
for row in requete:
	y.append(row[0])
	x.append(row[1])
#	z.append(row[1]+random.randrange(-10,10))
	if row[0] in dico:
		z.append(dico[row[0]])
	else:
		z.append(-10)
	t.append(i)
	i=i+1

yvals = range(len(y))

diamonds, = plt.plot(z, t, 'd', markersize=12)
bars = plt.barh(yvals,x,0.75,align='center',color='#c0c0c0')

#plt.title("Time spent reading the memo sheet (per activity)")

plt.xticks([0,30,60,90,120,150])
plt.xlim(0,150)
plt.yticks(yvals,y)
plt.ylim((-1,len(yvals)+1))

plt.xlabel("Time (s)")
plt.ylabel("Activity id")

plt.legend([bars, diamonds], ["Average actual time", "Expected time"])
#plt.legend(handles=[red_patch, blue_line])

plt.tight_layout()
#plt.show()
fig.savefig("plot5.png")
