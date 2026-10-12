"""Frames 205-215 : remplace le sous-titre « EN MÉTAL » par « SANS EMBOUTS »."""
import numpy as np, sys, os, cv2
sys.path.insert(0,os.path.dirname(__file__))
from fontfit import fillmask
import caption as C
from scipy import ndimage as ndi
from PIL import Image
ED=os.environ.get('PILOU_WORK','travail')+'/edit/'
OUT=ED+'cap_fixed/'; os.makedirs(OUT,exist_ok=True)
SCALE={205:0.927,206:0.971}
ACTIVE_SWITCH=208   # EMBOUTS surligné à partir de cette frame (début du /z/ à 8.608 s)
def soften(a,s=0.45): return ndi.gaussian_filter(a,s)
for i in range(205,216):
    a=np.asarray(Image.open(ED+f'full/{i:04d}.png').convert('RGB')).copy()
    m=fillmask(a.astype(int)); m[:525]=0; m[600:]=0; m[:,:110]=0; m[:,370:]=0
    dist=ndi.distance_transform_edt(~m)
    hole=(dist<=7.0); hole[:520]=0; hole[605:]=0
    bgr=cv2.cvtColor(a,cv2.COLOR_RGB2BGR)
    clean=cv2.inpaint(bgr,hole.astype(np.uint8)*255,9,cv2.INPAINT_TELEA)
    clean=cv2.cvtColor(clean,cv2.COLOR_BGR2RGB)
    s=SCALE.get(i,1.0)
    aF,aB,aS=C.render(['SANS','EMBOUTS'],0 if i<ACTIVE_SWITCH else 1,None,s,a.shape[0],a.shape[1])
    aF,aB,aS=soften(aF),soften(aB),soften(aS,0.6)
    out=clean.astype(float)
    out=out*(1-aS[...,None])+C.STROKE*aS[...,None]
    t=np.clip(aB/np.maximum(aF,1e-6),0,1)[...,None]
    out=out*(1-aF[...,None])+(C.WHITE*(1-t)+C.BLUE*t)*aF[...,None]
    Image.fromarray(np.clip(np.round(out),0,255).astype(np.uint8)).save(OUT+f'{i:04d}.png')
    if i==210: Image.fromarray(clean).save(ED+'clean210.png')
print('ok')
