"""Montage d'une vidéo Pilou (25 s) : voix ElevenLabs + plans nettoyés de la vidéo A + sous-titres blanc/doré.
À lancer depuis le dossier de la version (A/ ou B/) qui contient words.py."""
import numpy as np, sys, os, subprocess, shutil, wave, json
from PIL import Image
from scipy import ndimage as ndi
HERE=os.getcwd(); sys.path.insert(0,HERE)
SCR=__import__('os').environ.get('PILOU_WORK','travail')+'/'
sys.path.insert(0,SCR+'tools')
import caption as C, yuv
from words import VO, MP3, PHRASES, GROUPS, EXTRA, SHOTS, CUTMARKS, OUT
try: from words import HOLD
except ImportError: HOLD={}
VB=SCR+'videoB/'                 # images de la vidéo A : A_full (brutes), A_clean (sous-titres effacés)
SRC=VB+'A_clean/'
FPS=24
import math
_w=wave.open(VO); TOTAL=_w.getnframes()/_w.getframerate(); _w.close()   # la vidéo dure exactement comme la voix
NFR=math.ceil(TOTAL*FPS)
GOLD=np.array([201,138,76.]); WHITE=np.array([255,254,254.])
BASE_SCALE=0.97; POP=[0.89,0.93]; STYLE=dict(gap=0.26,tracking=0.01)      # mesurés sur la vidéo A
# ---------- minutage ----------
def phrases_out():
    shift=0; out=[]
    for k,(a,b,ws) in enumerate(PHRASES):
        out.append((a+shift,b+shift,[(w,t+shift) for w,t in ws])); shift+=EXTRA[k]
    return out
P2=phrases_out()
CUTS=[0.0]+[P2[p][2][w][1]-lead for p,w,lead in CUTMARKS]+[TOTAL]
# ---------- audio ----------
def build_audio():
    w=wave.open(VO); sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float)/32768; w.close()
    gaps=[(PHRASES[k][1],PHRASES[k+1][0]) for k in range(len(PHRASES)-1)]
    a,b=max(gaps,key=lambda g:g[1]-g[0]); room=x[int((a+0.03)*sr):int((b-0.03)*sr)]   # silence d'origine
    tone=lambda n: np.tile(room,n//len(room)+2)[:n]
    out=[]; pos=0
    for k,(a,b,ws) in enumerate(PHRASES):
        if EXTRA[k]<=0: continue
        nxt=PHRASES[k+1][0] if k+1<len(PHRASES) else len(x)/sr
        cut=int(round((b+nxt)/2*sr)); out+= [x[pos:cut], tone(int(round(EXTRA[k]*sr)))]; pos=cut
    out.append(x[pos:]); y=np.concatenate(out)
    n=int(round(TOTAL*sr)); assert len(y)<=n, f'voix trop longue : {len(y)/sr:.2f} s'
    y=np.concatenate([y,tone(n-len(y))])
    w=wave.open(HERE+'/vo_timed_raw.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((np.clip(y,-1,1)*32767).astype(np.int16).tobytes()); w.close()
    # même traitement et même niveau que la vidéo A (-16,6 LUFS mono, crête -0,9 dBFS)
    peak=np.abs(x).max(); pre=20*np.log10(0.238/peak)    # la voix précédente avait une crête de 0,238
    chain=f"volume={18+pre:.2f}dB,acompressor=threshold=-20dB:ratio=2:attack=5:release=90:makeup=1,volume=4.2dB,alimiter=limit=0.89:attack=3:release=60:level=0"
    subprocess.run(['ffmpeg','-v','error','-y','-i',HERE+'/vo_timed_raw.wav','-af',chain,'-ar','44100',HERE+'/vo_proc.wav'],check=True)
    r=subprocess.run(['ffmpeg','-nostats','-i',HERE+'/vo_proc.wav','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
    I=float([l for l in r.splitlines() if l.strip().startswith('I:')][-1].split()[1])
    if abs(I+16.6)>0.3:      # ajuste au besoin
        chain=chain.replace('volume=4.2dB',f'volume={4.2+(-16.6-I):.2f}dB')
        subprocess.run(['ffmpeg','-v','error','-y','-i',HERE+'/vo_timed_raw.wav','-af',chain,'-ar','44100',HERE+'/vo_proc.wav'],check=True)
    r=subprocess.run(['ffmpeg','-nostats','-i',HERE+'/vo_proc.wav','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
    print('audio :',[l.strip() for l in r.splitlines() if l.strip().startswith(('I:','Peak:'))][-2:])
# ---------- sous-titres ----------
def windows():
    ev=[]
    for (a,b,ws),groups in zip(P2,GROUPS):
        k=0; gl=[]
        for g in groups: gl.append([(w,ws[k+j][1]) for j,w in enumerate(g)]); k+=len(g)
        for g in gl: ev.append(dict(words=[w for w,_ in g],onsets=[t for _,t in g],start=g[0][1]-0.04))
    for e,n in zip(ev,ev[1:]): e['end']=n['start']          # le groupe reste jusqu'au suivant
    ev[-1]['end']=TOTAL
    return ev
EV=windows()
LOW=[(CUTS[i],CUTS[i+1]) for i,s in enumerate(SHOTS) if s[0]=='S8'][0]   # plan du chien allongé : texte plus bas
def caption_at(j):
    t=j/FPS
    for e in EV:
        if e['start']<=t<e['end']:
            act=max([i for i,o in enumerate(e['onsets']) if o-0.04<=t] or [0])
            age=int(round((t-e['start'])*FPS)); sc=POP[age] if age<len(POP) else BASE_SCALE
            return dict(words=e['words'],active=act,scale=sc,dy=62 if LOW[0]<=e['start']<LOW[1] else -1)
    return None
def draw(frame,c):
    if c is None: return frame
    aF,aB,aS=C.render(c['words'],c['active'],dict(cx=239,base=577+c['dy'],anchor_y=595+c['dy'],**STYLE),c['scale'],frame.shape[0],frame.shape[1])
    aF,aB,aS=ndi.gaussian_filter(aF,0.45),ndi.gaussian_filter(aB,0.45),ndi.gaussian_filter(aS,0.6)
    out=frame.astype(float)*(1-aS[...,None])+C.STROKE*aS[...,None]
    t=np.clip(aB/np.maximum(aF,1e-6),0,1)[...,None]
    out=out*(1-aF[...,None])+(WHITE*(1-t)+GOLD*t)*aF[...,None]
    return np.clip(np.round(out),0,255).astype(np.uint8)
# ---------- images ----------
def motion(a,b):
    prev=None; m=[]
    for i in range(a,b+1):
        g=np.asarray(Image.open(VB+f'A_full/{i:04d}.png').convert('L').resize((120,214))).astype(float)
        if prev is not None: m.append(np.abs(g-prev).mean())
        prev=g
    return np.array(m)
def interp_dir(shot,a,b):
    d=HERE+f'/interp_{shot}/'
    if not os.path.isdir(d):
        os.makedirs(d+'src')
        for k,i in enumerate(range(a,b+1)): os.symlink(SRC+f'{i:04d}.png',d+f'src/{k:04d}.png')
        subprocess.run(['ffmpeg','-v','error','-y','-framerate','24','-i',d+'src/%04d.png','-frames:v',str(2*(b-a+1)-1),
                        '-vf','minterpolate=fps=48:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1',d+'%05d.png'],check=True)
    return d
def plan():
    frames=[]
    for (name,a,b),c0,c1 in zip(SHOTS,CUTS[:-1],CUTS[1:]):
        n_all=(NFR if c1>=TOTAL else int(round(c1*FPS)))-int(round(c0*FPS)); hold=HOLD.get(name,0); n_out=n_all-hold
        have=b-a+1; extra=n_out-have
        seq=[SRC+f'{i:04d}.png' for i in range(a,b+1)]
        if extra<0: seq=seq[:n_out]
        elif extra>0:
            m=motion(a,b); idir=interp_dir(name,a,b); chosen=[]
            for k in np.argsort(m,kind='stable'):               # images ajoutées là où ça bouge le moins
                if m[k]>=0.3 and all(abs(k-c)>=2 for c in chosen): chosen.append(k)
                if len(chosen)==extra: break
            assert len(chosen)==extra,(name,extra)
            ins={k:(idir+f'{2*k+2:05d}.png' if os.path.exists(idir+f'{2*k+2:05d}.png') else seq[k]) for k in chosen}
            out=[]
            for k,p in enumerate(seq):
                out.append(p)
                if k in ins: out.append(ins[k])
            seq=out
        if hold:      # plan final : dernière image avec un léger zoom avant progressif
            hd=HERE+f'/hold_{name}/'; os.makedirs(hd,exist_ok=True)
            last=Image.open(seq[-1]).convert('RGB'); W,H=last.size
            for h in range(hold):
                z=1+0.03*(h+1)/hold; w2,h2=W/z,H/z; box=((W-w2)/2,(H-h2)/2,(W+w2)/2,(H+h2)/2)
                last.resize((W,H),Image.LANCZOS,box=box).save(hd+f'{h:03d}.png'); seq.append(hd+f'{h:03d}.png')
        frames+=seq
        print(f'{name}: {c0:5.2f}-{c1:5.2f} s, {n_all} images' + (f' dont {hold} de plan final' if hold else '') + (f', {extra} ajoutées' if extra>0 else f', {-extra} coupées' if extra<0 else ''))
    assert len(frames)==NFR,(len(frames),NFR)
    return frames
def build_audio_raw():
    """voix fournie utilisée telle quelle : aucun traitement, aucune pause ajoutée ; seulement du silence numérique après la fin"""
    w=wave.open(VO); sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),np.int16).copy(); w.close()
    n=int(round(TOTAL*sr)); assert len(x)<=n
    x=np.concatenate([x,np.zeros(n-len(x),np.int16)])
    w=wave.open(HERE+'/vo_proc.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(x.tobytes()); w.close()
    print('audio : voix d origine telle quelle,',round(len(x)/sr,2),'s')
def build():
    frames=plan()
    out=HERE+'/frames/'; shutil.rmtree(out,ignore_errors=True); os.makedirs(out)
    raw=open(HERE+'/v.yuv','wb')
    for j,p in enumerate(frames):
        im=draw(np.asarray(Image.open(p).convert('RGB')),caption_at(j))
        Image.fromarray(im).save(out+f'{j:04d}.png')
        Y,U,V=yuv.rgb2yuv(im)
        raw.write(np.clip(np.round(Y),0,255).astype(np.uint8).tobytes())
        raw.write(np.clip(np.round(U.reshape(427,2,240,2).mean((1,3))),0,255).astype(np.uint8).tobytes())
        raw.write(np.clip(np.round(V.reshape(427,2,240,2).mean((1,3))),0,255).astype(np.uint8).tobytes())
    raw.close()
    subprocess.run(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','yuv420p','-s','480x854','-r','24','-i',HERE+'/v.yuv',
        '-i',MP3,'-map','0:v','-map','1:a','-c:v','libx264','-preset','slow','-crf','14','-profile:v','high',
        '-pix_fmt','yuv420p','-colorspace','smpte170m','-color_primaries','bt709','-color_trc','bt709','-color_range','tv',
        '-c:a','copy','-movflags','+faststart',HERE+'/'+OUT],check=True)
    os.remove(HERE+'/v.yuv')
    json.dump([dict(words=e['words'],start=round(e['start'],2),end=round(e['end'],2)) for e in EV],open(HERE+'/captions.json','w'),ensure_ascii=False,indent=0)
    print('ok ->',OUT)
if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='plan':
        print('coupes',[round(c,2) for c in CUTS]); print('fin voix',round(P2[-1][1],2))
        for (n,a,b),c0,c1 in zip(SHOTS,CUTS[:-1],CUTS[1:]): print(f'{n}: besoin {(c1-c0)*FPS-HOLD.get(n,0):5.1f} images, dispo {b-a+1}, vitesse {(b-a+1)/((c1-c0)*FPS-HOLD.get(n,0)):.2f}x')
        for e in EV: print(f"  {e['start']:6.2f}-{e['end']:6.2f} {' '.join(e['words'])}")
    elif len(sys.argv)==1: build()

# ---------- versions Meta : 1080x1920 (Stories/Reels) et 1080x1350 (4:5, fil) ----------
from PIL import ImageFilter
K=1080/480; HW,HH=1080,1920; FEED_Y0=(HH-1350)//2
def draw_hd(frame,c):
    if c is None: return frame
    p=dict(cx=239*K,base=(577+c['dy'])*K,anchor_y=(595+c['dy'])*K,size=C.P['size']*K,stroke=C.P['stroke']*K,**STYLE)
    aF,aB,aS=C.render(c['words'],c['active'],p,c['scale'],HH,HW)
    aF,aB,aS=ndi.gaussian_filter(aF,0.45*K),ndi.gaussian_filter(aB,0.45*K),ndi.gaussian_filter(aS,0.6*K)
    out=frame.astype(float)*(1-aS[...,None])+C.STROKE*aS[...,None]
    t=np.clip(aB/np.maximum(aF,1e-6),0,1)[...,None]
    out=out*(1-aF[...,None])+(WHITE*(1-t)+GOLD*t)*aF[...,None]
    return np.clip(np.round(out),0,255).astype(np.uint8)
def write_yuv(fh,im):
    Y,U,V=yuv.rgb2yuv(im); h,w=Y.shape
    fh.write(np.clip(np.round(Y),0,255).astype(np.uint8).tobytes())
    fh.write(np.clip(np.round(U.reshape(h//2,2,w//2,2).mean((1,3))),0,255).astype(np.uint8).tobytes())
    fh.write(np.clip(np.round(V.reshape(h//2,2,w//2,2).mean((1,3))),0,255).astype(np.uint8).tobytes())
def encode(raw,size,out):
    subprocess.run(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','yuv420p','-s',size,'-r','24','-i',raw,
        '-i',MP3,'-map','0:v','-map','1:a','-c:v','libx264','-preset','slow','-crf','16','-profile:v','high','-level','4.1',
        '-pix_fmt','yuv420p','-colorspace','smpte170m','-color_primaries','bt709','-color_trc','bt709','-color_range','tv',
        '-c:a','copy','-movflags','+faststart',out],check=True)
def build_hd():
    frames=plan(); base=OUT.replace('_v3.mp4','').replace('.mp4','')
    r916=open(HERE+'/hd916.yuv','wb'); r45=open(HERE+'/hd45.yuv','wb')
    sharpen=ImageFilter.UnsharpMask(radius=1.6,percent=45,threshold=2)
    for j,p in enumerate(frames):
        im=Image.open(p).convert('RGB').resize((HW,HH),Image.LANCZOS).filter(sharpen)
        im=draw_hd(np.asarray(im),caption_at(j))
        write_yuv(r916,im); write_yuv(r45,im[FEED_Y0:FEED_Y0+1350])
        if j==300: Image.fromarray(im).save(HERE+'/hd_check.png')
    r916.close(); r45.close()
    encode(HERE+'/hd916.yuv','1080x1920',HERE+f'/{base}_1080x1920.mp4')
    encode(HERE+'/hd45.yuv','1080x1350',HERE+f'/{base}_1080x1350_4-5.mp4')
    os.remove(HERE+'/hd916.yuv'); os.remove(HERE+'/hd45.yuv')
    print('ok HD ->',base)
if __name__=='__main__' and len(sys.argv)>1 and sys.argv[1]=='hd': build_hd()
