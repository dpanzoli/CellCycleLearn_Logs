import numpy as np
import matplotlib.pyplot as plt
import sqlite3


conn = sqlite3.connect(r'../logsCecyle/student.db')
c = conn.cursor()

fig = plt.figure(figsize=(40,10))
ax = fig.add_subplot(111)
ticks = []
labels=[]
test1 = []
test2 = []
i=0
x = 0
for row in c.execute("SELECT ACTIVITE.lib_activite,avg(STATS.temps_tentative),1 from STATS,ACTIVITE where STATS.key_activite = ACTIVITE.key_activite group by STATS.key_activite"):
    y = row[1]
    print(row[2])
    test1.append(row[1])
    test2.append(row[2])
    ax.barh(i,y,height=0.8,left=x)
    ticks.append(i+0.5)
    labels.append(row[0])
    i = i+1
plt.errorbar(test1,test2,xerr = ticks,yerr = [0]*len(test1),linestyle='None',marker='^')
plt.yticks(ticks, labels)
plt.xticks((0,30,60,90,120,150,180,210,240,270,300,330,360,390,420),('0','30sec','1 min','1min30','2min','2min30','3min','3min30','4min','4min30','5min','5min30','6min','6min30','7min'))
fig.show()
#fig.savefig("plot1.png")
