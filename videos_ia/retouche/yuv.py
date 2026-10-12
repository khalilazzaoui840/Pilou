"""Conversion RGB <-> YUV420p BT.601 limited, identique au décodage ffmpeg, pour ne retoucher que les pixels modifiés."""
import numpy as np
W,H=480,854
FS=W*H*3//2
def read_frames(path):
    d=np.fromfile(path,np.uint8); n=len(d)//FS
    return d.reshape(n,FS)
def split(fr):
    Y=fr[:W*H].reshape(H,W); U=fr[W*H:W*H+W*H//4].reshape(H//2,W//2); V=fr[W*H+W*H//4:].reshape(H//2,W//2)
    return Y,U,V
def rgb2yuv(rgb):
    r,g,b=[rgb[...,k].astype(float) for k in range(3)]
    Y=16.91+(65.481*r+128.553*g+24.966*b)/255   # +0.91: compense l arrondi par troncature du décodage RGB de ffmpeg
    U=128+(-37.797*r-74.203*g+112.0*b)/255
    V=128+(112.0*r-93.786*g-18.214*b)/255
    return Y,U,V
def patch(fr,rgb_new,mask):
    """remplace dans la frame yuv les pixels où mask>0 (mask float 0..1) par rgb_new"""
    Y,U,V=split(fr.copy())
    Y=Y.astype(float); U=U.astype(float); V=V.astype(float)
    y,u,v=rgb2yuv(rgb_new)
    Y=Y*(1-mask)+y*mask
    m2=mask.reshape(H//2,2,W//2,2).mean((1,3))
    u2=u.reshape(H//2,2,W//2,2).mean((1,3)); v2=v.reshape(H//2,2,W//2,2).mean((1,3))
    U=U*(1-m2)+u2*m2; V=V*(1-m2)+v2*m2
    out=np.concatenate([np.clip(np.round(Y),0,255).astype(np.uint8).ravel(),
                        np.clip(np.round(U),0,255).astype(np.uint8).ravel(),
                        np.clip(np.round(V),0,255).astype(np.uint8).ravel()])
    return out
