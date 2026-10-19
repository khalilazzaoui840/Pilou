"""Assemble la vidéo B : plans nettoyés de A recalés sur la nouvelle voix, nouveaux sous-titres, audio B."""
import numpy as np, sys, os, subprocess, glob, shutil
from PIL import Image
sys.path.insert(0,__import__('os').environ.get('PILOU_WORK','travail')+'/tools')
import yuv
from timeline import SHOTS, CUTS, FPS, TOTAL
import captions_B as CB
VB=__import__('os').environ.get('PILOU_WORK','travail')+'/videoB/'
SRC=os.environ.get('SRC','A_clean')
def motion(a,b):
    prev=None; m=[]
    for i in range(a,b+1):
        g=np.asarray(Image.open(VB+f'A_full/{i:04d}.png').convert('L').resize((120,214))).astype(float)
        if prev is not None: m.append(np.abs(g-prev).mean())
        prev=g
    return np.array(m)
def interp_dir(shot,a,b):
    """images intermédiaires (x2) par interpolation de mouvement ; on n'en garde que quelques-unes, aux moments calmes"""
    d=VB+f'interp_{shot}/'
    if not os.path.isdir(d):
        os.makedirs(d); src=d+'src/'; os.makedirs(src)
        for k,i in enumerate(range(a,b+1)): os.symlink(VB+SRC+f'/{i:04d}.png',src+f'{k:04d}.png')
        subprocess.run(['ffmpeg','-v','error','-y','-framerate','24','-i',src+'%04d.png',
                        '-frames:v',str(2*(b-a+1)-1),'-vf','minterpolate=fps=48:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1',
                        d+'%05d.png'],check=True)
    return d
def plan():
    frames=[]
    for (name,a,b),c0,c1 in zip(SHOTS,CUTS[:-1],CUTS[1:]):
        n_out=int(round(c1*FPS))-int(round(c0*FPS)); have=b-a+1; extra=n_out-have
        seq=[VB+SRC+f'/{i:04d}.png' for i in range(a,b+1)]
        if extra<0: seq=seq[:n_out]
        elif extra>0:
            m=motion(a,b); idir=interp_dir(name,a,b)
            chosen=[]
            for k in np.argsort(m,kind='stable'):     # les passages où l'image bouge le moins
                if m[k]>=0.3 and all(abs(k-c)>=2 for c in chosen): chosen.append(k)
                if len(chosen)==extra: break
            assert len(chosen)==extra,(name,extra)
            ins={k:(idir+f'{2*k+2:05d}.png' if m[k]>=0.3 and os.path.exists(idir+f'{2*k+2:05d}.png') else seq[k]) for k in chosen}
            out=[]
            for k,p in enumerate(seq):
                out.append(p)
                if k in ins: out.append(ins[k])
            seq=out
        assert len(seq)==n_out
        frames+=seq
        print(f'{name}: {n_out} images, {max(extra,0)} ajoutées aux moments calmes' + (f', {-extra} coupées' if extra<0 else ''))
    assert len(frames)==int(round(TOTAL*FPS)), len(frames)
    return frames
if __name__=='__main__':
    frames=plan()
    out=VB+'B_frames/'; shutil.rmtree(out,ignore_errors=True); os.makedirs(out)
    raw=open(VB+'B.yuv','wb')
    for j,p in enumerate(frames):
        im=np.asarray(Image.open(p).convert('RGB'))
        im=CB.draw(im,CB.at_frame(j))
        Image.fromarray(im).save(out+f'{j:04d}.png')
        Y,U,V=yuv.rgb2yuv(im)
        Y=np.clip(np.round(Y),0,255).astype(np.uint8)
        U=np.clip(np.round(U.reshape(427,2,240,2).mean((1,3))),0,255).astype(np.uint8)
        V=np.clip(np.round(V.reshape(427,2,240,2).mean((1,3))),0,255).astype(np.uint8)
        raw.write(Y.tobytes()); raw.write(U.tobytes()); raw.write(V.tobytes())
    raw.close()
    subprocess.run(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','yuv420p','-s','480x854','-r','24','-i',VB+'B.yuv',
        '-i',VB+'voB_proc.wav','-map','0:v','-map','1:a','-c:v','libx264','-preset','slow','-crf','14','-profile:v','high',
        '-pix_fmt','yuv420p','-colorspace','smpte170m','-color_primaries','bt709','-color_trc','bt709','-color_range','tv',
        '-c:a','aac','-b:a','192k','-ar','44100','-ac','2','-movflags','+faststart','-t',str(TOTAL),VB+'PILOU_video_B.mp4'],check=True)
    os.remove(VB+'B.yuv'); print('ok')
