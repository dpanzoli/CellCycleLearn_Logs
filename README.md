# CellCycleLearn_Logs
Analyse des logs produits par l'application Cell Cycle Learn

## Nettoyage des données (lundi 13/02, mardi 14/02)
Récupération des fichiers correspondant aux dates connues des TP à Toulouse eT Champollion (en septembre et octobre). 
2974 fichiers sont récupérés. 
Pour chaque session, il y a 2 fichiers (inputs et events) et 2 séquences soit a priori 4 fichiers/étudiant/session
On s'attend donc à trouver 2974/4 sessions.
Mais, en pratique, on est loin du compte :
- Il existe 6, 8 parfois plus logs pour un même étudiant, qui s'est déconnecté et/ou reconnecté
- Il existe de nombreux logs de moins de 20 octets, qui ne contiennent aucune donnée
- A Champollion, tout le monde a utilisé le même login (Cecyle) et donc impossible de recouper sessions 1 et 2 pour un même étudiant.

La première phase de nettoyage consiste à isoler les fichiers utiles dans `logsUPSCUFR`. 
- les fichiers de moins 20 octets ont été supprimés. 
- les fichiers qui ne correspondent pas à des étudiants

Afin de faciliter les recherches, une base de données est créée pour recenser les fichiers utilisable, ainsi que leurs propriétés.
`create_database.py`
Dans cette base de données :
- on créé la relation entre `LOG` et `ETUDIANT`.
- on enrichit les données : durée du log (temps effectif entre première et dernière actions utilisateur, etc.)
Chaque enregistrement de `LOG` recense 2 fichiers (le input et le event) 

Grace à ces infos, on 
