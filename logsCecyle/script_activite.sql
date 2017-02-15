--.open C:\\Users\\stage\\Desktop\\Stage_Marvyn\\CellCycleLearn_Logs\\logsCecyle\\student.db

DROP TABLE IF EXISTS CCLSEQUENCE;
DROP TABLE IF EXISTS CCLSECTION;
DROP TABLE IF EXISTS ACTIVITE;

CREATE TABLE CCLSEQUENCE
	(id_sequence INTEGER PRIMARY KEY);

CREATE TABLE CCLSECTION
	(id_section VARCHAR PRIMARY KEY, lib_section VARCHAR);
	
CREATE TABLE ACTIVITE
	(key_activite INTEGER PRIMARY KEY autoincrement, id_activite VARCHAR, lib_activite VARCHAR,id_sequence INTEGER, id_section VARCHAR,
	FOREIGN KEY(id_section) REFERENCES CCLSECTION(id_section), 
	FOREIGN KEY(id_sequence) REFERENCES CCLSEQUENCE(id_sequence));
	
	
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

INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("-1","TransitionRequirements",1,"0");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("0","Les phases du cycle cellulaire",1,"0");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("-1","TransitionHypothesis",1,"1");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("0","La durée des phases du cycle cellulaire",1,"1");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("1","Courbe de croissance dans des conditions optimales",1,"1");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("-1","TransitionProtocol",1,"2");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("0","Planification du protocole expérimental",1,"2");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("2","Nombres de boîtes de Pétri",1,"2");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("3","Comptage",1,"2");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("4","Densité Cellulaire",1,"2");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("5","Nombre de cellules par boite et tailles des boites",1,"2");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("6","Ensemencement",1,"2");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("-1","TransitionExperimentation",1,"3");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("-1","TransitionResults",1,"4");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("0","Comptages",1,"4");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("1","Comptages et courbe de croissance dans des conditions optimales",1,"4");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("2","Proportions des phases dans le cycle cellulaire",1,"4");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("3","Proportions et durée des phases dans le cycle cellulaire",1,"4");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("-1","TransitionSynthesis",1,"5");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("0","Synthèse",1,"5");


INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("-1","TransitionRequirements",2,"0");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("0","Les checkpoints du cycle cellulaire",2,"0");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("2","Contenu ADN dans les différentes phases",2,"0");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("-1","TransitionHypothesis",2,"1");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("0","Checkpoint influencé par la privation en facteurs de croissance",2,"1");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("1","Evolution du nombre de cellules",2,"1");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("-1","TransitionProtocol",2,"2");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("0","Planification du protocole expérimental",2,"2");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("2","Nombres de boîtes de Pétri",2,"2");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("3","Densité cellulaire",2,"2");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("4","Nombre de cellules par boîte et taille des boîtes",2,"2");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("5","Ensemencement",2,"2");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("6","Changement de milieu",2,"2");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("-1","TransitionExperimentation",2,"3");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("-1","TransitionResults",2,"4");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("0","Profils de cytométrie de flux au cours de l'expérience",2,"4");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("1","Checkpoint influencé par la privation en sérum",2,"4");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("2","Profils de cytométrie de flux et courbe d'évolution dans une phase","2","4");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("-1","TransitionSynthesis",2,"5");
INSERT INTO ACTIVITE(id_activite,lib_activite,id_sequence,id_section) VALUES("0","Synthèse",2,"5");
