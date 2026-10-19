"""Sous-titres de la vidéo B, image par image, au style de la vidéo A (blanc + mot actif doré)."""
import numpy as np, sys
sys.path.insert(0,'/tmp/claude-0/-home-user-Pilou/a4115cab-5bdb-5d46-9461-6f6c68378b97/scratchpad/tools')
import caption as C
from timeline import P2, CUTS, SHOTS, FPS, TOTAL
from words import GROUPS
GOLD=np.array([201,138,76.]); BASE_SCALE=0.97; POP=[0.89,0.93]; GAP=0.26; TRACK=0.01   # mesurés sur la vidéo A
LOW=(CUTS[5],CUTS[6])          # plan S8 (chien allongé) : sous-titres plus bas, comme dans A
def windows():
    ev=[]
    for (a,b,ws,_),groups in zip(P2,GROUPS):
        k=0; gl=[]
        for g in groups:
            gl.append([(w,ws[k+j][1]) for j,w in enumerate(g)]); k+=len(g)
        for gi,g in enumerate(gl):
            start=g[0][1]-0.04
            end=(gl[gi+1][0][1]-0.04) if gi+1<len(gl) else b+0.10
            ev.append(dict(words=[w for w,_ in g],onsets=[t for _,t in g],start=start,end=end))
    for e,n in zip(ev,ev[1:]): e['end']=min(e['end'],n['start'])
    ev[-1]['end']=TOTAL                       # « EN DESSOUS ! » reste jusqu'à la fin
    return ev
EV=windows()
def at_frame(j):
    t=j/FPS
    for e in EV:
        if e['start']<=t<e['end']:
            act=max(i for i,o in enumerate(e['onsets']) if o-0.04<=t) if t>=e['onsets'][0]-0.04 else 0
            age=int(round((t-e['start'])*FPS))
            sc=POP[age] if age<len(POP) else BASE_SCALE
            dy=62 if LOW[0]<=e['start']<LOW[1] else -1
            return dict(words=e['words'],active=act,scale=sc,dy=dy)
    return None
def draw(frame,c):
    if c is None: return frame
    p=dict(cx=239,base=577+c['dy'],anchor_y=595+c['dy'],gap=GAP,tracking=TRACK)
    aF,aB,aS=C.render(c['words'],c['active'],p,c['scale'],frame.shape[0],frame.shape[1])
    from scipy import ndimage as ndi
    aF,aB,aS=ndi.gaussian_filter(aF,0.45),ndi.gaussian_filter(aB,0.45),ndi.gaussian_filter(aS,0.6)
    out=frame.astype(float)
    out=out*(1-aS[...,None])+C.STROKE*aS[...,None]
    t=np.clip(aB/np.maximum(aF,1e-6),0,1)[...,None]
    out=out*(1-aF[...,None])+(np.array([255,254,254.])*(1-t)+GOLD*t)*aF[...,None]
    return np.clip(np.round(out),0,255).astype(np.uint8)
if __name__=='__main__':
    for e in EV: print(f"{e['start']:6.2f}-{e['end']:6.2f} {' '.join(e['words'])}")
