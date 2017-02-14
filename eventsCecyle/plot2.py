#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from datetime import *
import csv

fig = plt.figure(figsize=(20,5))
ticks=[]
labels=[]
for j in range(0,17):
        try:
                csv_reader = csv.reader(open('events/data'+str(j+1)+'.csv'))
                ax = fig.add_subplot(111)
                i=0
                for line in csv_reader:
                        x=int(line[0])
                        d=int(line[1])
                        #plt.axhline(y=i+0.5, color="#aaaaaa")	
                        ax.barh(i, d, height=.8, left=x, color=line[3])
                        ticks.append(i+0.5)		
                        labels.append(line[2])
                        
                        i=i+1
                plt.yticks( ticks, labels )
                plt.xticks( (0,900,1800,2700,3600), ('0','0h15','0h30', '0h45', '1h'))
                fig.savefig('figure2_event1/users'+str(j+1)+'.png')
                fig.delaxes(ax)
                label = []
                ticks = []
        except:
                print("probleme avec" + str(j))


