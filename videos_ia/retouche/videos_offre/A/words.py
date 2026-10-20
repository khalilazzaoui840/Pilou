# Vidéo A (PILOU_video_modifiee) — voix audio_pilou_video_modifiee.mp3 (24,69 s)
MP3=__import__('os').environ.get('PILOU_WORK','travail')+'/021ff0e1-audio_pilou_video_modifiee.mp3'   # audio d'origine, copié tel quel
VO=__import__('os').environ.get('PILOU_WORK','travail')+'/v3/vo_A.wav'
PHRASES=[
 (0.04,1.60,[("TON",0.04),("CHIEN",0.28),("PERD",0.52),("SES",0.67),("POILS",0.85),("PARTOUT ?",1.06)]),
 (1.82,4.05,[("ET",1.82),("EN",1.95),("PLUS",2.05),("IL",2.45),("DÉTESTE",2.71),("LE",3.33),("BROSSAGE",3.43)]),
 (4.29,4.88,[("NORMAL",4.29)]),
 (5.20,7.31,[("LES",5.20),("BROSSES",5.32),("SANS",5.62),("EMBOUTS",5.86),("TIRENT",6.28),("ET",6.70),("GRIFFENT",6.82)]),
 (7.76,9.26,[("LA",7.76),("BROSSE",7.85),("PILOU",8.12),("C'EST",8.58),("DIFFÉRENT",8.71)]),
 (9.65,13.68,[("DES",9.65),("EMBOUTS",9.74),("SOUPLES",10.12),("QUI",10.51),("RETIRENT",10.63),("TOUT",11.08),("LE",11.23),("SOUS-POIL",11.38),("MORT",11.78),
              ("EN",12.09),("DOUCEUR",12.22),("SANS",12.84),("LUI",13.03),("FAIRE",13.21),("MAL",13.39)]),
 (14.06,14.64,[("LE",14.06),("RÉSULTAT ?",14.13)]),
 (15.03,16.86,[("DES",15.03),("POIGNÉES",15.22),("DE",15.52),("POILS",15.61),("À",15.95),("CHAQUE",16.15),("PASSAGE",16.37)]),
 (17.18,19.81,[("ET",17.18),("UN",17.29),("CHIEN",17.46),("ENFIN",17.84),("DÉTENDU",18.25),("QUI",18.90),("ADORE",19.16),("ÇA",19.63)]),
 (20.19,23.17,[("PROFITE",20.19),("DE",20.59),("L'OFFRE",20.70),("UNE",21.28),("BROSSE",21.43),("PILOU",21.67),("ACHETÉE",21.90),("UNE",22.50),("OFFERTE !",22.62)]),
 (23.33,24.57,[("FONCE !",23.33),("LIEN",23.97),("EN",24.15),("BIO !",24.28)]),
]
GROUPS=[[["TON","CHIEN"],["PERD","SES","POILS"],["PARTOUT ?"]],
 [["ET","EN","PLUS"],["IL","DÉTESTE"],["LE","BROSSAGE"]],
 [["NORMAL"]],
 [["LES","BROSSES"],["SANS","EMBOUTS"],["TIRENT","ET","GRIFFENT"]],
 [["LA","BROSSE","PILOU"],["C'EST","DIFFÉRENT"]],
 [["DES","EMBOUTS"],["SOUPLES"],["QUI","RETIRENT"],["TOUT","LE"],["SOUS-POIL","MORT"],["EN","DOUCEUR"],["SANS","LUI"],["FAIRE","MAL"]],
 [["LE","RÉSULTAT ?"]],
 [["DES","POIGNÉES"],["DE","POILS"],["À","CHAQUE"],["PASSAGE"]],
 [["ET","UN","CHIEN"],["ENFIN","DÉTENDU"],["QUI","ADORE","ÇA"]],
 [["PROFITE","DE","L'OFFRE"],["UNE","BROSSE","PILOU"],["ACHETÉE"],["UNE","OFFERTE !"]],
 [["FONCE !"],["LIEN","EN","BIO !"]]]
EXTRA=[0.0]*len(PHRASES)    # la voix est utilisée telle quelle, sans pause ajoutée
# plans de la vidéo A d'origine (frames 1-based) et repères de coupe (phrase, mot, avance en s)
SHOTS=[('S1',1,67),('S3',115,169),('S4',170,253),('S5',254,336),('S6',337,407),('S7',408,479),('S8',480,544),('S9',545,576),('S10',577,656)]
CUTMARKS=[(1,0,0.20),(2,0,0.22),(4,0,0.22),(5,5,0.08),(6,0,0.20),(8,0,0.15),(9,0,0.18),(9,3,0.06)]
OUT='PILOU_video_A_offre_v3.mp4'
