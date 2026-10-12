"""Retrouve, pour chaque frame d'un plan, le sous-titre affiché (groupe, mot actif, échelle) en le re-rendant."""
import numpy as np, sys, os, json
sys.path.insert(0,os.path.dirname(__file__))
from fontfit import fillmask
import caption as C
from PIL import Image
ED=os.environ.get('PILOU_WORK','travail')+'/edit/'
SHOTS={'s6':(337,407,[['QUI','RETIRENT'],['TOUT','LE'],['SOUS-POIL','MORT'],['EN','DOUCEUR'],['SANS','LUI'],['FAIRE','MAL']]),
       's8':(480,544,[['PASSAGE'],['ET','UN','CHIEN'],['ENFIN','DÉTENDU'],['QUI','ADORE','ÇA']])}
SCALES=[0.88,0.9,0.927,0.95,0.971,0.985,1.0]
cache={}
DY={'s6':0.0,'s8':0.0}
CUR='s6'
def cand(words,act,s):
    k=(tuple(words),act,s,DY[CUR])
    if k not in cache:
        aF,aB,aS=C.render(words,act,dict(base=C.P['base']+DY[CUR],anchor_y=C.P['anchor_y']+DY[CUR]),s); cache[k]=(aF>0.5,aB>0.5)
    return cache[k]
def best_for(i,groups):
    a=np.asarray(Image.open(ED+f'full/{i:04d}.png').convert('RGB')).astype(int)
    y0=525+int(DY[CUR]); m=fillmask(a); m[:y0]=0; m[y0+75:]=0
    r,g,b=a[...,0],a[...,1],a[...,2]
    blue=(b>190)&(r<150)&(b-r>70); blue&=m
    if m.sum()<200: return None
    best=(-1,None)
    for gi,w in enumerate(groups):
        for act in range(len(w)):
            for s in SCALES:
                F,B=cand(w,act,s)
                iou=(F&m).sum()/((F|m).sum()+1e-9)
                biou=(B&blue).sum()/((B|blue).sum()+1e-9)
                sc=iou+0.5*biou
                if sc>best[0]: best=(sc,dict(words=w,active=act,scale=s,iou=round(float(iou),3),biou=round(float(biou),3)))
    return best[1]
def main():
    out={}
    global CUR
    for name,(a,b,groups) in SHOTS.items():
        CUR=name
        tl={}
        for i in range(a,b+1):
            r=best_for(i,groups); tl[i]=r
            print(name,i,None if r is None else (' '.join(r['words']),r['active'],r['scale'],r['iou'],r['biou']))
        out[name]=tl
    json.dump(out,open(ED+'caption_timeline.json','w'),ensure_ascii=False,indent=0)

if __name__=='__main__':
    import sys as _s
    if len(_s.argv)>1: DY['s8']=float(_s.argv[1])
    main()
