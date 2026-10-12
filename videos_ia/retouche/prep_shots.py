"""Prépare les plans de brossage : retrait des sous-titres, clips 720x1280 sans texte, images de référence de la brosse."""
import numpy as np, sys, os, json, cv2, subprocess
sys.path.insert(0,os.path.dirname(__file__))
from fontfit import fillmask
from scipy import ndimage as ndi
from PIL import Image
ED=os.environ.get('PILOU_WORK','travail')+'/edit/'
OUT=ED+'shots/'; os.makedirs(OUT,exist_ok=True)
SHOTS={'s6':(337,407,0),'s8':(480,544,62)}
for name,(a,b,dy) in SHOTS.items():
    d=OUT+name+'_clean/'; os.makedirs(d,exist_ok=True)
    for i in range(a,b+1):
        im=np.asarray(Image.open(ED+f'full/{i:04d}.png').convert('RGB')).copy()
        m=fillmask(im.astype(int))
        ii=im.astype(int); m|=(ii[...,2]>ii[...,0]+25)&(ii[...,2]>110)   # halos bleutés
        y0=520+dy if i!=480 else 520
        band=np.zeros_like(m); band[y0:y0+90,40:440]=1
        m&=band.astype(bool)
        hole=ndi.distance_transform_edt(~m)<=8.5
        hole&=ndi.binary_dilation(band.astype(bool),iterations=8)
        bgr=cv2.cvtColor(im,cv2.COLOR_RGB2BGR)
        mask=(~hole).astype(np.uint8)   # xphoto: 1 = pixel valide
        dst=np.zeros_like(bgr)
        cv2.xphoto.inpaint(bgr,mask,dst,cv2.xphoto.INPAINT_FSR_FAST)
        Image.fromarray(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)).save(d+f'{i:04d}.png')
        np.save(d+f'hole_{i:04d}.npy',hole)
    # clip 720x1280 pour le modèle (24 i/s)
    subprocess.run(['ffmpeg','-v','error','-y','-framerate','24','-start_number',str(a),'-i',d+'%04d.png',
                    '-vf','scale=720:1280:flags=lanczos','-c:v','libx264','-crf','12','-pix_fmt','yuv420p',OUT+f'{name}_clean_720.mp4'],check=True)
    print(name,'ok')
