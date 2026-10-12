"""« en métal » -> « sans embouts », version 3.
Dans l'original, « les brosses‿en » se prononce déjà /bʁɔ.sɑ̃/ : c'est le son de « brosses sans ».
On garde donc l'original intact jusqu'à la fin de ce /ɑ̃/ (en allongeant juste le /s/),
puis on enchaîne sur « ‿embouts » (/zɑ̃bu/ pris dans « des‿embouts souples »).
Une seule jonction voisée, faite sur les impulsions glottiques, à hauteur égale (~123 Hz / ~110 Hz).
Aucune retouche de hauteur ni de durée sur les voyelles."""
import numpy as np, wave, sys, os
import parselmouth
from parselmouth.praat import call
ED=os.environ.get('PILOU_WORK','travail')+'/edit/'
P=dict(s_ins_at=8.445, s_ins_from=8.418, s_ins_len=0.055, vowel_cut=8.5411, z_from=12.6622, z_to=12.952,
       resume=9.046, fade_ms=40, out='audio_v3.wav')
for a in sys.argv[1:]:
    k,v=a.split('='); P[k]=v if k=='out' else float(v)
w0=wave.open(ED+'audio.wav'); sr=w0.getframerate(); raw=np.frombuffer(w0.readframes(w0.getnframes()),np.int16).reshape(-1,2).copy(); w0.close()
x=raw[:,0].astype(float)/32768
snd=parselmouth.Sound(x,sampling_frequency=sr)
def pulse(t,win=0.02):
    pp=call(snd.extract_part(t-0.06,t+0.06,preserve_times=True),"To PointProcess (periodic, cc)",75,350)
    n=call(pp,"Get number of points"); ts=np.array([call(pp,"Get time from index",i) for i in range(1,n+1)])
    k=np.argmin(abs(ts-t)); return ts[k], (ts[k+1]-ts[k]) if k+1<len(ts) else 0.008
def I(t): return int(round(t*sr))
# 1) /s/ de « brosses » allongé (bruit dans du bruit : inaudible)
a=I(P['s_ins_at']); L=I(P['s_ins_len']); b0=I(P['s_ins_from'])
ins=x[b0:b0+L].copy(); nx=I(0.008); t=np.linspace(0,1,nx)
# 2) jonction /ɑ̃/ (« en » original) -> /z/ de « des‿embouts », alignée sur les impulsions
tv,pv=pulse(P['vowel_cut']); tz,pz=pulse(P['z_from'])
iv=I(tv); iz=I(tz); nov=I(min(pv,pz))
print(f"coupe voyelle {tv:.4f}s (période {pv*1000:.1f} ms) -> /z/ {tz:.4f}s (période {pz*1000:.1f} ms)")
head=x[a:iv+nov].copy()                       # suite de l'original : fin du /s/ + /ɑ̃/ + 1 période
Z=x[iz:I(P['z_to'])].copy()
nf=I(P['fade_ms']/1000); Z[-nf:]*=np.cos(np.linspace(0,np.pi/2,nf))**1.5
to=np.linspace(0,1,nov)
mid=np.concatenate([head[:-nov], head[-nov:]*np.cos(to*np.pi/2)**2 + Z[:nov]*np.sin(to*np.pi/2)**2, Z[nov:]])
# assemblage : x[:a] + ins + mid  (fondus à puissance constante dans le /s/)
seq=np.concatenate([x[a-nx:a]*np.cos(t*np.pi/2)+ins[:nx]*np.sin(t*np.pi/2), ins[nx:-nx],
                    ins[-nx:]*np.cos(t*np.pi/2)+mid[:nx]*np.sin(t*np.pi/2), mid[nx:]])
start=a-nx
i_res=I(P['resume']); gap=i_res-(start+len(seq)); assert gap>0, gap
i_tail=I(9.012); tail=x[i_tail:i_res]
room=x[I(7.990):I(8.080)]; n_room=gap-len(tail)
room=np.tile(room,n_room//len(room)+2)[:n_room+I(0.006)]
n6=I(0.006); t6=np.linspace(0,1,n6)
fill=np.concatenate([room[:-n6],room[-n6:]*(1-t6)+tail[:n6]*t6,tail[n6:]])
n2=I(0.004); fill[:n2]*=np.linspace(0,1,n2)
R=np.concatenate([seq,fill]); assert len(R)==i_res-start
segi=np.round(np.clip(R,-1,1)*32768).clip(-32768,32767).astype(np.int16)
raw[start:i_res,0]=segi; raw[start:i_res,1]=segi
w=wave.open(ED+P['out'],'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes(raw.tobytes()); w.close()
off=len(ins)-nx
print(f"« san » (original) : {(a+off-nx)/sr:.3f} ; /z/ : {(start+nx+len(ins)-2*nx+len(head)-nov)/sr:.3f} ; fin « embouts » {(start+len(seq))/sr:.3f} ; pause {gap/sr*1000:.0f} ms")
