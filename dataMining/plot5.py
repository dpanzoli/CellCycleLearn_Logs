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
	z.append(row[1]+random.randrange(-10,10))
	t.append(i)
	i=i+1

yvals = range(len(y))

diamonds, = plt.plot(z, t, 'd', markersize=12)
bars = plt.barh(yvals,x,0.75,align='center',color='#c0c0c0')

#plt.title("Time spent reading the memo sheet (per activity)")

plt.xticks([0,60,120,180,240,300])
plt.yticks(yvals,y)
plt.ylim((-1,len(yvals)+1))

plt.xlabel("Time (s)")
plt.ylabel("Activity id")

plt.legend([bars, diamonds], ["Average actual time", "Expected time"])
#plt.legend(handles=[red_patch, blue_line])

plt.tight_layout()
#plt.show()
fig.savefig("plot5.pdf")
