import numpy as np, wave, sys
from PIL import Image, ImageDraw
def load(p):
    w=wave.open(p); sr=w.getframerate(); n=w.getnframes(); ch=w.getnchannels()
    x=np.frombuffer(w.readframes(n),dtype=np.int16).reshape(-1,ch).astype(float).mean(1)/32768
    return x,sr
def spec(path,t0,t1,out,pxs=1000,fmax=11000):
    x,sr=load(path)
    hop=int(sr/pxs*1) ; win=1024
    a=int(t0*sr); b=int(t1*sr)
    cols=[]
    for i in range(a,b,hop):
        seg=x[i-win//2:i+win//2]
        if len(seg)<win: seg=np.pad(seg,(0,win-len(seg)))
        cols.append(np.abs(np.fft.rfft(seg*np.hanning(win))))
    S=np.array(cols).T
    nb=int(fmax/(sr/2)*S.shape[0]); S=S[:nb][::-1]
    D=20*np.log10(S+1e-7); D=np.clip((D-D.max()+80)/80,0,1)
    H=300
    img=Image.fromarray((D*255).astype(np.uint8)).resize((S.shape[1],H))
    # waveform rms row
    img=img.convert('RGB'); W=img.size[0]
    canvas=Image.new('RGB',(W,H+120),'white'); canvas.paste(img,(0,0))
    d=ImageDraw.Draw(canvas)
    seg=x[a:b]; step=hop
    for k in range(W):
        s=seg[k*step:(k+1)*step]
        if len(s)==0: break
        r=np.sqrt((s**2).mean()); db=20*np.log10(r+1e-9)
        h=int(max(0,db+60)*1.3)
        d.line([(k,H+100),(k,H+100-h)],fill=(0,0,200))
    t=np.ceil(t0*20)/20
    while t<t1:
        xk=int((t-t0)*sr/hop)
        big=abs(t*10-round(t*10))<1e-6
        d.line([(xk,0),(xk,H+100)],fill=(255,0,0) if big else (255,180,180))
        if big: d.text((xk+2,H+102),f'{t:.1f}',fill=(0,0,0))
        t+=0.05
    canvas.save(out)
if __name__=='__main__':
    spec(sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),sys.argv[4],int(sys.argv[5]) if len(sys.argv)>5 else 1000)
