"""Rendu des sous-titres au style de la vidéo (Inter Bold, contour sombre, mot actif en bleu)."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi
FONT=os.environ.get('PILOU_WORK','travail')+'/fonts/Inter-Bold.ttf'
SS=4
WHITE=np.array([253,253,248.]); BLUE=np.array([83,171,246.]); STROKE=np.array([17,17,17.])
P=dict(size=41.75, gap=0.26, base=577.0, cx=240.0, stroke=4.4, stroke_alpha=1.0, tracking=0.0, anchor_y=595.0)
def layout(words,size,gap,tracking):
    f=ImageFont.truetype(FONT,int(round(size*SS)))
    ws=[]
    for w in words:
        if tracking==0:
            ws.append([(0,w)])
        else:
            x=0; parts=[]
            for ch in w:
                parts.append((x,ch)); x+=f.getlength(ch)+tracking*size*SS
            ws.append(parts)
    widths=[]
    for w,parts in zip(words,ws):
        widths.append(f.getlength(w) if tracking==0 else parts[-1][0]+f.getlength(parts[-1][1]))
    return f,ws,widths
def render(words,active,p=None,scale=1.0,H=854,W=480):
    """renvoie (alpha_fill, rgb_fill, alpha_stroke) en pleine résolution"""
    p=dict(P,**(p or {}))
    size=p['size']*scale
    f,ws,widths=layout(words,size,p['gap'],p['tracking'])
    gap=p['gap']*size*SS
    total=sum(widths)+gap*(len(words)-1)
    ascent,descent=f.getmetrics()
    # ligne de base: base (pleine échelle) mise à l'échelle autour de anchor_y
    base=p['anchor_y']+(p['base']-p['anchor_y'])*scale
    cx=p['cx']
    pad=int(14*SS)
    Wc=int(total)+2*pad; Hc=int((ascent+descent))+2*pad
    ox=cx*SS-total/2-pad; oy=base*SS-ascent-pad   # origine du canevas en pixels SS
    fill=Image.new('L',(Wc,Hc),0); blue=Image.new('L',(Wc,Hc),0)
    df=ImageDraw.Draw(fill); db=ImageDraw.Draw(blue)
    x=pad
    for k,(w,parts,wd) in enumerate(zip(words,ws,widths)):
        for dx,ch in parts:
            df.text((x+dx,pad),ch,font=f,fill=255)
            if k==active: db.text((x+dx,pad),ch,font=f,fill=255)
        x+=wd+gap
    F=np.asarray(fill).astype(float)/255; B=np.asarray(blue).astype(float)/255
    r=p['stroke']*scale*SS
    dist=ndi.distance_transform_edt(F<0.5)
    S=np.clip(r+0.5*SS-dist,0,SS)/SS*p['stroke_alpha']
    # rééchantillonnage vers la grille vidéo
    def down(a):
        x0=ox; y0=oy
        ix=int(np.floor(x0)); iy=int(np.floor(y0))
        # décale au sous-pixel près
        sh=ndi.shift(a,(y0-iy*1.0- (y0-iy) + (y0-np.floor(y0)) - (y0-np.floor(y0)),0),order=1) if False else a
        # positionner sur une grille SS-alignée
        offx=int(round(x0)); offy=int(round(y0))
        big=np.zeros((H*SS,W*SS))
        ys,xs=slice(max(0,offy),min(H*SS,offy+a.shape[0])),slice(max(0,offx),min(W*SS,offx+a.shape[1]))
        big[ys,xs]=a[ys.start-offy:ys.stop-offy, xs.start-offx:xs.stop-offx]
        return big.reshape(H,SS,W,SS).mean((1,3))
    aF=down(F); aB=down(B); aS=down(S)
    return aF,aB,aS
def composite(frame,words,active,p=None,scale=1.0):
    aF,aB,aS=render(words,active,p,scale,frame.shape[0],frame.shape[1])
    out=frame.astype(float)
    out=out*(1-aS[...,None])+STROKE*aS[...,None]
    col=np.where(aB[...,None]>0,1,0)
    fillcol=WHITE*(1-np.clip(aB/np.maximum(aF,1e-6),0,1))[...,None]+BLUE*np.clip(aB/np.maximum(aF,1e-6),0,1)[...,None]
    out=out*(1-aF[...,None])+fillcol*aF[...,None]
    return np.clip(out,0,255).astype(np.uint8), np.maximum(aS,aF)
