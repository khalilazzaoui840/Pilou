import numpy as np, wave, sys
def load(p):
    w=wave.open(p); sr=w.getframerate(); n=w.getnframes(); ch=w.getnchannels()
    x=np.frombuffer(w.readframes(n),dtype=np.int16).reshape(-1,ch).astype(float).mean(1)/32768
    return x,sr
def feats(x,sr,t,win=0.025):
    n=int(win*sr); i=int(t*sr)
    s=x[i-n//2:i+n//2]*np.hanning(n)
    E=np.sqrt((s**2).mean()); db=20*np.log10(E+1e-9)
    F=np.abs(np.fft.rfft(s,4096))**2; f=np.fft.rfftfreq(4096,1/sr)
    hf=F[f>3500].sum()/(F[f>100].sum()+1e-12)
    cen=(F*f).sum()/(F.sum()+1e-12)
    # voicing: normalized autocorr peak in 70-400Hz lag
    s2=x[i-n:i+n]; s2=s2-s2.mean()
    ac=np.correlate(s2,s2,'full')[len(s2)-1:]; ac/= (ac[0]+1e-12)
    lo,hi=int(sr/400),int(sr/70)
    k=np.argmax(ac[lo:hi])+lo
    return db,hf,cen,ac[k],sr/k
if __name__=='__main__':
    x,sr=load(sys.argv[1]); t0=float(sys.argv[2]); t1=float(sys.argv[3]); st=float(sys.argv[4]) if len(sys.argv)>4 else 0.005
    print(' t      dB    HF   cent  voic  f0')
    t=t0
    while t<=t1+1e-9:
        db,hf,cen,v,f0=feats(x,sr,t)
        tag=('V' if v>0.6 else ' ')+('F' if hf>0.35 else ' ')+('_' if db<-35 else ' ')
        print(f'{t:6.3f} {db:6.1f} {hf:5.2f} {cen:6.0f} {v:5.2f} {f0:5.0f} {tag} '+'#'*int(max(0,db+50)/1.2))
        t+=st
