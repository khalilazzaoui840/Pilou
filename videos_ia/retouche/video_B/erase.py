"""Efface les anciens sous-titres de la vidéo A (plans S3 à S10) avec ProPainter, sur une bande autour du texte."""
import numpy as np, json, os, sys, subprocess, shutil
sys.path.insert(0,'/tmp/claude-0/-home-user-Pilou/a4115cab-5bdb-5d46-9461-6f6c68378b97/scratchpad/tools')
import caption as C
from PIL import Image
from scipy import ndimage as ndi
from timeline import SHOTS
VB='/tmp/claude-0/-home-user-Pilou/a4115cab-5bdb-5d46-9461-6f6c68378b97/scratchpad/videoB/'
PP='/tmp/claude-0/-home-user-Pilou/a4115cab-5bdb-5d46-9461-6f6c68378b97/scratchpad/ext/pp/src'
PY='/tmp/claude-0/-home-user-Pilou/a4115cab-5bdb-5d46-9461-6f6c68378b97/scratchpad/venv/bin/python'
TL=json.load(open(VB+'captA_timeline.json'))
MIN_SCORE=float(os.environ.get('MIN_SCORE','2.0'))
def mask_for(i):
    r=TL[str(i)]
    aF,aB,aS=C.render(r['words'],r['active'],dict(cx=240+r['dx'],base=577+r['dy'],anchor_y=595+r['dy'],gap=0.26,tracking=0.01),r['scale'])
    m=ndi.binary_dilation(np.maximum(aS,aF)>0.03,iterations=2)
    if r['score']<MIN_SCORE:
        # repérage incertain : on prend aussi tout ce qui ressemble à du texte (blanc / doré + contour) dans la bande
        a=np.asarray(Image.open(VB+f'A_full/{i:04d}.png').convert('RGB')).astype(int)
        y0=530 if r['dy']<30 else 592
        txt=(a.min(2)>225)|(np.abs(a-np.array([201,138,76])).max(2)<30)
        band=np.zeros_like(txt); band[y0:y0+60,60:420]=True
        txt&=band
        dark=(a.mean(2)<55)&ndi.binary_dilation(txt,iterations=5)
        m=ndi.binary_dilation(m|txt|dark,iterations=4)
    return m,r
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
