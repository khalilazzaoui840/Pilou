"""Remplace « en métal » par « sans embouts » dans la voix off, avec la propre voix du narrateur.

Sources (même enregistrement) :
  « sans »            <- « SANS lui faire mal »  (/s/ + /ɑ̃/)
  « ‿embouts » (/zɑ̃bu/) <- « des‿EMBOUTS souples » (liaison /z/ comprise)
L'intonation (PSOLA, Praat) reprend celle de « en métal » : descente puis montée finale.
"""
import os
import numpy as np, parselmouth, wave, sys
from parselmouth.praat import call
ED=os.environ.get('PILOU_WORK','travail')+'/edit/'
snd=parselmouth.Sound(ED+'audio.wav').convert_to_mono()
sr=int(snd.sampling_frequency); x=snd.values[0].copy()
P=dict(cut_in=8.450, s_from=16.090, s_to=16.250, z_from=12.660, z_end=12.697, u_from=12.862, z_to=12.952,
       resume=9.045, z_stretch=1.5, u_stretch=2.05, u_gain_db=3.0, xf_ms=3.0)
for a in sys.argv[1:]:
    k,v=a.split('='); P[k]=float(v)
def zc(t,search=0.003):
    i=int(round(t*sr)); w=int(search*sr)
    seg=x[i-w:i+w]; z=np.where(np.diff(np.signbit(seg)))[0]
    return (i-w+z[np.argmin(abs(z-w))]+1) if len(z) else i
def psola(sig,pitch_pts,dur_pts=()):
    s=parselmouth.Sound(sig,sampling_frequency=sr); L=s.duration
    man=call(s,"To Manipulation",0.005,75,350)
    pt=call("Create PitchTier","pt",0,L)
    for t,f in pitch_pts: call(pt,"Add point",t,f)
    call([pt,man],"Replace pitch tier")
    if dur_pts:
        dt=call("Create DurationTier","dt",0,L)
        for t,r in dur_pts: call(dt,"Add point",t,r)
        call([dt,man],"Replace duration tier")
    return call(man,"Get resynthesis (overlap-add)").values[0]
MODE=P.get('mode',1.0)
i0,i1=zc(P['s_from']),zc(P['s_to'])
j0,jz,ju,j1=zc(P['z_from']),zc(P['z_end']),zc(P['u_from']),zc(P['z_to'])
segZ=x[j0:j1].copy()
nu=ju-j0; g=10**(P['u_gain_db']/20); r=int(0.01*sr)
segZ[nu:]*=g; segZ[nu-r:nu]*=np.linspace(1,g,r)
nz=jz-j0; gz=10**(P.get('z_gain_db',0)/20); rz=int(0.004*sr)
segZ[:nz]*=gz; segZ[nz:nz+rz]*=np.linspace(gz,1,rz)
xf=int(P['xf_ms']/1000*sr); t=np.linspace(0,1,xf)
S=x[i0:i1]
raw=np.concatenate([S[:-xf],S[-xf:]*(1-t)+segZ[:xf]*t,segZ[xf:]])
off=(len(S)-xf)/sr; t0=i0/sr; s0=j0/sr
tz=off+jz/sr-s0; tu=off+ju/sr-s0; te=off+j1/sr-s0; e=0.002
pts=[(16.186-t0,138),(16.215-t0,131),(off-0.004,125),(off+0.004,120),(tz,121),(off+12.720-s0,124),(off+12.780-s0,119),(off+12.825-s0,115),(tu+0.004,146),(tu+0.6*(te-tu),178),(te-0.006,165)]
durs=[(off-e,1.0),(off+e,P['z_stretch']),(tz-e,P['z_stretch']),(tz+e,1.0),(tu-e,1.0),(tu+e,P['u_stretch']),(te-e,P['u_stretch']),(te,1.0)]
new=raw if MODE==0 else psola(raw,pts,durs)
p1=S
nf=int(0.055*sr); new[-nf:]*=np.exp(-np.linspace(0,4.2,nf))*np.cos(np.linspace(0,np.pi/2,nf))**0.5
# --- insertion dans la piste d'origine
i_in=zc(P['cut_in']); i_res=zc(P['resume'])
gap=i_res-(i_in+len(new))
print(f'segment {len(new)/sr:.3f}s : {i_in/sr:.3f} -> {(i_in+len(new))/sr:.3f}, reprise « ça » {i_res/sr:.3f}, blanc {gap/sr*1000:.0f} ms')
assert gap>0
room=x[i_res-gap:i_res].copy()   # texture d'origine juste avant « ça »
R=np.concatenate([new,room])
n1=int(0.012*sr); t=np.linspace(0,1,n1)
R[:n1]=x[i_in:i_in+n1]*np.cos(t*np.pi/2)+R[:n1]*np.sin(t*np.pi/2)   # /s/ -> /s/
n2=int(0.004*sr); t=np.linspace(0,1,n2)
R[-n2:]=R[-n2:]*(1-t)+x[i_res-n2:i_res]*t
k=len(new); R[k:k+n2]*=t
out=x.copy(); out[i_in:i_res]=R
print('peak',np.abs(out).max(),'z debut',(i_in+len(p1)-xf)/sr)
w0=wave.open(ED+'audio.wav'); orig=np.frombuffer(w0.readframes(w0.getnframes()),np.int16).reshape(-1,2).copy(); w0.close()
seg=np.round(np.clip(out[i_in:i_res],-1,1)*32768).clip(-32768,32767).astype(np.int16)
orig[i_in:i_res,0]=seg; orig[i_in:i_res,1]=seg      # seule la zone « en métal » est réécrite
y=None
w=wave.open(ED+'audio_new.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
w.writeframes(orig.tobytes()); w.close()
