"""Voix B : on insère les pauses prévues (texture de silence d'origine), on cale sur 25,0 s,
puis traitement identique au niveau de la vidéo A (gain, légère compression, limiteur, -13,6 LUFS)."""
import numpy as np, wave, subprocess
from words import PHRASES, EXTRA
from timeline import TOTAL
w=wave.open('vo.wav'); sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float)/32768; w.close()
room=x[int(2.36*sr):int(2.58*sr)]            # silence d'origine entre deux phrases
def roomtone(n):
    r=np.tile(room,n//len(room)+2); return r[:n]
out=[]; pos=0
for k,(a,b,ws) in enumerate(PHRASES):
    if EXTRA[k]<=0: continue
    nxt=PHRASES[k+1][0] if k+1<len(PHRASES) else len(x)/sr
    cut=int(round((b+nxt)/2*sr))             # milieu de la pause existante
    out.append(x[pos:cut]); out.append(roomtone(int(round(EXTRA[k]*sr)))); pos=cut
out.append(x[pos:])
y=np.concatenate(out)
n=int(round(TOTAL*sr)); y=np.concatenate([y,roomtone(max(0,n-len(y)))])[:n]
yi=(np.clip(y,-1,1)*32767).astype(np.int16)
w=wave.open('voB_timed_raw.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(yi.tobytes()); w.close()
chain="volume=18dB,acompressor=threshold=-20dB:ratio=2:attack=5:release=90:makeup=1,volume=4.2dB,alimiter=limit=0.89:attack=3:release=60:level=0"  # = -16,6 LUFS mono, comme A
subprocess.run(['ffmpeg','-v','error','-y','-i','voB_timed_raw.wav','-af',chain,'-ar','44100','voB_proc.wav'],check=True)
print('durée', len(yi)/sr)
