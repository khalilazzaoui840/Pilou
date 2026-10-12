"""« en métal » -> « sans embouts », version 2 : collage SANS aucune retouche de hauteur ni de durée.
Sources (même prise) : « SANS lui faire mal » (/s ɑ̃/) et « des‿EMBOUTS souples » (/z ɑ̃ b u/).
Seuls traitements : fondus de quelques ms aux jonctions (passages par zéro) et extinction naturelle du /u/."""
import numpy as np, wave, sys, os
ED=os.environ.get('PILOU_WORK','travail')+'/edit/'
P=dict(cut_in=8.450,s_from=16.090,s_to=16.250,z_from=12.660,z_to=12.952,resume=9.046,fade_ms=40,xf_ms=3,out='audio_v2.wav')
for a in sys.argv[1:]:
    k,v=a.split('='); P[k]=v if k=='out' else float(v)
w0=wave.open(ED+'audio.wav'); sr=w0.getframerate(); raw=np.frombuffer(w0.readframes(w0.getnframes()),np.int16).reshape(-1,2).copy(); w0.close()
x=raw[:,0].astype(float)/32768
def zc(t,rising=True,search=0.004):
    """passage par zéro montant le plus proche (même phase aux deux bords d'une jonction)"""
    i=int(round(t*sr)); w=int(search*sr); seg=x[i-w:i+w]
    z=np.where((seg[:-1]<0)&(seg[1:]>=0))[0] if rising else np.where(np.diff(np.signbit(seg)))[0]
    return i-w+z[np.argmin(abs(z-w))]+1 if len(z) else i
i0,i1=zc(P['s_from']),zc(P['s_to']); j0,j1=zc(P['z_from']),zc(P['z_to'])
S=x[i0:i1]; Z=x[j0:j1].copy()
nf=int(P['fade_ms']/1000*sr); Z[-nf:]*=np.cos(np.linspace(0,np.pi/2,nf))**1.5
xf=int(P['xf_ms']/1000*sr); t=np.linspace(0,1,xf)
new=np.concatenate([S[:-xf],S[-xf:]*(1-t)+Z[:xf]*t,Z[xf:]])
i_in=zc(P['cut_in']); i_res=zc(P['resume'],rising=False)
gap=i_res-(i_in+len(new)); assert gap>0
i_tail=int(round(9.012*sr))                          # fin réelle de « métal » dans l'original
tail=x[i_tail:i_res]                                 # souffle d'origine juste avant « ça »
n_room=gap-len(tail); assert n_room>0
room=x[int(7.990*sr):int(8.080*sr)]                  # silence d'origine (avant « les brosses »)
room=np.tile(room,n_room//len(room)+2)[:n_room+int(0.006*sr)]
nx=int(0.006*sr); t6=np.linspace(0,1,nx)
fill=np.concatenate([room[:-nx],room[-nx:]*(1-t6)+tail[:nx]*t6,tail[nx:]])
R=np.concatenate([new,fill]); assert len(R)==i_res-i_in
n1=int(0.012*sr); t=np.linspace(0,1,n1)
R[:n1]=x[i_in:i_in+n1]*np.cos(t*np.pi/2)+R[:n1]*np.sin(t*np.pi/2)   # /s/ -> /s/
k=len(new); n2=int(0.004*sr); R[k:k+n2]*=np.linspace(0,1,n2)
seg=np.round(np.clip(R,-1,1)*32768).clip(-32768,32767).astype(np.int16)
raw[i_in:i_res,0]=seg; raw[i_in:i_res,1]=seg
w=wave.open(ED+P['out'],'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes(raw.tobytes()); w.close()
print(f"sans : {i_in/sr:.3f}->{(i_in+len(S)-xf)/sr:.3f}  embouts : ->{(i_in+len(new))/sr:.3f}  pause {gap/sr*1000:.0f} ms  « ça » {i_res/sr:.3f}")
