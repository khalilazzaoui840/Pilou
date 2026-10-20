"""Montage d'une vidéo Pilou (25 s) : voix ElevenLabs + plans nettoyés de la vidéo A + sous-titres blanc/doré.
À lancer depuis le dossier de la version (A/ ou B/) qui contient words.py."""
import numpy as np, sys, os, subprocess, shutil, wave, json
from PIL import Image
from scipy import ndimage as ndi
HERE=os.getcwd(); sys.path.insert(0,HERE)
SCR=__import__('os').environ.get('PILOU_WORK','travail')+'/'
sys.path.insert(0,SCR+'tools')
import caption as C, yuv
from words import VO, PHRASES, GROUPS, EXTRA, SHOTS, CUTMARKS, OUT
VB=SCR+'videoB/'                 # images de la vidéo A : A_full (brutes), A_clean (sous-titres effacés)
SRC=VB+'A_clean/'
TOTAL=25.0; FPS=24
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
        n_out=int(round(c1*FPS))-int(round(c0*FPS)); have=b-a+1; extra=n_out-have
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
        frames+=seq
        print(f'{name}: {c0:5.2f}-{c1:5.2f} s, {n_out} images' + (f', {extra} ajoutées' if extra>0 else f', {-extra} coupées' if extra<0 else ''))
    assert len(frames)==int(round(TOTAL*FPS))
    return frames
def build():
    build_audio()
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
        '-i',HERE+'/vo_proc.wav','-map','0:v','-map','1:a','-c:v','libx264','-preset','slow','-crf','14','-profile:v','high',
        '-pix_fmt','yuv420p','-colorspace','smpte170m','-color_primaries','bt709','-color_trc','bt709','-color_range','tv',
        '-c:a','aac','-b:a','192k','-ar','44100','-ac','2','-movflags','+faststart','-t',str(TOTAL),HERE+'/'+OUT],check=True)
    os.remove(HERE+'/v.yuv')
    json.dump([dict(words=e['words'],start=round(e['start'],2),end=round(e['end'],2)) for e in EV],open(HERE+'/captions.json','w'),ensure_ascii=False,indent=0)
    print('ok ->',OUT)
if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='plan':
        print('coupes',[round(c,2) for c in CUTS]); print('fin voix',round(P2[-1][1],2))
        for (n,a,b),c0,c1 in zip(SHOTS,CUTS[:-1],CUTS[1:]): print(f'{n}: besoin {(c1-c0)*FPS:5.1f} images, dispo {b-a+1}, vitesse {(b-a+1)/((c1-c0)*FPS):.2f}x')
        for e in EV: print(f"  {e['start']:6.2f}-{e['end']:6.2f} {' '.join(e['words'])}")
    else: build()
