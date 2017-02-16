import sqlite3
import json
import datetime

files = []
conn = sqlite3.connect(r'C:\\Users\\stage\\Desktop\\Stage_Marvyn\\CellCycleLearn_Logs\\logsCecyle\\student.db')
c = conn.cursor()

#On créé la table STATS
c.execute('''DROP TABLE IF EXISTS STATS''')
c.execute('''CREATE TABLE STATS
            (nom_fichier VARCHAR, id_activite,temps_activite INTEGER,nb_tentative INTEGER,
            FOREIGN KEY(nom_fichier)REFERENCES LOGS(nom_fichier),
            FOREIGN KEY(id_activite)REFERENCES ACTIVITE(id_activite),
            PRIMARY KEY(nom_fichier,id_activite))''')

#On récupère tout les nom de fichiers
for row in c.execute("SELECT nom_fichier FROM LOGS"):
    files.append(row[0])

d = {}
#Pour tout nos fichiers
for f in files:
    #On ouvre deux fichiers JSON, un input et un event
    with open('./logsUPSCUFR/'+f+"_event.log")as data_file, open("./logsUPSCUFR/"+f+"_input.log")as data_file2:
        eventdata = json.load(data_file)
        inputdata = json.load(data_file2)
    #On prend le premier timestamp
    timeStart = eventdata['events'][0]['timestamp']
    #Pour tout les events on regarde si à un moment on change d'activité, puis on récupère letemps passé
    for i in range(len(eventdata['events'])-1):
        if eventdata['events'][i+1]["activity_id"] != eventdata['events'][i]["activity_id"] or i == len(eventdata['events'])-2:
            x = (f,str(eventdata['events'][i]["sequence_id"]),str(eventdata['events'][i]["section_id"]),str(eventdata['events'][i]["activity_id"]))
            heure1 = datetime.datetime.fromtimestamp(timeStart//1000)
            timeStart = eventdata['events'][i]['timestamp']
            heure2  =datetime.datetime.fromtimestamp(eventdata['events'][i+1]['timestamp']//1000)  
            dureeInput=(heure2-heure1).seconds
            #Si on est jamais passé dans l'activité on créé une entrée
            if not x in d:
                d[x] = [0,0,[]]
            else:
                d[x][2].append([(str(eventdata['events'][i+1]["sequence_id"]),str(eventdata['events'][i+1]["section_id"]))])
            d[x][0]+=dureeInput

    #Cas rare : Quand le dernier event est différent de l'avant dernier, il faut l'ajouter
    if eventdata['events'][i+1]["activity_id"] != eventdata['events'][i]["activity_id"]:
        heure2  =datetime.datetime.fromtimestamp(eventdata['events'][i+1]['timestamp']//1000)
        dureeInput=(heure2-heure1).seconds
        x = (f,str(eventdata['events'][i+1]["sequence_id"]),str(eventdata['events'][i+1]["section_id"]),str(eventdata['events'][i+1]["activity_id"]))
        if not x in d:
            d[x] = [0,0,[]]
            d[x][0]+=dureeInput

    #On récupère le nombre de fois où l'élève à fait une épreuve
    for i in range(len(inputdata['inputs'])):
        d[(f,str(inputdata['inputs'][i]["sequence_id"]),str(inputdata['inputs'][i]["section_id"]),str(inputdata['inputs'][i]["activity_id"]))][1]+=1

#On parcours toute les clés du dictionnaire et on les ajoute dans la base         
for key in d:    
    for row in c.execute("SELECT * FROM ACTIVITE where id_section = ? and id_activite =? and id_sequence = ?",[key[2],key[3],key[1]]):
        x= row[0]
    c.execute("INSERT INTO STATS VALUES(?,?,?,?)",[key[0],x,d[key][0],d[key][1]])
conn.commit()
