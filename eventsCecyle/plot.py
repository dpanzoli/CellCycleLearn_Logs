#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from datetime import *
import csv

#scores = [500,100,300,400]


fig = plt.figure(figsize=(20,10))
ticks=[]
labels=[]

for i in range(0,17):
	try:	
		csv_reader = csv.reader(open('events/data'+str(i+1)+'.csv'))
		ax = fig.add_subplot(111)
		for line in csv_reader:
			x=int(line[0])
			print(line)
			d=int(line[1])
			ax.barh(i+0.1, d, height=.8, left=x, color=line[3])
		ticks.append(i+0.5)
		#labels.append('champo'+str(i+1)+'(score='+str(scores[i])+')')
		labels.append('champo_'+str(i+1))
	except :
		print("probleme avec "+str(i))

plt.yticks( ticks, labels )
plt.xticks( (0,900,1800,2700,3600), ('0','0h15','0h30', '0h45', '1h'))


plt.show()

