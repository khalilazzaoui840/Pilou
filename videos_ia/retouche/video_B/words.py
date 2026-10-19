# Débuts de mots (s) dans la voix B d'origine (video_2.mp3), d'après les phonèmes + pauses.
# Chaque phrase : (début, fin, [(mot, début), ...])
PHRASES=[
 (0.04,2.31,[("TON",0.04),("CHIEN",0.25),("S'ENFUIT",0.49),("EN",0.79),("COURANT",0.91),("DÈS",1.30),("QUE",1.42),("TU",1.49),("SORS",1.63),("LA",1.79),("BROSSE ?",1.90)]),
 (2.64,3.26,[("NORMAL",2.64)]),
 (3.44,5.57,[("LES",3.46),("BROSSES",3.60),("SANS",3.88),("EMBOUTS",4.12),("TIRENT",4.50),("ET",4.92),("GRIFFENT",5.05)]),
 (5.92,7.59,[("LA",5.92),("BROSSE",6.01),("PILOU",6.28),("C'EST",6.76),("DIFFÉRENT",6.89)]),
 (7.83,12.04,[("DES",7.83),("EMBOUTS",7.97),("SOUPLES",8.32),("QUI",8.71),("RETIRENT",8.80),("TOUT",9.34),("LE",9.49),("SOUS-POIL",9.61),("MORT",10.00),
              ("EN",10.33),("DOUCEUR",10.48),("SANS",11.13),("LUI",11.38),("FAIRE",11.56),("MAL",11.74)]),
 (12.38,13.01,[("LE",12.38),("RÉSULTAT ?",12.48)]),
 (13.35,15.20,[("DES",13.35),("POIGNÉES",13.54),("DE",13.84),("POILS",13.93),("À",14.27),("CHAQUE",14.44),("PASSAGE",14.68)]),
 (15.50,18.16,[("ET",15.50),("UN",15.61),("CHIEN",15.78),("ENFIN",16.12),("DÉTENDU",16.57),("QUI",17.24),("ADORE",17.54),("ÇA",17.92)]),
 (18.57,20.46,[("TON",18.57),("CHIEN",18.74),("MÉRITE",18.94),("UN",19.27),("BROSSAGE",19.33),("SANS",19.84),("DOULEUR",20.00)]),
 (20.68,22.93,[("ALORS",20.68),("COMMANDE",20.92),("TA",21.22),("BROSSE",21.33),("PILOU",21.58),("C'EST",22.09),("JUSTE",22.24),("EN",22.50),("DESSOUS !",22.58)]),
]
# Groupes de sous-titres (indices de mots consécutifs par phrase), comme dans la vidéo A
GROUPS=[[["TON","CHIEN"],["S'ENFUIT"],["EN","COURANT"],["DÈS","QUE","TU"],["SORS","LA","BROSSE ?"]],
 [["NORMAL"]],
 [["LES","BROSSES"],["SANS","EMBOUTS"],["TIRENT","ET","GRIFFENT"]],
 [["LA","BROSSE","PILOU"],["C'EST","DIFFÉRENT"]],
 [["DES","EMBOUTS"],["SOUPLES"],["QUI","RETIRENT"],["TOUT","LE"],["SOUS-POIL","MORT"],["EN","DOUCEUR"],["SANS","LUI"],["FAIRE","MAL"]],
 [["LE","RÉSULTAT ?"]],
 [["DES","POIGNÉES"],["DE","POILS"],["À","CHAQUE"],["PASSAGE"]],
 [["ET","UN","CHIEN"],["ENFIN","DÉTENDU"],["QUI","ADORE","ÇA"]],
 [["TON","CHIEN"],["MÉRITE","UN"],["BROSSAGE"],["SANS","DOULEUR"]],
 [["ALORS","COMMANDE"],["TA","BROSSE","PILOU"],["C'EST","JUSTE"],["EN","DESSOUS !"]]]
# Pauses ajoutées APRÈS chaque phrase (s) pour atteindre 25 s sans toucher à la voix
EXTRA=[0.10,0.10,0.15,0.10,0.15,0.15,0.10,0.15,0.05,0.0]
