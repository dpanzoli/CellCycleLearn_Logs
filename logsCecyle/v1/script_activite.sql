--.open C:\\Users\\stage\\Desktop\\Stage_Marvyn\\CellCycleLearn_Logs\\logsCecyle\\student.db

DROP TABLE IF EXISTS CCLSEQUENCE;
DROP TABLE IF EXISTS CCLSECTION;
DROP TABLE IF EXISTS ACTIVITE;

CREATE TABLE CCLSEQUENCE
	(id_sequence INTEGER PRIMARY KEY);

CREATE TABLE CCLSECTION
	(id_section VARCHAR PRIMARY KEY, lib_section VARCHAR);
	
CREATE TABLE ACTIVITE
	(id_activite INTEGER PRIMARY KEY autoincrement, num_activite VARCHAR, lib_activite VARCHAR,fk_id_sequence INTEGER, fk_id_section VARCHAR,type VARCHAR,chrono INTEGER,score_max INTEGER,
	FOREIGN KEY(fk_id_section) REFERENCES CCLSECTION(id_section), 
	FOREIGN KEY(fk_id_sequence) REFERENCES CCLSEQUENCE(id_sequence));
	
.read etudiant.sql	
INSERT INTO CCLSEQUENCE VALUES("1");
INSERT INTO CCLSEQUENCE VALUES("2");

--ALTER TABLE LOGS ADD FOREIGN KEY (sequence) REFERENCES CCLSEQUENCE(id_sequence);
.read logs.sql


INSERT INTO CCLSECTION  VALUES("0","Prérequis");
INSERT INTO CCLSECTION  VALUES("1","Hypothèses");
INSERT INTO CCLSECTION  VALUES("2","Protocole");
INSERT INTO CCLSECTION  VALUES("3","Expérience");
INSERT INTO CCLSECTION  VALUES("4","Résultats");
INSERT INTO CCLSECTION  VALUES("5","Synthèse");

INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("-1","TransitionRequirements",1,"0","Transition",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("0","Les phases du cycle cellulaire",1,"0","Drag and Drop",0,90000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("-1","TransitionHypothesis",1,"1","Transition",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("0","La durée des phases du cycle cellulaire",1,"1","Drag and Drop",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("1","Courbe de croissance dans des conditions optimales",1,"1","Courbe",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("-1","TransitionProtocol",1,"2","Transition",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("0","Planification du protocole expérimental",1,"2","Fiche Mémo",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("1","Nombres de boîtes de Pétri",1,"2","Fiche Mémo",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("2","Comptage",1,"2","Comptage",0,40000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("3","Densité Cellulaire",1,"2","Calcul",0,10000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("4","Nombre de cellules par boite et tailles des boites",1,"2","Fiche Mémo",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("5","Ensemencement",1,"2","Pipette",0,40000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("-1","TransitionExperimentation",1,"3","Transition",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("-1","TransitionResults",1,"4","Transition",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("0","Comptages",1,"4","Drag and Drop",0,60000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("1","Comptages et courbe de croissance dans des conditions optimales",1,"4","Courbe",1,60000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("2","Proportions des phases dans le cycle cellulaire",1,"4","Drag and Drop",0,30000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("3","Proportions et durée des phases dans le cycle cellulaire",1,"4","Drag and Drop",1,40000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("-1","TransitionSynthesis",1,"5","Transition",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("0","Synthèse",1,"5","Synthèse",0,100000);


INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("-1","TransitionRequirements",2,"0","Transition",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("0","Les checkpoints du cycle cellulaire",2,"0","Drag and Drop",0,80000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("1","Contenu ADN dans les différentes phases",2,"0","Drag and Drop",0,40000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("-1","TransitionHypothesis",2,"1","Transition",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("0","Checkpoint influencé par la privation en facteurs de croissance",2,"1","Drag and Drop",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("1","Evolution du nombre de cellules",2,"1","Courbe",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("-1","TransitionProtocol",2,"2","Transition",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("0","Planification du protocole expérimental",2,"2","Planification",0,50000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("1","Nombres de boîtes de Pétri",2,"2","Drag and Drop",0,10000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("2","Densité cellulaire",2,"2","Fiche Mémo",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("3","Nombre de cellules par boîte et taille des boîtes",2,"2","Fiche Mémo",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("4","Ensemencement",2,"2","Fiche Mémo",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("5","Changement de milieu",2,"2","Pipette",0,60000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("-1","TransitionExperimentation",2,"3","Transition",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("-1","TransitionResults",2,"4","Transition",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("0","Profils de cytométrie de flux au cours de l'expérience",2,"4","Drag and Drop",0,50000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("1","Checkpoint influencé par la privation en sérum",2,"4","Drag and Drop",1,40000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("2","Profils de cytométrie de flux et courbe d'évolution dans une phase",2,"4","Courbe",1,60000);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("-1","TransitionSynthesis",2,"5","Transition",0,0);
INSERT INTO ACTIVITE(num_activite,lib_activite,fk_id_sequence,fk_id_section,type,chrono,score_max) VALUES("0","Synthèse",2,"5","Syntèse",0,60000);
