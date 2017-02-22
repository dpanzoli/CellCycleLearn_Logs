PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS LOGS;
CREATE TABLE LOGS
            (nom_fichier VARCHAR PRIMARY KEY,fk_id_etudiant VARCHAR, fk_sequence INTEGER,
            heure_debut_event INTEGER, heure_fin_event INTEGER, duree_event INTEGER,
            heure_debut_input INTEGER,heure_fin_input INTEGER, duree_input INTEGER,
            jour VARCHAR,mois VARCHAR,annee VARCHAR,
            FOREIGN KEY(fk_id_etudiant) REFERENCES ETUDIANT(id_etudiant)
			FOREIGN KEY(fk_sequence) REFERENCES CCLSEQUENCE(id_sequence));
INSERT INTO "LOGS" VALUES('0310021602961_1475598693254','0310021602961',2,1457,1527,1812,1458,1527,1767,'04','10','2016');
INSERT INTO "LOGS" VALUES('0310021607677_1475597246154','0310021607677',1,1433,1525,3077,1434,1524,3007,'04','10','2016');
INSERT INTO "LOGS" VALUES('1607006387Y_1474992028455','1607006387Y',1,1425,1538,4333,1428,1537,4112,'27','09','2016');
INSERT INTO "LOGS" VALUES('1607006387Y_1474996371697','1607006387Y',2,1538,1549,655,1540,1548,451,'27','09','2016');
INSERT INTO "LOGS" VALUES('21002027_1474992027813','21002027',1,1425,1510,2666,1427,1510,2550,'27','09','2016');
INSERT INTO "LOGS" VALUES('21002027_1474994699850','21002027',2,1510,1533,1410,1512,1533,1292,'27','09','2016');
INSERT INTO "LOGS" VALUES('21004056_1475768758627','21004056',1,1412,1459,2789,1413,1459,2710,'06','10','2016');
INSERT INTO "LOGS" VALUES('21004056_1475771589449','21004056',2,1459,1526,1643,1500,1526,1568,'06','10','2016');
INSERT INTO "LOGS" VALUES('21004482_1475682686313','21004482',1,1418,1427,579,1419,1427,472,'05','10','2016');
INSERT INTO "LOGS" VALUES('21004482_1475683322203','21004482',1,1428,1603,5719,1428,1603,5690,'05','10','2016');
INSERT INTO "LOGS" VALUES('2100547_1475235888124','2100547',1,1011,1110,3569,1012,1110,3497,'30','09','2016');
INSERT INTO "LOGS" VALUES('21100494_1475769036328','21100494',1,1416,1506,2967,1418,1506,2888,'06','10','2016');
INSERT INTO "LOGS" VALUES('21100494_1475775811934','21100494',2,1609,1619,562,1610,1618,517,'06','10','2016');
INSERT INTO "LOGS" VALUES('21100524_1475163783587','21100524',1,1409,1452,2594,1410,1452,2496,'29','09','2016');
INSERT INTO "LOGS" VALUES('21100524_1475166385607','21100524',2,1452,1520,1656,1455,1520,1477,'29','09','2016');
INSERT INTO "LOGS" VALUES('21100529_1474391401006','21100529',2,1535,1612,2243,1539,1612,1970,'20','09','2016');
INSERT INTO "LOGS" VALUES('21101724_1475077819753','21101724',1,1416,1518,3717,1419,1518,3567,'28','09','2016');
INSERT INTO "LOGS" VALUES('21104909_1474560172689','21104909',1,1428,1539,4305,1428,1539,4251,'22','09','2016');
INSERT INTO "LOGS" VALUES('21200184_1474560630310','21200184',1,1435,1507,1888,1436,1505,1736,'22','09','2016');
INSERT INTO "LOGS" VALUES('21200184_1474562522570','21200184',2,1507,1524,1044,1508,1524,949,'22','09','2016');
INSERT INTO "LOGS" VALUES('21200346_1475842495787','21200346',2,1041,1112,1899,1042,1111,1762,'07','10','2016');
INSERT INTO "LOGS" VALUES('21200370_1475840983310','21200370',1,1015,1058,2576,1017,1058,2452,'07','10','2016');
INSERT INTO "LOGS" VALUES('21200370_1475843592444','21200370',2,1059,1128,1741,1100,1127,1646,'07','10','2016');
INSERT INTO "LOGS" VALUES('21200371_1474472879537','21200371',1,1413,1518,3872,1415,1518,3778,'21','09','2016');
INSERT INTO "LOGS" VALUES('21200371_1474476789009','21200371',2,1518,1539,1251,1521,1539,1089,'21','09','2016');
INSERT INTO "LOGS" VALUES('21200643_1475854805157','21200643',1,1406,1539,5554,1409,1539,5401,'07','10','2016');
INSERT INTO "LOGS" VALUES('21200732_1475077918090','21200732',1,1418,1543,5133,1419,1543,5040,'28','09','2016');
INSERT INTO "LOGS" VALUES('21200745_1475077991552','21200745',1,1419,1538,4705,1421,1537,4594,'28','09','2016');
INSERT INTO "LOGS" VALUES('21200888_1475598520971','21200888',2,1454,1521,1573,1456,1521,1472,'04','10','2016');
INSERT INTO "LOGS" VALUES('21201091_1474995235511','21201091',2,1519,1540,1272,1520,1540,1178,'27','09','2016');
INSERT INTO "LOGS" VALUES('21201132_1475165855962','21201132',2,1443,1510,1579,1447,1509,1338,'29','09','2016');
INSERT INTO "LOGS" VALUES('21201483_1475253003728','21201483',1,1457,1539,2492,1458,1538,2453,'30','09','2016');
INSERT INTO "LOGS" VALUES('21201591_1474631820830','21201591',1,1022,1115,3206,1022,1115,3173,'23','09','2016');
INSERT INTO "LOGS" VALUES('21201591_1474635035711','21201591',2,1116,1152,2146,1117,1148,1886,'23','09','2016');
INSERT INTO "LOGS" VALUES('21201880_1475595089792','21201880',1,1400,1442,2521,1402,1442,2420,'04','10','2016');
INSERT INTO "LOGS" VALUES('21201880_1475597790817','21201880',2,1442,1502,1190,1443,1502,1112,'04','10','2016');
INSERT INTO "LOGS" VALUES('21201950_1475854803723','21201950',1,1406,1500,3246,1407,1459,3144,'07','10','2016');
INSERT INTO "LOGS" VALUES('21201950_1475858097497','21201950',2,1501,1530,1783,1503,1530,1640,'07','10','2016');
INSERT INTO "LOGS" VALUES('21201966_1475840989149','21201966',1,1015,1125,4150,1017,1124,4012,'07','10','2016');
INSERT INTO "LOGS" VALUES('21202160_1475235848816','21202160',1,1010,1053,2566,1013,1053,2382,'30','09','2016');
INSERT INTO "LOGS" VALUES('21202160_1475238435755','21202160',2,1053,1121,1683,1055,1121,1550,'30','09','2016');
INSERT INTO "LOGS" VALUES('21202575_1475768748655','21202575',1,1412,1453,2477,1413,1452,2341,'06','10','2016');
INSERT INTO "LOGS" VALUES('21202575_1475771241498','21202575',2,1453,1513,1217,1454,1513,1150,'06','10','2016');
INSERT INTO "LOGS" VALUES('21202577_1475771530122','21202577',2,1458,1521,1370,1501,1521,1199,'06','10','2016');
INSERT INTO "LOGS" VALUES('21203095_1474387661298','21203095',1,1433,1612,5931,1435,1611,5789,'20','09','2016');
INSERT INTO "LOGS" VALUES('21203120_1474649154371','21203120',2,1511,1512,81,1511,1512,28,'23','09','2016');
INSERT INTO "LOGS" VALUES('21204052_1475595264030','21204052',1,1400,1542,6072,1404,1542,5836,'04','10','2016');
INSERT INTO "LOGS" VALUES('21204364_1475235891980','21204364',1,1011,1121,4195,1012,1121,4092,'30','09','2016');
INSERT INTO "LOGS" VALUES('21204967_1475769245772','21204967',1,1420,1520,3638,1421,1520,3538,'06','10','2016');
INSERT INTO "LOGS" VALUES('21205899_1474646040333','21205899',1,1419,1519,3576,1420,1518,3492,'23','09','2016');
INSERT INTO "LOGS" VALUES('21206583_1474992025633','21206583',1,1426,1519,3164,1429,1518,2922,'27','09','2016');
INSERT INTO "LOGS" VALUES('21206583_1474995227474','21206583',2,1519,1540,1291,1520,1535,873,'27','09','2016');
INSERT INTO "LOGS" VALUES('21206646_1474646641298','21206646',1,1429,1506,2218,1429,1506,2194,'23','09','2016');
INSERT INTO "LOGS" VALUES('21206849_1474648920194','21206849',2,1507,1531,1444,1511,1530,1150,'23','09','2016');
INSERT INTO "LOGS" VALUES('21207261_1475236778437','21207261',1,1025,1107,2523,1025,1107,2514,'30','09','2016');
INSERT INTO "LOGS" VALUES('21207261_1475239309939','21207261',2,1108,1137,1790,1110,1137,1615,'30','09','2016');
INSERT INTO "LOGS" VALUES('21207389_1475595732564','21207389',1,1408,1411,175,1409,1409,10,'04','10','2016');
INSERT INTO "LOGS" VALUES('21207389_1475599980439','21207389',2,1519,1553,2045,1520,1552,1956,'04','10','2016');
INSERT INTO "LOGS" VALUES('21300046_1474473018228','21300046',1,1415,1510,3311,1417,1510,3211,'21','09','2016');
INSERT INTO "LOGS" VALUES('21300046_1474476343057','21300046',2,1511,1537,1601,1513,1537,1462,'21','09','2016');
INSERT INTO "LOGS" VALUES('21300180_1474390453951','21300180',2,1519,1551,1923,1521,1551,1759,'20','09','2016');
INSERT INTO "LOGS" VALUES('21300390_1474631394864','21300390',1,1015,1137,4890,1016,1135,4746,'23','09','2016');
INSERT INTO "LOGS" VALUES('21300482_1474561214917','21300482',1,1445,1549,3815,1446,1549,3787,'22','09','2016');
INSERT INTO "LOGS" VALUES('21300616_1474473014213','21300616',1,1415,1533,4642,1417,1530,4413,'21','09','2016');
INSERT INTO "LOGS" VALUES('21300710_1475250653859','21300710',1,1417,1522,3852,1419,1521,3727,'30','09','2016');
INSERT INTO "LOGS" VALUES('21300710_1475254562361','21300710',2,1522,1543,1285,1523,1543,1182,'30','09','2016');
INSERT INTO "LOGS" VALUES('21300973_1474472985976','21300973',1,1415,1512,3409,1417,1511,3261,'21','09','2016');
INSERT INTO "LOGS" VALUES('21300973_1474476414323','21300973',2,1512,1541,1742,1513,1541,1635,'21','09','2016');
INSERT INTO "LOGS" VALUES('21301119_1475166134298','21301119',2,1448,1512,1471,1449,1512,1430,'29','09','2016');
INSERT INTO "LOGS" VALUES('21301301_1474472973687','21301301',1,1415,1551,5786,1416,1549,5608,'21','09','2016');
INSERT INTO "LOGS" VALUES('21301337_1475236862587','21301337',1,1027,1113,2757,1027,1113,2728,'30','09','2016');
INSERT INTO "LOGS" VALUES('21301489_1474992038454','21301489',1,1426,1518,3116,1428,1518,3001,'27','09','2016');
INSERT INTO "LOGS" VALUES('21301489_1474995190915','21301489',2,1518,1547,1758,1519,1547,1703,'27','09','2016');
INSERT INTO "LOGS" VALUES('21301501_1474472981202','21301501',1,1415,1540,5118,1416,1540,5049,'21','09','2016');
INSERT INTO "LOGS" VALUES('21301519_1474631471673','21301519',1,1018,1122,3863,1020,1120,3594,'23','09','2016');
INSERT INTO "LOGS" VALUES('21301519_1474635434088','21301519',2,1122,1156,2041,1124,1156,1904,'23','09','2016');
INSERT INTO "LOGS" VALUES('21301744_1474472976622','21301744',1,1415,1550,5694,1416,1550,5623,'21','09','2016');
INSERT INTO "LOGS" VALUES('21301842_1475063206912','21301842',1,1013,1124,4309,1015,1124,4177,'28','09','2016');
INSERT INTO "LOGS" VALUES('21301843_1475077938187','21301843',1,1418,1547,5321,1420,1547,5202,'28','09','2016');
INSERT INTO "LOGS" VALUES('21301925_1474631383429','21301925',1,1016,1148,5507,1017,1147,5439,'23','09','2016');
INSERT INTO "LOGS" VALUES('21301941_1474645894522','21301941',1,1417,1503,2774,1420,1503,2536,'23','09','2016');
INSERT INTO "LOGS" VALUES('21301983_1475065719171','21301983',2,1054,1121,1613,1056,1121,1526,'28','09','2016');
INSERT INTO "LOGS" VALUES('21302466_1474631382182','21302466',1,1016,1101,2704,1017,1100,2610,'23','09','2016');
INSERT INTO "LOGS" VALUES('21302466_1474635091771','21302466',2,1116,1147,1865,1119,1147,1718,'23','09','2016');
INSERT INTO "LOGS" VALUES('21302676_1474559793802','21302676',1,1422,1459,2260,1422,1459,2206,'22','09','2016');
INSERT INTO "LOGS" VALUES('21302701_1474646039668','21302701',1,1421,1514,3176,1423,1514,3049,'23','09','2016');
INSERT INTO "LOGS" VALUES('21302782_1474646041522','21302782',1,1419,1538,4718,1420,1538,4625,'23','09','2016');
INSERT INTO "LOGS" VALUES('21302829_1474631384791','21302829',1,1015,1136,4895,1017,1136,4742,'23','09','2016');
INSERT INTO "LOGS" VALUES('21302882_1475599485738','21302882',2,1510,1538,1669,1512,1538,1565,'04','10','2016');
INSERT INTO "LOGS" VALUES('21303077_1475844039549','21303077',2,1106,1144,2245,1107,1144,2210,'07','10','2016');
INSERT INTO "LOGS" VALUES('21303188_1475858000091','21303188',2,1459,1527,1652,1504,1527,1339,'07','10','2016');
INSERT INTO "LOGS" VALUES('21303290_1475250662004','21303290',1,1417,1552,5682,1420,1552,5516,'30','09','2016');
INSERT INTO "LOGS" VALUES('21303290_1475685789523','21303290',2,1509,1553,2676,1515,1553,2312,'05','10','2016');
INSERT INTO "LOGS" VALUES('21303354_1475769012248','21303354',1,1416,1527,4266,1418,1527,4132,'06','10','2016');
INSERT INTO "LOGS" VALUES('21303368_1474646012628','21303368',1,1418,1519,3659,1420,1519,3551,'23','09','2016');
INSERT INTO "LOGS" VALUES('21303368_1474649696158','21303368',2,1520,1535,932,1520,1535,872,'23','09','2016');
INSERT INTO "LOGS" VALUES('21303380_1475236140600','21303380',1,1015,1121,3959,1015,1119,3833,'30','09','2016');
INSERT INTO "LOGS" VALUES('21303380_1475240104867','21303380',2,1121,1133,725,1121,1133,719,'30','09','2016');
INSERT INTO "LOGS" VALUES('21303384_1475770672518','21303384',2,1444,1502,1084,1446,1502,963,'06','10','2016');
INSERT INTO "LOGS" VALUES('21303413_1474631385316','21303413',1,1015,1126,4250,1017,1125,4088,'23','09','2016');
INSERT INTO "LOGS" VALUES('21303773_1475840982090','21303773',1,1015,1141,5150,1017,1141,5053,'07','10','2016');
INSERT INTO "LOGS" VALUES('21303792_1474648180478','21303792',2,1455,1515,1247,1455,1515,1191,'23','09','2016');
INSERT INTO "LOGS" VALUES('21303792_1474649692298','21303792',2,1520,1520,14,1520,1520,12,'23','09','2016');
INSERT INTO "LOGS" VALUES('21303873_1475769026068','21303873',1,1416,1506,2979,1418,1505,2859,'06','10','2016');
INSERT INTO "LOGS" VALUES('21303873_1475772027410','21303873',2,1507,1531,1451,1509,1531,1318,'06','10','2016');
INSERT INTO "LOGS" VALUES('21304077_1474648090787','21304077',2,1453,1528,2101,1500,1518,1056,'23','09','2016');
INSERT INTO "LOGS" VALUES('21304104_1474559780585','21304104',1,1421,1550,5311,1424,1550,5116,'22','09','2016');
INSERT INTO "LOGS" VALUES('21304170_1475841917284','21304170',1,1031,1129,3467,1031,1128,3414,'07','10','2016');
INSERT INTO "LOGS" VALUES('21304176_1474631415362','21304176',1,1015,1142,5208,1016,1142,5123,'23','09','2016');
INSERT INTO "LOGS" VALUES('21304371_1474560655239','21304371',1,1436,1538,3760,1436,1538,3727,'22','09','2016');
INSERT INTO "LOGS" VALUES('21304751_1474472721429','21304751',1,1411,1508,3432,1417,1507,3024,'21','09','2016');
INSERT INTO "LOGS" VALUES('21304751_1474476215741','21304751',2,1509,1531,1378,1510,1531,1305,'21','09','2016');
INSERT INTO "LOGS" VALUES('21304990_1474992040806','21304990',1,1425,1520,3244,1427,1519,3139,'27','09','2016');
INSERT INTO "LOGS" VALUES('21304990_1474995288835','21304990',2,1520,1546,1568,1520,1545,1504,'27','09','2016');
INSERT INTO "LOGS" VALUES('21305392_1474635668045','21305392',2,1126,1148,1330,1128,1148,1232,'23','09','2016');
INSERT INTO "LOGS" VALUES('21305528_1475595856951','21305528',1,1410,1411,69,1410,1410,0,'04','10','2016');
INSERT INTO "LOGS" VALUES('21305528_1475596002218','21305528',1,1412,1518,3917,1413,1518,3889,'04','10','2016');
INSERT INTO "LOGS" VALUES('21305536_1474387644416','21305536',1,1433,1612,5981,1434,1612,5898,'20','09','2016');
INSERT INTO "LOGS" VALUES('21306378_1475166141338','21306378',2,1448,1510,1323,1449,1510,1221,'29','09','2016');
INSERT INTO "LOGS" VALUES('21306704_1474634950916','21306704',2,1114,1200,2779,1118,1200,2506,'23','09','2016');
INSERT INTO "LOGS" VALUES('21306869_1475844185989','21306869',2,1109,1135,1601,1110,1135,1526,'07','10','2016');
INSERT INTO "LOGS" VALUES('21306952_1475843598188','21306952',1,1059,1132,1971,1059,1131,1912,'07','10','2016');
INSERT INTO "LOGS" VALUES('21306952_1475845674600','21306952',2,1134,1158,1444,1137,1158,1207,'07','10','2016');
INSERT INTO "LOGS" VALUES('21307124_1475250655413','21307124',1,1417,1542,5089,1418,1542,4991,'30','09','2016');
INSERT INTO "LOGS" VALUES('21400006_1474472992970','21400006',1,1415,1533,4693,1415,1533,4646,'21','09','2016');
INSERT INTO "LOGS" VALUES('21400259_1474992067518','21400259',1,1426,1521,3305,1428,1521,3172,'27','09','2016');
INSERT INTO "LOGS" VALUES('21400259_1474995426196','21400259',2,1522,1547,1521,1523,1547,1397,'27','09','2016');
INSERT INTO "LOGS" VALUES('21400278_1474992393889','21400278',1,1432,1524,3162,1437,1524,2830,'27','09','2016');
INSERT INTO "LOGS" VALUES('21400278_1474995574182','21400278',2,1524,1543,1112,1525,1543,1037,'27','09','2016');
INSERT INTO "LOGS" VALUES('21400523_1475255399106','21400523',2,1536,1550,838,1538,1550,694,'30','09','2016');
INSERT INTO "LOGS" VALUES('21400526_1475077823552','21400526',1,1416,1457,2471,1419,1454,2148,'28','09','2016');
INSERT INTO "LOGS" VALUES('21400526_1475080573859','21400526',2,1502,1518,962,1503,1518,883,'28','09','2016');
INSERT INTO "LOGS" VALUES('21400827_1474992042052','21400827',1,1426,1543,4664,1428,1543,4486,'27','09','2016');
INSERT INTO "LOGS" VALUES('21400827_1474996718243','21400827',2,1543,1550,385,1545,1550,312,'27','09','2016');
INSERT INTO "LOGS" VALUES('21400913_1474992058090','21400913',1,1426,1520,3263,1428,1519,3073,'27','09','2016');
INSERT INTO "LOGS" VALUES('21400913_1474995327856','21400913',2,1520,1542,1284,1522,1542,1159,'27','09','2016');
INSERT INTO "LOGS" VALUES('21401051_1474631412731','21401051',1,1015,1211,6966,1017,1211,6833,'23','09','2016');
INSERT INTO "LOGS" VALUES('21401502_1475685846629','21401502',2,1510,1550,2426,1511,1550,2376,'05','10','2016');
INSERT INTO "LOGS" VALUES('21401559_1474390456630','21401559',2,1519,1551,1912,1521,1551,1763,'20','09','2016');
INSERT INTO "LOGS" VALUES('21401581_1475250652892','21401581',1,1417,1510,3201,1418,1510,3093,'30','09','2016');
INSERT INTO "LOGS" VALUES('21401581_1475253876344','21401581',2,1511,1538,1633,1512,1538,1518,'30','09','2016');
INSERT INTO "LOGS" VALUES('21401606_1474636093114','21401606',2,1133,1145,725,1133,1145,707,'23','09','2016');
INSERT INTO "LOGS" VALUES('21401754_1474472732343','21401754',1,1411,1536,5131,1416,1536,4787,'21','09','2016');
INSERT INTO "LOGS" VALUES('21401809_1475166024680','21401809',2,1446,1513,1579,1448,1512,1458,'29','09','2016');
INSERT INTO "LOGS" VALUES('21401848_1474646249162','21401848',1,1422,1523,3651,1424,1523,3565,'23','09','2016');
INSERT INTO "LOGS" VALUES('21402273_1474473013339','21402273',1,1415,1546,5453,1417,1546,5351,'21','09','2016');
INSERT INTO "LOGS" VALUES('21402410_1474645949523','21402410',1,1417,1513,3358,1419,1513,3278,'23','09','2016');
INSERT INTO "LOGS" VALUES('21403027_1475841491727','21403027',1,1024,1112,2892,1027,1111,2650,'07','10','2016');
INSERT INTO "LOGS" VALUES('21403027_1475844391829','21403027',2,1112,1153,2427,1114,1152,2287,'07','10','2016');
INSERT INTO "LOGS" VALUES('21403686_1475065690642','21403686',2,1054,1127,1988,1055,1127,1917,'28','09','2016');
INSERT INTO "LOGS" VALUES('21403862_1474992037910','21403862',1,1426,1522,3350,1428,1521,3192,'27','09','2016');
INSERT INTO "LOGS" VALUES('21403862_1474995408462','21403862',2,1522,1544,1356,1523,1544,1280,'27','09','2016');
INSERT INTO "LOGS" VALUES('21403875_1474472987683','21403875',1,1415,1532,4640,1416,1532,4545,'21','09','2016');
INSERT INTO "LOGS" VALUES('21404025_1475063444103','21404025',1,1017,1114,3428,1018,1113,3293,'28','09','2016');
INSERT INTO "LOGS" VALUES('21404025_1475066886031','21404025',2,1114,1129,920,1115,1129,837,'28','09','2016');
INSERT INTO "LOGS" VALUES('21404252_1474390112412','21404252',1,1514,1522,533,1514,1522,476,'20','09','2016');
INSERT INTO "LOGS" VALUES('21404252_1474390655874','21404252',2,1523,1554,1849,1525,1554,1740,'20','09','2016');
INSERT INTO "LOGS" VALUES('21404331_1474560667588','21404331',1,1436,1552,4585,1436,1552,4560,'22','09','2016');
INSERT INTO "LOGS" VALUES('21404372_1474559778719','21404372',1,1421,1531,4159,1422,1529,3986,'22','09','2016');
INSERT INTO "LOGS" VALUES('21404680_1475599484631','21404680',2,1510,1538,1632,1512,1537,1533,'04','10','2016');
INSERT INTO "LOGS" VALUES('21404866_1474631430012','21404866',1,1016,1152,5761,1018,1152,5618,'23','09','2016');
INSERT INTO "LOGS" VALUES('21405330_1475686010264','21405330',2,1513,1605,3130,1516,1605,2912,'05','10','2016');
INSERT INTO "LOGS" VALUES('21405628_1475595905664','21405628',1,1411,1411,33,1411,1411,0,'04','10','2016');
INSERT INTO "LOGS" VALUES('21405628_1475596016585','21405628',1,1413,1521,4078,1413,1521,4047,'04','10','2016');
INSERT INTO "LOGS" VALUES('21405752_1475080869712','21405752',2,1507,1531,1471,1509,1531,1358,'28','09','2016');
INSERT INTO "LOGS" VALUES('21405867_1475235883977','21405867',1,1011,1101,3013,1013,1100,2832,'30','09','2016');
INSERT INTO "LOGS" VALUES('21405867_1475238906450','21405867',2,1101,1123,1326,1102,1123,1260,'30','09','2016');
INSERT INTO "LOGS" VALUES('21406113_1475167712885','21406113',2,1514,1543,1692,1516,1542,1568,'29','09','2016');
INSERT INTO "LOGS" VALUES('21406252_1474992026924','21406252',1,1426,1527,3654,1428,1526,3466,'27','09','2016');
INSERT INTO "LOGS" VALUES('21406252_1474995726693','21406252',2,1527,1549,1319,1528,1549,1262,'27','09','2016');
INSERT INTO "LOGS" VALUES('21406278_1475065130763','21406278',1,1045,1116,1907,1045,1116,1877,'28','09','2016');
INSERT INTO "LOGS" VALUES('21406534_1475235896547','21406534',1,1011,1121,4186,1013,1120,4040,'30','09','2016');
INSERT INTO "LOGS" VALUES('21406542_1475769588003','21406542',1,1425,1528,3728,1426,1527,3695,'06','10','2016');
INSERT INTO "LOGS" VALUES('21406577_1475077921430','21406577',1,1418,1509,3051,1418,1508,2959,'28','09','2016');
INSERT INTO "LOGS" VALUES('21406577_1475080985255','21406577',2,1509,1535,1542,1510,1534,1470,'28','09','2016');
INSERT INTO "LOGS" VALUES('21406780_1475250705283','21406780',1,1417,1546,5329,1419,1546,5207,'30','09','2016');
INSERT INTO "LOGS" VALUES('21406780_1475256040202','21406780',2,1546,1552,323,1548,1552,253,'30','09','2016');
INSERT INTO "LOGS" VALUES('21406966_1475840992588','21406966',1,1016,1136,4814,1020,1136,4534,'07','10','2016');
INSERT INTO "LOGS" VALUES('21407076_1475080867237','21407076',2,1507,1547,2397,1509,1547,2285,'28','09','2016');
INSERT INTO "LOGS" VALUES('21407141_1474648264853','21407141',2,1456,1527,1836,1457,1526,1750,'23','09','2016');
INSERT INTO "LOGS" VALUES('21407483_1475255340745','21407483',2,1535,1551,956,1537,1550,816,'30','09','2016');
INSERT INTO "LOGS" VALUES('21407776_1475238727257','21407776',2,1058,1058,28,1058,1058,0,'30','09','2016');
INSERT INTO "LOGS" VALUES('21407776_1475238768558','21407776',2,1059,1120,1307,1059,1120,1289,'30','09','2016');
INSERT INTO "LOGS" VALUES('21407874_1475066090805','21407874',2,1101,1126,1532,1104,1126,1352,'28','09','2016');
INSERT INTO "LOGS" VALUES('21408005_1475858134814','21408005',2,1501,1537,2137,1503,1537,2034,'07','10','2016');
INSERT INTO "LOGS" VALUES('21408342_1475254700175','21408342',2,1524,1547,1398,1525,1547,1317,'30','09','2016');
INSERT INTO "LOGS" VALUES('21410468_1475238111177','21410468',2,1048,1123,2097,1050,1121,1904,'30','09','2016');
INSERT INTO "LOGS" VALUES('21501074_1474995659727','21501074',2,1526,1543,1007,1527,1542,903,'27','09','2016');
INSERT INTO "LOGS" VALUES('21501169_1475237073938','21501169',1,1030,1208,5833,1031,1207,5756,'30','09','2016');
INSERT INTO "LOGS" VALUES('21504429_1474559787427','21504429',1,1421,1454,1964,1422,1454,1885,'22','09','2016');
INSERT INTO "LOGS" VALUES('21504429_1474562280975','21504429',2,1503,1522,1168,1503,1522,1142,'22','09','2016');
INSERT INTO "LOGS" VALUES('21506286_1475598826231','21506286',2,1500,1521,1298,1503,1520,1033,'04','10','2016');
INSERT INTO "LOGS" VALUES('21506317_1475772320739','21506317',2,1512,1530,1123,1515,1530,919,'06','10','2016');
INSERT INTO "LOGS" VALUES('21507351_1474391427726','21507351',2,1535,1611,2158,1540,1611,1907,'20','09','2016');
INSERT INTO "LOGS" VALUES('21507376_1475768876119','21507376',1,1414,1453,2348,1415,1453,2262,'06','10','2016');
INSERT INTO "LOGS" VALUES('21507376_1475771236200','21507376',2,1453,1518,1504,1454,1518,1423,'06','10','2016');
INSERT INTO "LOGS" VALUES('21507392_1475770960300','21507392',2,1448,1506,1078,1449,1506,1012,'06','10','2016');
INSERT INTO "LOGS" VALUES('21507799_1474387538488','21507799',1,1431,1520,2893,1433,1519,2750,'20','09','2016');
INSERT INTO "LOGS" VALUES('21507799_1474390569187','21507799',2,1521,1602,2427,1524,1602,2284,'20','09','2016');
INSERT INTO "LOGS" VALUES('21508200_1475840986489','21508200',1,1016,1113,3460,1018,1110,3114,'07','10','2016');
INSERT INTO "LOGS" VALUES('21508200_1475844546333','21508200',2,1115,1130,921,1117,1130,790,'07','10','2016');
INSERT INTO "LOGS" VALUES('21508496_1475854859886','21508496',1,1407,1455,2866,1408,1454,2770,'07','10','2016');
INSERT INTO "LOGS" VALUES('21508496_1475857736799','21508496',2,1455,1521,1590,1457,1520,1422,'07','10','2016');
INSERT INTO "LOGS" VALUES('21508551_1475843769877','21508551',2,1102,1137,2130,1104,1137,1963,'07','10','2016');
INSERT INTO "LOGS" VALUES('21600537_1474559788895','21600537',1,1421,1522,3659,1423,1522,3574,'22','09','2016');
INSERT INTO "LOGS" VALUES('21601386_1475063347415','21601386',1,1015,1124,4163,1016,1124,4109,'28','09','2016');
INSERT INTO "LOGS" VALUES('21601397_1475063902633','21601397',1,1024,1116,3131,1025,1114,2967,'28','09','2016');
INSERT INTO "LOGS" VALUES('21602560_1475077853099','21602560',1,1417,1532,4476,1421,1531,4219,'28','09','2016');
INSERT INTO "LOGS" VALUES('21603542_1475769244185','21603542',1,1420,1513,3214,1421,1513,3156,'06','10','2016');
INSERT INTO "LOGS" VALUES('21603806_1474631378457','21603806',1,1015,1037,1305,1016,1036,1191,'23','09','2016');
INSERT INTO "LOGS" VALUES('21603806_1474632884630','21603806',1,1040,1137,3418,1040,1136,3383,'23','09','2016');
INSERT INTO "LOGS" VALUES('21604380_1475235890387','21604380',1,1011,1053,2526,1012,1053,2443,'30','09','2016');
INSERT INTO "LOGS" VALUES('21604380_1475238429190','21604380',2,1053,1121,1657,1054,1120,1609,'30','09','2016');
INSERT INTO "LOGS" VALUES('21604809_1474560902531','21604809',1,1440,1544,3860,1440,1544,3832,'22','09','2016');
INSERT INTO "LOGS" VALUES('21604925_1474634708686','21604925',2,1110,1114,215,1110,1114,189,'23','09','2016');
INSERT INTO "LOGS" VALUES('21604925_1474634938187','21604925',2,1114,1135,1254,1114,1135,1226,'23','09','2016');
INSERT INTO "LOGS" VALUES('21604949_1474634117754','21604949',2,1100,1137,2192,1103,1137,2027,'23','09','2016');
INSERT INTO "LOGS" VALUES('21607006_1474387403686','21607006',1,1429,1524,3267,1430,1523,3181,'20','09','2016');
INSERT INTO "LOGS" VALUES('21607006_1474390761534','21607006',2,1524,1547,1385,1526,1547,1280,'20','09','2016');
INSERT INTO "LOGS" VALUES('21607125_1474560400535','21607125',1,1432,1434,143,1432,1434,108,'22','09','2016');
INSERT INTO "LOGS" VALUES('21607125_1474560623580','21607125',1,1435,1539,3851,1436,1539,3808,'22','09','2016');
INSERT INTO "LOGS" VALUES('21607305_1474563518566','21607305',2,1524,1554,1827,1525,1554,1707,'22','09','2016');
INSERT INTO "LOGS" VALUES('21608222_1475163648593','21608222',1,1407,1418,701,1408,1416,448,'29','09','2016');
INSERT INTO "LOGS" VALUES('21608222_1475166026641','21608222',2,1446,1512,1541,1447,1512,1473,'29','09','2016');
INSERT INTO "LOGS" VALUES('21608718_1474994582374','21608718',2,1508,1532,1434,1512,1531,1183,'27','09','2016');
INSERT INTO "LOGS" VALUES('21609209_1475685734053','21609209',2,1508,1548,2434,1509,1546,2195,'05','10','2016');
INSERT INTO "LOGS" VALUES('21610421_1474562378490','21610421',2,1505,1546,2498,1506,1546,2437,'22','09','2016');
INSERT INTO "LOGS" VALUES('cecycle _1480337235227','0',1,1012,1048,2138,1016,1047,1912,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecycle _1480339385707','1',2,1048,1137,2950,1052,1137,2699,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecycle_1480956908901','2',2,1420,1459,2341,1422,1459,2203,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecycle_1481140452168','3',2,1719,1720,53,1719,1720,29,'07','12','2016');
INSERT INTO "LOGS" VALUES('cecycle_1481140513194','4',2,1720,1722,86,1720,1721,14,'07','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480331505425','5',1,837,856,1142,837,855,1099,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480332650792','6',2,856,905,546,856,905,544,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480335796003','7',1,948,949,24,948,949,18,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480337144282','8',1,1011,1052,2454,1012,1051,2374,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480337195148','9',1,1012,1117,3879,1016,1116,3617,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480337197746','10',1,1012,1103,3076,1014,1101,2797,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480337210579','11',1,1012,1112,3568,1014,1111,3421,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480337211535','12',1,1012,1111,3514,1014,1110,3389,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480337220046','13',1,1013,1112,3551,1016,1112,3335,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480337221207','14',1,1013,1107,3201,1016,1106,2988,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480337233465','15',1,1012,1115,3744,1017,1114,3453,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480337234081','16',1,1012,1049,2186,1014,1047,2019,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480337238639','17',1,1012,1112,3574,1016,1112,3354,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480337242794','18',1,1013,1106,3206,1014,1106,3131,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480337243477','19',1,1013,1107,3206,1017,1106,2939,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480337246182','20',1,1013,1115,3721,1018,1112,3259,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480337256704','21',1,1013,1107,3223,1016,1106,3014,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480337341910','22',1,1014,1059,2672,1017,1058,2471,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480337693514','23',1,1020,1104,2653,1023,1104,2439,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480339430492','24',2,1049,1135,2743,1050,1134,2621,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480339604501','25',2,1052,1121,1751,1058,1121,1384,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480340024354','26',2,1059,1136,2222,1101,1136,2100,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480340284445','27',2,1103,1134,1878,1104,1134,1805,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480340352520','28',2,1104,1148,2649,1110,1148,2313,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480340510741','29',2,1107,1126,1156,1114,1126,725,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480340526692','30',2,1107,1148,2468,1114,1148,2059,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480340527105','31',2,1107,1146,2324,1115,1146,1845,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480340644335','32',2,1109,1146,2231,1115,1146,1831,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480340743535','33',2,1111,1146,2093,1114,1145,1860,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480340815995','34',2,1112,1151,2328,1116,1151,2104,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480340822358','35',2,1112,1149,2216,1114,1149,2075,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480340828464','36',2,1112,1147,2123,1113,1147,2037,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480340993573','37',2,1115,1153,2264,1118,1153,2082,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480341014098','38',2,1115,1146,1864,1116,1146,1820,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480341107389','39',2,1117,1156,2350,1118,1156,2249,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480341684682','40',2,1126,1149,1358,1126,1148,1317,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480349615260','41',1,1340,1456,4590,1346,1456,4210,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480349615374','42',1,1339,1436,3442,1343,1436,3144,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480349619996','43',1,1340,1452,4352,1348,1451,3785,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480349626146','44',1,1342,1533,6615,1346,1533,6380,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480349626509','45',1,1339,1432,3153,1343,1432,2926,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480349627977','46',1,1339,1432,3177,1341,1431,2987,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480349630121','47',1,1339,1433,3229,1342,1432,3043,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480349631591','48',1,1339,1431,3124,1342,1431,2956,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480349634000','49',1,1339,1527,6485,1344,1527,6165,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480349646861','50',1,1339,1500,4827,1344,1459,4502,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480349656199','51',1,1341,1534,6771,1344,1534,6621,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480349666036','52',1,1341,1454,4351,1343,1453,4217,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480349693250','53',1,1342,1350,482,1345,1348,219,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480349705096','54',1,1340,1537,7030,1343,1536,6768,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480349713702','55',1,1342,1501,4758,1346,1500,4429,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480350316331','56',1,1350,1457,3976,1351,1455,3865,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480352780093','57',2,1432,1522,3031,1437,1522,2712,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480352813070','58',2,1432,1519,2812,1435,1519,2636,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480352814573','59',2,1432,1521,2954,1445,1521,2147,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480352873065','60',2,1433,1522,2958,1442,1522,2385,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480353088236','61',2,1437,1521,2684,1441,1521,2417,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480353098640','62',2,1437,1528,3058,1440,1528,2882,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480354042315','63',2,1452,1529,2208,1454,1529,2107,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480354142828','64',2,1454,1534,2401,1459,1534,2099,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480354213861','65',2,1455,1524,1731,1458,1524,1587,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480354283372','66',2,1457,1527,1815,1459,1527,1692,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480354355500','67',2,1458,1530,1926,1500,1530,1781,'28','11','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480354485975','68',2,1500,1537,2233,1504,1537,1950,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480354555293','69',2,1501,1530,1757,1503,1529,1545,'28','11','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480884311675','70',1,1812,1827,873,1815,1827,675,'04','12','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480885196682','71',2,1827,1840,790,1828,1840,749,'04','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480954372118','72',1,1338,1501,4993,1340,1500,4839,'05','12','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480954382365','73',1,1339,1433,3244,1342,1431,2958,'05','12','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480954420719','74',1,1339,1426,2866,1340,1426,2771,'05','12','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480954429070','75',1,1339,1426,2789,1343,1425,2537,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480954432722','76',1,1339,1438,3560,1342,1438,3347,'05','12','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480954447685','77',1,1340,1429,2949,1341,1428,2820,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480954459529','78',1,1340,1503,4985,1342,1502,4823,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480954490945','79',1,1340,1344,265,1342,1343,93,'05','12','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480954491353','80',1,1340,1428,2848,1343,1428,2683,'05','12','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480954538178','81',1,1341,1422,2461,1343,1420,2189,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480954697001','82',1,1343,1441,3476,1344,1440,3358,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480954802093','83',1,1345,1350,292,1345,1349,223,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480954985557','84',1,1348,1359,617,1350,1355,301,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480955107668','85',1,1350,1424,2012,1350,1423,1962,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480955544727','86',1,1357,1425,1686,1358,1425,1616,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480955645816','87',1,1359,1445,2748,1359,1445,2703,'05','12','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480957017704','88',2,1422,1454,1925,1424,1453,1751,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480957123076','89',2,1424,1455,1879,1425,1455,1781,'05','12','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480957247178','90',2,1426,1455,1746,1429,1455,1567,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480957264479','91',1,1426,1430,262,1428,1430,145,'05','12','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480957333845','92',2,1427,1503,2138,1433,1502,1756,'05','12','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480957386343','93',2,1428,1456,1671,1430,1456,1572,'05','12','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480957440507','94',2,1429,1501,1933,1431,1501,1814,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480957531554','95',2,1430,1503,1930,1432,1502,1840,'05','12','2016');
INSERT INTO "LOGS" VALUES('Cecyle_1480957665997','96',2,1433,1508,2114,1435,1508,1959,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480958002030','97',2,1438,1508,1803,1439,1508,1749,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480958187824','98',2,1442,1510,1683,1443,1509,1607,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1480958403365','99',2,1445,1510,1482,1446,1510,1403,'05','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1481068583389','100',1,2122,2158,2190,2122,2158,2134,'07','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1481130906059','101',2,1340,1352,748,1340,1352,733,'07','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1481136678506','102',1,1616,1630,822,1618,1630,689,'07','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1481136748049','103',1,1618,1626,526,1618,1626,458,'07','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1481137510769','104',2,1630,1654,1437,1631,1651,1221,'07','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1481137547183','105',1,1631,1633,145,1632,1633,51,'07','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1481137707171','106',1,1633,1651,1039,1634,1650,977,'07','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1481138750509','107',2,1651,1807,4601,1651,1807,4556,'07','12','2016');
INSERT INTO "LOGS" VALUES('cecyle_1481223942984','108',1,1631,1633,151,1631,1632,109,'08','12','2016');
COMMIT;
