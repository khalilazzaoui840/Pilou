# Vidéo B (test A/B Meta) — 25 s

Même milieu que la vidéo A, nouvelle accroche et nouvelle fin :
- Accroche : « Ton chien s'enfuit en courant dès que tu sors la brosse ? »
- Fin : « Ton chien mérite un brossage sans douleur. Alors commande ta brosse Pilou, c'est juste en dessous ! »

Étapes :
1. `build_audio.py` : voix ElevenLabs telle quelle + pauses ajoutées (1,05 s au total) pour faire 25,0 s, volume calé sur A (-16,6 LUFS mono).
2. `captlA.py` + `erase.py` : repérage des anciens sous-titres de A image par image, effacement avec ProPainter.
3. `timeline.py` / `build_B.py` : plans de A recalés sur les phrases ; les images ajoutées pour remplir la durée sont placées aux moments où l'image bouge le moins.
4. `captions_B.py` : sous-titres Inter Bold blanc + mot actif doré (201,138,76), comme A.
