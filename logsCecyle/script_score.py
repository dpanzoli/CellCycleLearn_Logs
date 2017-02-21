import sqlite3
import json
unit_mark = 10000

def correctInput(u_input,meta):
    score = 0
    if u_input['user_input'] == meta['awnser']:
            score+= unit_mark
    return score

def correctDosage(u_input,meta):
    score = 0
    for i in range(len(u_input['user_input'])):
        if u_input[i]['user_input'] == meta['awnser'][i]:
            score+= unit_mark
    return score

def correctTextView(u_input,meta):
    score = 0
    for i in range(len(u_input['user_input'])):
        if u_input[i]['user_input'] == meta['awnser'][i]:
            score+= unit_mark
    return score

def correctCurve(u_input,meta):
    score = 0
    somme,dist = 0,0
    for i in range(len(u_input['user_input'])):
        somme += u_input[i]
        dist += abs(u_input['user_input'][i] - meta['awnser'][i])
    if (((somme - ecart)/somme)*100) >= meta['threshold']:
        score += unit_mark
    return score

def correctCount(u_input,meta):
    score = 0
    for i in range(len(u_input['user_input'])):
        if u_input['user_input'][i] in meta['awnser'][i]:
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Début du code
files = []
conn = sqlite3.connect(r'student.db')
c = conn.cursor()
for row in c.execute("SELECT nom_fichier FROM LOGS"):
    files.append(row[0])

#Pour tout nos fichiers
for f in ['21004056_1475771589449']:
    res = []
    #On ouvre un fichier JSON
    with open("./logsUPSCUFR/"+f+"_input.log")as data_file , open("sequence1.json") as seq1, open("sequence2.json") as seq2:
        inputdata = json.load(data_file)
        sequence1 = json.load(seq1)
        sequence2 = json.load(seq2)
    inp = inputdata['inputs'] 
    for i in range(len(inp)-1):
        if(inp[i]['section_id']) != 1:
            if inp[i]['sequence_id'] == 1:
                if inp[i]['activity_kind'] == "dragdrop":
                    res.append(correctDragDropView(inp[i],sequence1['sections'][inp[i]["section_id"]]['activites'][inp[i]["activity_id"]]['meta']))
                else:
                     pass
            else:
                if inp[i]['activity_kind'] == "dragdrop":
                    res.append([inp[i]["section_id"],inp[i]["activity_id"],correctDragDropView(inp[i],sequence2['sections'][inp[i]["section_id"]]['activites'][inp[i]["activity_id"]]['meta'])])
                
print(res)            
