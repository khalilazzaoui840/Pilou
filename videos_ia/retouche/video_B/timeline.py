"""Minutage de la vidéo B (25 s) : voix d'origine + pauses ajoutées, coupes calées sur les phrases."""
from words import PHRASES, GROUPS, EXTRA
TOTAL=25.0; FPS=24
def phrases_out():
    shift=0; out=[]
    for k,(a,b,ws) in enumerate(PHRASES):
        out.append((a+shift,b+shift,[(w,t+shift) for w,t in ws],shift)); shift+=EXTRA[k]
    return out
P2=phrases_out()
def on(p,w=0): return P2[p][2][w][1]
# plans de la vidéo A (frames 1-based incluses) et coupes dans la vidéo B
SHOTS=[('S3',115,169),('S4',170,253),('S5',254,336),('S6',337,407),('S7',408,479),('S8',480,544),('S9',545,576),('S10',577,656)]
CUTS=[0.0, on(1)-0.22, on(3)-0.22, on(4,5)-0.08, on(5)-0.20, on(7)-0.15, on(8)-0.18,
      on(8,5)-0.06,   # S10 dès « sans douleur » : la brosse Pilou à l'écran
      TOTAL]
if __name__=='__main__':
    print('fin voix', round(P2[-1][1],2))
    for (n,a,b),c0,c1 in zip(SHOTS,CUTS[:-1],CUTS[1:]):
        need=(c1-c0)*FPS; have=b-a+1
        print(f'{n}: {c0:6.2f}->{c1:6.2f} besoin {need:5.1f} dispo {have} vitesse {have/need:4.2f}x')
