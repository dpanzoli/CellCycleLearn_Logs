#!/usr/bin/env python3

import json
from datetime import datetime
import csv
import sys

#Prérequis : #ffde00 - 255 222 0
#Hypothèses : #ffa200 - 255 162 0
#Protocole : #f30279 - 243 2 121
#Résultats : #aa00d5 - 170 0 213
#Synthèse : #0028d5 - 0 40 213

dico = {}
dico[0]={}
dico[0][-1]=["transition : prérequis", "#ffde00"]
dico[0][0]=["prérequis 1", "#ffde00"]
dico[0][1]=["prerequis 2","#ffde00"]
dico[1]={}
dico[1][-1]=["transition : hypothèses", "#ffa200"]
dico[1][0]=["hypothèse 1", "#ffa200"]
dico[1][1]=["hypothèse 2", "#ffa200"]
dico[2]={}
dico[2][-1]=["transition : protocole", "#f30279"]
dico[2][0]=["planification", "#f30279"]
dico[2][1]=["nombre de boîtes", "#f30279"]
dico[2][2]=["densite cellulaire", "#f30279"]
dico[2][3]=["nombre de cellule par boite/taille boîtes", "#f30279"]
dico[2][4]=["ensencement", "#f30279"]
dico[2][5]=["changement de milieu", "#f30279"]
dico[3]={}
dico[3][-1]=["transition : expérience", "#0028D5"]
dico[4]={}
dico[4][-1]=["transition : résultats", "#aa00d5"]
dico[4][0]=["profils de cytométrie", "#aa00d5"]
dico[4][1]=["chekpoint influancé par la privation", "#aa00d5"]
dico[4][2]=["profils de cytometrie et courbe d'évolution dans une phase", "#aa00d5"]
dico[5]={}
dico[5][-1]=["transition : synthèse", "#0028d5"]
dico[5][0]=["synthèse", "#0028d5"]

def time_decode(timeStampZero, timeStamp):
	dateZ = datetime.fromtimestamp(timeStampZero//1000)
	date = datetime.fromtimestamp(timeStamp//1000)
	return date-dateZ
with open('events2/champo_'+str(sys.argv[1])+'.log') as data_file:    
    data = json.load(data_file)

print (len(data['events']), "events loaded")

f = open('events2/data'+str(sys.argv[1])+'.csv', 'w')
fcsv = csv.writer(f, lineterminator='\n')

firstEvent=data['events'][0] # on récupère le premier event
#print(time_decode(firstEvent['timestamp'], firstEvent['timestamp']),dico[0][-1][0])


section=int(firstEvent['section_id']) #on récupère l'id de la section
activity=int(firstEvent['activity_id']) #on récupère l'id de l'activité
activities=[]
activities.append([0, -1, dico[0][-1][0], dico[0][-1][1]]) #On ajoute l'activité participé + couleur
for event in data['events']: #Pour tout les events dans le json
	#récup de l'activité par le dico	
	try:
		act=dico[int(event['section_id'])][int(event['activity_id'])] #On récupère le chapitre où il est
	except KeyError:
		act="unknown"	
        #Si l'activité actuelle est moins recente que l'ancienne alors 
	if (section==int(event['section_id']) and activity>int(event['activity_id'])) or section>int(event['section_id']):
		i=0
		#print("retour en arrière sur", event['section_id'], event['activity_id'])
	else:
                #Si on est pas sur la meme section ou si on est pas sur la meme activity
		if section!=int(event['section_id']) or activity!=int(event['activity_id']):
			#print(time_decode(firstEvent['timestamp'], event['timestamp']),act[0])
                        #On ajoute dans activites le temps écoulé et le nom de l'activité + couleur
			activities.append([time_decode(firstEvent['timestamp'], event['timestamp']).seconds, -1, act[0], act[1]])
		section=int(event['section_id'])
		activity=int(event['activity_id'])
		
#Calcul des durées et export csv
for i in range(0, len(activities)-1):
        #On regarde combien de temps chaque activité à duré et on l'écris dans le csv
	activities[i][1]=activities[i+1][0]-activities[i][0]
	fcsv.writerow(activities[i])

#durée de la synthèse
#i) récup du timestamp du dernier evenement
lastEvent=data['events'][len(data)-1]
dureeLastEvent=time_decode(firstEvent['timestamp'], event['timestamp']).seconds
activities[len(activities)-1][1]=dureeLastEvent-activities[len(activities)-1][0]
fcsv.writerow(activities[len(activities)-1])

f.close()
