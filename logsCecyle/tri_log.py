from os import listdir
import os
from os import rename
from os.path import isfile, join
import re
import sys
import datetime

cpt=0
table={}

for f in listdir("./logsUPSCUFR/"):
        if isfile(join("./logsUPSCUFR/", f)):
               if os.path.getsize('C:\\Users\\stage\\Desktop\\Stage_Marvyn\\CellCycleLearn_Logs\\logsCecyle\\logsUPSCUFR\\'+str(f)) <= 20:
##                       tab=f.split("_")
##                        t=tab[0]
##                        if not t in table:
##                                d = int(tab[1])//1000
##                                date = datetime.datetime.fromtimestamp(d).strftime('%Y-%m-%d')
##                                table[t]=[0,date]
##                        table[t][0]+=1
                       if not os.path.exists('C:\\Users\\stage\\Desktop\\Stage_Marvyn\\CellCyclelearn_Logs\\logsCecyle\\logs\\'+str(f)):
                               rename('C:\\Users\\stage\\Desktop\\Stage_Marvyn\\CellCyclelearn_Logs\\logsCecyle\\logsUPSCUFR\\'+str(f),'C:\\Users\\stage\\Desktop\\Stage_Marvyn\\CellCyclelearn_Logs\\logsCecyle\\logs\\'+str(f))  
                        
##for key in sorted(table):
##    if table[key][0]  >= 4 : #and sys.argv[2] == table[key][1]:
##        rename('C:\\Users\\stage\\Desktop\\Stage_Marvyn\\logsCecyle\\logsUPSCUFR\\'+str(f),'C:\\Users\\stage\\Desktop\\Stage_Marvyn\\logsCecyle\\logs\\'+str(f))
##        print(key)
##print(cpt)
