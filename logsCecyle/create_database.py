import sqlite3
from os import listdir
import os
from os import rename
from os.path import isfile, join
import re
import sys
import json
import datetime

conn = sqlite3.connect(r'C:\\Users\\stage\\Desktop\\Stage_Marvyn\\logsCecyle\\student.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS ETUDIANT ''')
c.execute('''DROP TABLE IF EXISTS LOGS ''')
#Création de la table Etudiant
c.execute('''CREATE TABLE ETUDIANT
            (student_id VARCHAR PRIMARY KEY, univ VARCHAR)''')
#Création de la table Logs avec une clé étrangère qui est la clé principale de la table ETUDIANT
c.execute('''CREATE TABLE LOGS
            (nom_fichier VARCHAR PRIMARY KEY,student_id VARCHAR, sequence INTEGER,
            heure_debut_event INTEGER, heure_fin_event INTEGER, duree_event INTEGER,
            heure_debut_input INTEGER,heure_fin_input INTEGER, duree_input INTEGER,
            jour VARCHAR,mois VARCHAR,annee VARCHAR,
            FOREIGN KEY(student_id) REFERENCES ETUDIANT(student_id))''')


#~~Remplissage de la table ~~
i=0
for f in listdir("./logsUPSCUFR/"):
    if isfile(join("./logsUPSCUFR/",f)):
        #On vire les fichiers inutiles
        tab = f.split("_")
        if os.path.getsize('C:\\Users\\stage\\Desktop\\Stage_Marvyn\\logsCecyle\\logsUPSCUFR\\'+str(f)) > 20 and tab[2] != "input.log" and os.path.getsize('C:\\Users\\stage\\Desktop\\Stage_Marvyn\\logsCecyle\\logsUPSCUFR\\'+tab[0]+"_"+tab[1]+"_input.log")>20:
            #On regarde si c'est de champollion
            if(tab[0][0].lower() == "c"):
                univ = "CUFR"
                id_etudiant = i#On lui donne un ID
                i+=1
            else:
                univ = "UPS"
                id_etudiant = tab[0]
            #On créé le format de date
            date = datetime.datetime.fromtimestamp(int(tab[1])//1000)
            
            jour = date.strftime('%d')
            mois = date.strftime('%m')
            an = date.strftime('%Y')
            #On ouvre les fichiers JSON pour chopper les deates et les sequences
            with open(join("./logsUPSCUFR/",f)) as data_file:    
                data = json.load(data_file)

##            #On regarde si c'est un event ou un input
##            if tab[2] == "event.log":
##                x = "events"
##            else:
##                x = 'inputs'

            #On récupère la durée pour l'events
            heure1 = datetime.datetime.fromtimestamp(data['events'][0]['timestamp']//1000)
            heure2 = datetime.datetime.fromtimestamp(data['events'][len(data['events'])-1]['timestamp']//1000)
            dureeEvent=(heure2-heure1).seconds
            #On récupère la sequence
            sequence = data['events'][0]['sequence_id']
            #On récupère la date de début et la date de fin
            heureDebutEvent = int(datetime.datetime.fromtimestamp(data['events'][0]['timestamp']//1000).strftime('%H%M'))
            heureFinEvent = int(datetime.datetime.fromtimestamp(data['events'][len(data['events'])-1]['timestamp']//1000).strftime('%H%M'))
            
            with open(join("./logsUPSCUFR/",tab[0]+"_"+tab[1]+"_input.log")) as data_file:    
                data = json.load(data_file)

            #On récupère la durée pour l'input
            heure1 = datetime.datetime.fromtimestamp(data['inputs'][0]['timestamp']//1000)
            heure2 = datetime.datetime.fromtimestamp(data['inputs'][len(data['inputs'])-1]['timestamp']//1000)
            dureeInput=(heure2-heure1).seconds
            #On récupère la date de début et la date de fin
            heureDebutInput = int(datetime.datetime.fromtimestamp(data['inputs'][0]['timestamp']//1000).strftime('%H%M'))
            heureFinInput = int(datetime.datetime.fromtimestamp(data['inputs'][len(data['inputs'])-1]['timestamp']//1000).strftime('%H%M'))

            c.execute('INSERT OR IGNORE INTO ETUDIANT VALUES(?,?)',[id_etudiant,univ])
            conn.commit()
            c.execute('INSERT INTO LOGS VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',[f,id_etudiant,sequence,heureDebutEvent,heureFinEvent,dureeEvent,heureDebutInput,heureFinInput,dureeInput,jour,mois,an])
            conn.commit()          
            
            
            
