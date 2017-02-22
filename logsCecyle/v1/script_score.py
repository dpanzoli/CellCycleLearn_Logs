import sqlite3
import json
unit_mark = 10000

def correctInput(u_input,meta):
    score = 0
    if u_input['data']['user_input'] == meta['answer']:
            score+= unit_mark
    return score

def correctDosageAndTextView(u_input,meta):
    score = 0
    for i in range(len(u_input['data']['user_input'])):
        if u_input['data']['user_input'][i] == meta['answer'][i]:
            score+= unit_mark
    return score

##def correctTextView(u_input,meta):
##    score = 0
##    for i in range(len(u_input['user_input'])):
##        if u_input[i]['user_input'] == meta['awnser'][i]:
##            score+= unit_mark
##    return score

def correctCurve(u_input,meta):
    score = 0
    somme,dist = 0,0
    for i in range(len(u_input['data']['user_input'])):
        somme += u_input['data']['user_input'][i]
        dist += abs(u_input['data']['user_input'][i] - meta['answer'][i])
        if (((somme - dist)/(somme+1))*100) >= meta['threshold']:
            score += unit_mark
    return score

def correctCount(u_input,meta):
    score = 0
    for i in range(len(u_input['data']['user_input'])):
        if u_input['data']['user_input'][i] in meta['answer'][i]:
            score+= unit_mark
    return score

def correctDragDropView(u_input,meta):
    score = 0
    if  'answer' in meta:
        for i in range(len(u_input['data']['user_input'])):
            if len(u_input['data']['user_input'][i]['stickers']) == len(meta['answer'][i]["stickers"]):
                if len(u_input['data']['user_input'][i]['stickers']) == 0:
                       score+=unit_mark
                for j in range(len(u_input['data']['user_input'][i]['stickers'])):
                    if str(u_input['data']['user_input'][i]['stickers'][j]) ==str(meta['answer'][i]["stickers"][j]):
                        score += unit_mark
    elif 'answer_mult' in meta:
        for i in range(len(meta['awnser_multi'])):
            temp = 0
            for j in range(len(u_input['data']['user_input'])):
                if len(u_input['data']['user_input'][j]['stickers']) ==len(meta['answer_multi'][i][j]["stickers"]):
                    for k in range(len(u_input['data']['user_input'][j]['stickers'])):
                        if str(u_input['data']['user_input'][i]['stickers'][k]) ==str(meta['answer'][i][j]["stickers"][k]):
                               score += unit_mark
            if temp > score:
                score = temp
    return score

def correctPlanif(u_input,meta):
    score = 0
    for i in range(len(u_input['data']['user_input']['protocol'])):
        if u_input['data']['user_input']['protocol'][i] == meta['answer']['protocol'][i]:
            score+=unit_mark
    if len(u_input['data']['user_input']['culture']) == len(meta['answer']['culture']):
        for i in range(len(meta['answer']['culture'])):
            if u_input['data']['user_input']['culture'][i]['condition'] == meta['answer']['culture'][i]['condition'] and u_input['data']['user_input']['culture'][i]['time'] == meta['answer']['culture'][i]['time']:
                score+=unit_mark
    if u_input['data']['user_input']['temoincheck']:
        if len(u_input['data']['user_input']['temoin']) == len(meta['answer']['temoin']):
            for i in range(len(meta['answer']['temoin'])):
                if u_input['data']['user_input']['temoin'][i]['condition'] == meta['answer']['temoin'][i]['condition'] and u_input['data']['user_input']['temoin'][i]['time'] == meta['answer']['temoin'][i]['time']:
                    score+=unit_mark
    return score
            

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Début du code
files = []
conn = sqlite3.connect(r'student.db')
c = conn.cursor()
#c.execute("ALTER TABLE STATS ADD COLUMN score INTEGER ")
for row in c.execute("SELECT nom_fichier FROM LOGS"):
    files.append(row[0])
d = {}
#Pour tout nos fichiers
for f in files:
    #On ouvre un fichier JSON
    with open("./logsUPSCUFR/"+f+"_input.log")as data_file , open("sequence1.json") as seq1, open("sequence2.json") as seq2:
        inputdata = json.load(data_file)
        sequence1 = json.load(seq1)
        sequence2 = json.load(seq2)
    inp = inputdata['inputs']
    for i in range(len(inp)):
        seq,sec,act = inp[i]["sequence_id"],inp[i]["section_id"],inp[i]["activity_id"]
        x = (f,seq,sec,act)
        if sec != 1:           
            if not x in d:
                        d[x] = []                        
            if seq == 1:
                s = sequence1
            else:
                s = sequence2
            if inp[i]['activity_kind'] == "dragdrop":
                d[x].append(correctDragDropView(inp[i],s['sections'][sec]['activites'][act]['meta']))
            elif inp[i]['activity_kind'] == "curvetest" or inp[i]['activity_kind'] == "curvestar":
                d[x].append(correctCurve(inp[i],s['sections'][sec]['activites'][act]['meta']))
            elif inp[i]['activity_kind'] == "counttest":
                d[x].append(correctCount(inp[i],s['sections'][sec]['activites'][act]['meta']))
            elif inp[i]['activity_kind'] == "input":
                d[x].append(correctInput(inp[i],s['sections'][sec]['activites'][act]['meta']))
            elif inp[i]['activity_kind'] == "pipette" or inp[i]['activity_kind'] == "synthesis" or inp[i]['activity_kind'] == "doublepipette" :
                d[x].append(correctDosageAndTextView(inp[i],s['sections'][sec]['activites'][act]['meta']))
            elif inp[i]['activity_kind'] == "planif":
                if act == -1:
                    act+=1
                d[x].append(correctPlanif(inp[i],s['sections'][sec]['activites'][act]['meta']))
for x in d:
    for row in c.execute("SELECT * FROM ACTIVITE where fk_id_section = ? and num_activite =? and fk_id_sequence = ?",[x[2],x[3],x[1]]):
        ida= row[0]
    if len(d[x]) > 3:
        c.execute("UPDATE STATS SET score = ? where fk_nom_fichier = ? and fk_id_activite = ? and tentative = 1",[d[x][len(d[x])-1],x[0],ida])
    else:
        for i in range(len(d[x])):
            c.execute("UPDATE STATS SET score = ? where fk_nom_fichier = ? and fk_id_activite = ? and tentative = ?",[d[x][i],x[0],ida,i+1])
conn.commit()
