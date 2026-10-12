# Retouche de la vidéo Pilou

Scripts utilisés pour corriger la pub (vidéo 480x854, 24 i/s, 27,33 s).

1. `voix_sans_embouts.py` : remplace « en métal » par « sans embouts » (8,44 s → 9,02 s). Dans l'original,
   « les brosses‿en » se prononce déjà « bro-ssan » : il est gardé tel quel (seul le /s/ est allongé), puis
   raccordé à « ‿embouts » (pris dans « des‿embouts souples ») sur une impulsion de la voix, à hauteur égale.
   Aucune retouche de hauteur ni de durée. Le reste de la bande son est inchangé, à l'échantillon près.
2. `fix_caption.py` : remplace le sous-titre « EN MÉTAL » par « SANS EMBOUTS » (frames 205 à 215, EMBOUTS en bleu dès la frame 207).
   Police retrouvée : Inter Bold, contour (17,17,17), blanc (253,253,248), bleu actif (83,171,246).
3. `build.py` : réassemble la vidéo à partir des frames YUV d'origine, en ne réécrivant que les pixels modifiés.
4. `prep_shots.py`, `captl.py`, `../refaire_plans_brosse.py` : préparation et génération (kie.ai) des plans
   de brossage avec la vraie brosse Pilou (14,00–16,96 s et 19,96–22,67 s).

Les scripts lisent leurs fichiers de travail dans `$PILOU_WORK` (frames, audio, polices).
