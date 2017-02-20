import sqlite3
import json
import datetime

files = []
conn = sqlite3.connect(r'student.db')
c = conn.cursor()

#On créé la table STATS
c.execute('''DROP TABLE IF EXISTS STATS''')
c.execute('''CREATE TABLE STATS
            (fk_nom_fichier VARCHAR, fk_id_activite INTEGER,tentative INTEGER,temps_tentative INTEGER,
            FOREIGN KEY(fk_nom_fichier)REFERENCES LOGS(nom_fichier),
            FOREIGN KEY(fk_id_activite)REFERENCES ACTIVITE(id_activite),
            PRIMARY KEY(fk_nom_fichier,fk_id_activite,tentative))''')

#On récupère tout les nom de fichiers
for row in c.execute("SELECT nom_fichier FROM LOGS"):
    files.append(row[0])


def tri_debut(listedeb,listefin,time):
    cpt = 0
    for i in listefin:

        if i < time:
            cpt+=1
    listedeb = listedeb[cpt:]
    listefin = listefin[cpt:]
    return(listedeb,listefin)

d = {}
#Pour tout nos fichiers
for f in files:
    #On ouvre deux fichiers JSON, un input et un event
    with open('./logsUPSCUFR/'+f+"_event.log")as data_file, open("./logsUPSCUFR/"+f+"_input.log")as data_file2:
        eventdata = json.load(data_file)
        inputdata = json.load(data_file2)
    #On prend le premier timestamp
    timeStart = eventdata['events'][0]['timestamp']
    currentActivity = "0"
    #Pour tout les events on regarde si à un moment on change d'activité, puis on récupère letemps passé
    for i in range(len(eventdata['events'])-1):

        if str(eventdata['events'][i+1]["section_id"]) != str(eventdata['events'][i]["section_id"]) or str(eventdata['events'][i+1]["sequence_id"]) != str(eventdata['events'][i]["sequence_id"]) or str(eventdata['events'][i+1]["activity_id"]) != str(eventdata['events'][i]["activity_id"]) or i == len(eventdata['events'])-2:
            x = (f,str(eventdata['events'][i]["sequence_id"]),str(eventdata['events'][i]["section_id"]),str(eventdata['events'][i]["activity_id"]))
            heure1 = datetime.datetime.fromtimestamp(timeStart//1000)
            heure2  =datetime.datetime.fromtimestamp(eventdata['events'][i]['timestamp']//1000)
            dureeInput=(heure2-heure1).seconds
            #Si on est jamais passé dans l'activité on créé une entrée
            if not x in d:
                d[x] = [0,[timeStart],[eventdata['events'][i]['timestamp']],[0,0,0,0,0],0]
                currentActivity = str(eventdata['events'][i]["sequence_id"])+str(eventdata['events'][i]["section_id"])+str(int(eventdata['events'][i]["activity_id"])+1)
            #Sinon c'est un retour et on ajoute dans t-1
            else:
                if currentActivity > str(eventdata['events'][i]["sequence_id"])+str(eventdata['events'][i]["section_id"])+str(int(eventdata['events'][i]["activity_id"])+1):
                    d[x][3][3]+=dureeInput
                d[x][1].append(timeStart)
                d[x][2].append(eventdata['events'][i+1]['timestamp'])

            #On ajoute quand même à la durée totale
            d[x][0]+=dureeInput
            timeStart = eventdata['events'][i]['timestamp']


    #Cas rare : Quand le dernier event est différent de l'avant dernier, il faut l'ajouter
    if eventdata['events'][i+1]["activity_id"] != eventdata['events'][i]["activity_id"]:
        heure2  =datetime.datetime.fromtimestamp(eventdata['events'][i+1]['timestamp']//1000)
        dureeInput=(heure2-heure1).seconds
        x = (f,str(eventdata['events'][i+1]["sequence_id"]),str(eventdata['events'][i+1]["section_id"]),str(eventdata['events'][i+1]["activity_id"]))
        if not x in d:
            d[x] = [0,[timeStart],[eventdata['events'][i+1]['timestamp']],[0,0,0,0,0],0]
            currentActivity = str(eventdata['events'][i]["sequence_id"])+str(eventdata['events'][i]["section_id"])+str(int(eventdata['events'][i]["activity_id"])+1)
        else:
            if currentActivity > str(eventdata['events'][i]["sequence_id"])+str(eventdata['events'][i]["section_id"])+str(int(eventdata['events'][i]["activity_id"])+1):
                    d[x][3][3]+=dureeInput
            d[x][1].append(timeStart)
            d[x][2].append(eventdata['events'][i+1]['timestamp'])
        d[x][0]+=dureeInput

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Input

        
    #On récupère le nombre de fois où l'élève à fait une épreuve
    j = 0
    for i in range(len(inputdata['inputs'])-1):
        seq,sec,act=str(inputdata['inputs'][i]["sequence_id"]),str(inputdata['inputs'][i]["section_id"]),str(inputdata['inputs'][i]["activity_id"])
        #On corrige l'erreur du script des logs ( il met -1 au lieu de 0 ) 
        if act == "-1":
            act = "0"
        #On cherche toutes les activités chronométré
        for row in c.execute("SELECT * FROM ACTIVITE where fk_id_section = ? and num_activite =? and fk_id_sequence = ?",[sec,act,seq]):
            x= row[0]
        #Si ce 'nest pas une activité chrono elle peut avoir donc plusieurs tentatives
        if x != 16 and x !=18 and x !=38 and x !=37:
            #Si il y a une autre tentative 
            if inputdata['inputs'][i]["sequence_id"] == inputdata['inputs'][i+1]["sequence_id"] and inputdata['inputs'][i]["activity_id"] == inputdata['inputs'][i+1]["activity_id"] and inputdata['inputs'][i]["section_id"] == inputdata['inputs'][i+1]["section_id"]:
                #On prend la fonction tri-debut qui permet de trier le temps de début utilisable et initilisable 
                x,y=tri_debut(d[f,seq,sec,act][1],d[f,seq,sec,act][2],inputdata['inputs'][i]['timestamp'])
                heure1 =datetime.datetime.fromtimestamp(x[0]//1000)
                heure2 = datetime.datetime.fromtimestamp(inputdata['inputs'][i]['timestamp']//1000)
                d[f,seq,sec,act][3][j] = (heure2-heure1).seconds
                #On augmente le nombre de tentative de 1
                j+=1
                #Si il ya eu plusieurs retour sur l'activité avant qu'elle soit faites et qu'on a donc plus de un temps de debut
                if len(y) > 1:
                    #Si notre temps de fin de l'event est plus grand que le timestamp de l'input 
                    if y[0]> inputdata['inputs'][i+1]['timestamp']:
                        #Notre nouveau temps de début ( entre la tentaive n et n+1 ) sera le temps précédent 
                        x[0] = inputdata['inputs'][i]['timestamp']
                        d[f,seq,sec,act][1][0] = inputdata['inputs'][i]['timestamp']
                    else:
                        #Sinon on laisse comme ça et notre fonction de tri s'en occupera 
                        d[f,seq,sec,act][1] = x
                else:
                    #Si c'est de taille un on remplace le temps de départ par le temps de notre nouveau début
                    x[0] = inputdata['inputs'][i]['timestamp']
                    d[f,seq,sec,act][1] = x
                #On enregistre nos temps de fin dans le dico pour le prochain tour
                d[f,seq,sec,act][2] = y
            else:
                x,y=tri_debut(d[f,seq,sec,act][1],d[f,seq,sec,act][2],inputdata['inputs'][i]['timestamp'])
                heure1 =datetime.datetime.fromtimestamp(x[0]//1000)
                heure2 = datetime.datetime.fromtimestamp(inputdata['inputs'][i]['timestamp']//1000)
                d[f,seq,sec,act][3][j] = (heure2-heure1).seconds
                #On augmente le nombre de tentative de 1
                j=0
                #Si il ya eu plusieurs retour sur l'activité avant qu'elle soit faites et qu'on a donc plus de un temps de debut
                if len(y) > 1:
                    #Si notre temps de fin de l'event est plus grand que le timestamp de l'input 
                    if y[0]> inputdata['inputs'][i+1]['timestamp']:
                        #Notre nouveau temps de début ( entre la tentaive n et n+1 ) sera le temps précédent 
                        x[0] = inputdata['inputs'][i]['timestamp']
                        d[f,seq,sec,act][1][0] = inputdata['inputs'][i]['timestamp']
                    else:
                        #Sinon on laisse comme ça et notre fonction de tri s'en occupera 
                        d[f,seq,sec,act][1] = x
                else:
                    #Si c'est de taille un on remplace le temps de départ par le temps de notre nouveau début
                    x[0] = inputdata['inputs'][i]['timestamp']
                    d[f,seq,sec,act][1] = x
                #On enregistre nos temps de fin dans le dico pour le prochain tour
        #Si c'est un temps chronometré
        else:
            if  inputdata['inputs'][i]["activity_id"] != inputdata['inputs'][i+1]["activity_id"]:
                heure1 =datetime.datetime.fromtimestamp(d[f,seq,sec,act][1][0]//1000)
                heure2 = datetime.datetime.fromtimestamp(inputdata['inputs'][i]['timestamp']//1000)
                if(heure1 > heure2):
                    heure1,heure2=heure2,heure1
                d[f,seq,sec,act][3][0] = (heure2-heure1).seconds
                d[f,seq,sec,act][4]=1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Insertion Base

#On parcours toute les clés du dictionnaire et on les ajoute dans la base
for key in d:
    #Si activité n'a pas d'input
    if d[key][3][0] + d[key][3][1] +d[key][3][2] ==0:
        #On met tout dans la tentative 1
        d[key][3][0] = d[key][0] - d[key][3][3]
    else:
        #Sinon on rajoute le temps entre la tentative 3 et le changement d'activite dans t[3]
        if d[key][3][4]<0:
            d[key][3][4] = d[key][0] - d[key][3][0] - d[key][3][1] - d[key][3][2] - d[key][3][3]
    for row in c.execute("SELECT * FROM ACTIVITE where fk_id_section = ? and num_activite =? and fk_id_sequence = ?",[key[2],key[3],key[1]]):
        x= row[0]
    for t in range(len(d[key][3])):
        if d[key][3][t] != 0:
            if t == 3:
                c.execute("INSERT INTO STATS VALUES(?,?,?,?)",[key[0],x,-1,d[key][3][t]])
            elif t == 4:
                c.execute("INSERT INTO STATS VALUES(?,?,?,?)",[key[0],x,0,d[key][3][t]])
            else:
                c.execute("INSERT INTO STATS VALUES(?,?,?,?)",[key[0],x,t+1,d[key][3][t]])
                
    
conn.commit()
