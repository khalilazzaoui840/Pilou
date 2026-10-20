"""Efface les anciens sous-titres de la vidéo A (plans S3 à S10) avec ProPainter, sur une bande autour du texte."""
import numpy as np, json, os, sys, subprocess, shutil
sys.path.insert(0,__import__('os').environ.get('PILOU_WORK','travail')+'/tools')
import caption as C
from PIL import Image
from scipy import ndimage as ndi
from timeline import SHOTS
VB=__import__('os').environ.get('PILOU_WORK','travail')+'/videoB/'
PP=__import__('os').environ.get('PILOU_WORK','travail')+'/ext/pp/src'
PY=__import__('os').environ.get('PILOU_WORK','travail')+'/venv/bin/python'
TL=json.load(open(VB+'captA_timeline.json'))
MIN_SCORE=float(os.environ.get('MIN_SCORE','2.0'))
GOLD=np.array([201,138,76.])
def mask_for(i):
    """masque du sous-titre de la vidéo A sur la frame i (None s'il n'y a pas de sous-titre)"""
    r=TL[str(i)]
    aF,aB,aS=C.render(r['words'],r['active'],dict(cx=240+r['dx'],base=577+r['dy'],anchor_y=595+r['dy'],gap=0.26,tracking=0.01),r['scale'])
    a=np.asarray(Image.open(VB+f'A_full/{i:04d}.png').convert('RGB')).astype(float)
    F=aF>0.6; B=aB>0.6; W=F&~B; K=(aS>0.6)&~(aF>0.2)
    f=lambda m,o: o[m].mean() if m.sum() else 0.0
    w=f(W,a.min(2)>225); g=f(B,np.abs(a-GOLD).max(2)<38); k=f(K,a.mean(2)<55)
    r=dict(r,terms=(round(w,2),round(g,2),round(k,2)))
    sc=TL[str(i)]['score']
    near=lambda j: str(j) in TL and TL[str(j)]['score']>=1.6
    if sc>=2.05: it=3
    elif sc>=1.6: it=6
    elif k>=0.7 and g>=0.6: it=6                         # mot(s) entièrement doré(s) (« PARTOUT ? », « FONCE ! »)
    elif sc>=0.95 and (near(i-1) or near(i+1)): it=6     # image d'apparition/disparition : masque élargi
    else: return None,r                                    # pas de sous-titre (pause)
    return ndi.binary_dilation(np.maximum(aS,aF)>0.03,iterations=it),r
def run(shot):
    name,a,b=[s for s in SHOTS if s[0]==shot][0]
    ms={i:mask_for(i) for i in range(a,b+1)}
    ys=[np.where(m.any(1))[0] for m,_ in ms.values() if m is not None]
    lo=min(y.min() for y in ys); hi=max(y.max() for y in ys)
    c=(lo+hi)//2; y0=max(0,min(854-128,c-64)); y1=y0+128
    work=VB+f'pp_{shot}/'; shutil.rmtree(work,ignore_errors=True)
    os.makedirs(work+shot); os.makedirs(work+'masks')
    for k,i in enumerate(range(a,b+1)):
        Image.open(VB+f'A_full/{i:04d}.png').convert('RGB').crop((0,y0,480,y1)).save(work+f'{shot}/{k:04d}.png')
        m=ms[i][0]; mm=np.zeros((128,480),np.uint8) if m is None else (m[y0:y1]*255).astype(np.uint8)
        Image.fromarray(mm).save(work+f'masks/{k:04d}.png')
    subprocess.run([PY,'inference_propainter.py','-i',work+shot,'-m',work+'masks','-o',work+'out','--save_frames',
                    '--raft_iter','12','--neighbor_length','8','--ref_stride','12','--subvideo_length','60','--mask_dilation','3'],
                   cwd=PP,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    # recolle la bande nettoyée dans les frames complètes
    out=VB+'A_clean/'; os.makedirs(out,exist_ok=True)
    for k,i in enumerate(range(a,b+1)):
        full=np.asarray(Image.open(VB+f'A_full/{i:04d}.png').convert('RGB')).copy()
        band=np.asarray(Image.open(work+f'out/{shot}/frames/{k:04d}.png').convert('RGB'))
        m=ms[i][0]
        if m is not None:
            w=ndi.gaussian_filter(ndi.binary_dilation(m,iterations=4).astype(float),1.5)[y0:y1,...,None]
            full[y0:y1]=np.round(full[y0:y1]*(1-w)+band*w).astype(np.uint8)
        Image.fromarray(full).save(out+f'{i:04d}.png')
    print(shot,'ok bande',y0,y1,flush=True)
def run_fsr(shot):
    import cv2
    name,a,b=[s for s in SHOTS if s[0]==shot][0]
    out=VB+'A_fsr/'; os.makedirs(out,exist_ok=True)
    for i in range(a,b+1):
        m,_=mask_for(i)
        im=np.asarray(Image.open(VB+f'A_full/{i:04d}.png').convert('RGB'))
        if m is not None:
            m=ndi.binary_dilation(m,iterations=3)
            bgr=cv2.cvtColor(im,cv2.COLOR_RGB2BGR); dst=np.zeros_like(bgr)
            cv2.xphoto.inpaint(bgr,(~m).astype(np.uint8),dst,cv2.xphoto.INPAINT_FSR_FAST)
            im=cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)
        Image.fromarray(im).save(out+f'{i:04d}.png')
    print(shot,'fsr ok',flush=True)
if __name__=='__main__':
    if sys.argv[1]=='--fsr':
        from multiprocessing import Pool
        with Pool(4) as p: p.map(run_fsr,sys.argv[2:])
    else:
        for s in sys.argv[1:]: run(s)
