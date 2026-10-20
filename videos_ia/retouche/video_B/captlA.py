"""Vidéo A (sous-titres blanc/doré) : retrouve pour chaque frame le sous-titre affiché -> masque précis à effacer.
Version rapide : tout est calculé sur la bande du sous-titre, rendus mis en cache."""
import numpy as np, sys, os, json
sys.path.insert(0,os.path.dirname(__file__))
import caption as C
from PIL import Image
from multiprocessing import Pool
VB=__import__('os').environ.get('PILOU_WORK','travail')+'/videoB/'
GOLD=np.array([201,138,76.]); STYLE=dict(gap=0.26,tracking=0.01); STEADY=0.97
Y0,Y1=500,690
G=lambda s:[w.split() for w in s]
SHOTS={
 'S1':(1,67,G(['TON CHIEN','PERD SES POILS','PARTOUT ?','SUR LE CANAPÉ']),[0]),
 'S2':(68,114,G(['SUR LE CANAPÉ','LES VÊTEMENTS','DANS TOUTE','LA MAISON']),[0]),
 'S3':(115,169,G(['LA MAISON','ET EN PLUS','IL DÉTESTE','LE BROSSAGE']),[0]),
 'S4':(170,253,G(['LE BROSSAGE','NORMAL','LES BROSSES','SANS EMBOUTS','TIRENT ET GRIFFENT']),[0]),
 'S5':(254,336,G(['TIRENT ET GRIFFENT','LA BROSSE PILOU',"C'EST DIFFÉRENT",'DES EMBOUTS','SOUPLES','QUI RETIRENT']),[0]),
 'S6':(337,407,G(['QUI RETIRENT','TOUT LE','SOUS-POIL MORT','EN DOUCEUR','SANS LUI','FAIRE MAL']),[0]),
 'S7':(408,479,G(['FAIRE MAL','LE RÉSULTAT ?','DES POIGNÉES','DE POILS','À CHAQUE','PASSAGE']),[0]),
 'S8':(480,544,G(['PASSAGE','ET UN CHIEN','ENFIN DÉTENDU','QUI ADORE ÇA']),[0,62]),
 'S9':(545,576,G(['QUI ADORE ÇA','FINI LES POILS','PARTOUT']),[0,62]),
 'S10':(577,656,G(['PARTOUT','LA BROSSE PILOU','FONCE !','LIEN EN BIO !']),[0])}
SCALES=[0.89,0.93,0.95,STEADY]
def cand_list(groups,DYS):
    out=[]
    for w in groups:
        for act in range(len(w)):
            for s in SCALES:
                for dx in (-1,0,1):
                    for dy in (-2,-1,0):
                        for D in DYS: out.append((tuple(w),act,s,dx,dy+D))
    return out
def render_idx(c):
    w,act,s,dx,dy=c
    aF,aB,aS=C.render(list(w),act,dict(cx=240+dx,base=577+dy,anchor_y=595+dy,**STYLE),s)
    aF,aB,aS=aF[Y0:Y1],aB[Y0:Y1],aS[Y0:Y1]
    F=aF>0.6; B=aB>0.6
    W=np.flatnonzero(F&~B); Gi=np.flatnonzero(B); K=np.flatnonzero((aS>0.6)&~(aF>0.2))
    return W,Gi,K
def run_shot(name):
    a,b,groups,DYS=SHOTS[name]
    cands=cand_list(groups,DYS); idx=[render_idx(c) for c in cands]
    res={}
    for i in range(a,b+1):
        im=np.asarray(Image.open(VB+f'A_full/{i:04d}.png').convert('RGB')).astype(float)[Y0:Y1]
        isW=((im.min(2)>225)).ravel(); isG=(np.abs(im-GOLD).max(2)<38).ravel(); isK=(im.mean(2)<55).ravel()
        best=(-1,None)
        for c,(W,Gi,K) in zip(cands,idx):
            s=(isW[W].mean() if len(W) else 0.5)+(isG[Gi].mean() if len(Gi) else 0.5)+isK[K].mean()
            if s>best[0]: best=(s,c)
        s,(w,act,sc,dx,dy)=best
        res[i]=dict(words=list(w),active=act,scale=sc,dx=dx,dy=dy,score=round(float(s),3))
    return res
if __name__=='__main__':
    with Pool(4) as p: parts=p.map(run_shot,list(SHOTS))
    res={}
    for d in parts: res.update(d)
    json.dump({str(k):v for k,v in res.items()},open(VB+'captA_timeline.json','w'),ensure_ascii=False)
    for name,(a,b,_,_) in SHOTS.items():
        print(name,' | '.join(f"{i}:{' '.join(res[i]['words'])}[{res[i]['active']}]{res[i]['scale']}/{res[i]['dy']} {res[i]['score']}" for i in range(a,b+1,6)),flush=True)
