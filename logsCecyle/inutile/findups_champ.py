from os import listdir
from os import rename
from os.path import isfile, join
import re
import sys
import datetime

prog = re.compile('.*\.logs')
cpt=0
table={}

for f in listdir("./logs/"):
        if isfile(join("./logs/", f)) and prog.match(f):
                tab=f.split("_")
                if(len(tab[1]) >4):
                        t=int(tab[1])//1000
                else:
                        t=int(tab[2])//1000
                #print(datetime.datetime.fromtimestamp(t).strftime('%d/%m/%Y %H:%M:%S'))
                k = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')
                if k in sys.argv[1]:
                        cpt+=1
                        rename('C:\\Users\\stage\\Desktop\\Stage_Marvyn\\logsCecyle\\logs\\'+str(f),'C:\\Users\\stage\\Desktop\\Stage_Marvyn\\logsCecyle\\logsUPSCUFR\\'+str(f))
print(cpt)
