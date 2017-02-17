from os import listdir
from os.path import isfile, join
import re
import datetime
import sys

prog = re.compile('.*\.log')
cpt=0
table={}

if len(sys.argv)<2:
	sys.exit(-1)
else:
	date=sys.argv[1]
	print("fichiers de log à la date du",date)

for f in listdir("./logs/"):
	if isfile(join("./logs/", f)) and prog.match(f):
		cpt=cpt+1
		tab=f.split("_")
		t=int(tab[1])//1000
		user=tab[0]
		#print(datetime.datetime.fromtimestamp(t).strftime('%d/%m/%Y %H:%M:%S'))
		k = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')
		if not k in table:
			table[k]=set()
		table[k].add(user)

for key in sorted(table):
    print (key, table[key])


