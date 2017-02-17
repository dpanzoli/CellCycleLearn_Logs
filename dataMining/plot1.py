import numpy as np
import matplotlib.pyplot as plt
import sqlite3


conn = sqlite3.connect(r'../logsCecyle/student.db')
c = conn.cursor()

fig = plt.figure(figsize=(40,10))
ax = fig.add_subplot(111)
ticks = []
labels=[]
i=0
x = 0
for row in c.execute("SELECT ACTIVITE.lib_activite,avg(STATS.temps_tentative) from STATS,ACTIVITE where STATS.id_activite = ACTIVITE.key_activite group by STATS.id_activite"):
    y = row[1]
    ax.barh(i,y,height=0.8,left=x)
    ticks.append(i+0.5)
    labels.append(row[0])
    i = i+1
plt.yticks(ticks, labels)
plt.xticks((0,30,60,90,120,150,180,210,240,270,300,330,360,390,420),('0','30sec','1 min','1min30','2min','2min30','3min','3min30','4min','4min30','5min','5min30','6min','6min30','7min'))
fig.savefig("plot1.png")
