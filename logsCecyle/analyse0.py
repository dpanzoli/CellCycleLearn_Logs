from os import listdir
from os.path import isfile, join
import re
import datetime

prog = re.compile('.*\.log')
cpt=0
table={}

for f in listdir("./logs/"):
        if isfile(join("./logs/", f)) and prog.match(f):
                cpt=cpt+1
                tab=f.split("_")
                if(len(tab[1]) >4):
                        t=int(tab[1])//1000
                else:
                        t=int(tab[2])//1000
                #print(datetime.datetime.fromtimestamp(t).strftime('%d/%m/%Y %H:%M:%S'))
                k = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')
                if not k in table:
                        table[k]=0
                table[k] += 1

for key in sorted(table):
    print (key, table[key])


