"""Assemble la vidéo : frames d'origine (YUV exact) + frames retouchées, audio modifié."""
import sys, os, numpy as np, subprocess, glob
sys.path.insert(0,os.path.dirname(__file__))
import yuv
from PIL import Image
from scipy import ndimage as ndi
ED=os.environ.get('PILOU_WORK','travail')+'/edit/'
def build(out_path, patch_dirs, audio, crf=12):
    fr=yuv.read_frames(ED+'orig.yuv').copy()
    n_patched=0
    for d in patch_dirs:
        for f in sorted(glob.glob(d+'/*.png')):
            i=int(os.path.basename(f)[:4])-1      # nom 1-based comme full/
            new=np.asarray(Image.open(f).convert('RGB'))
            old=np.asarray(Image.open(ED+f'full/{i+1:04d}.png').convert('RGB'))
            diff=np.abs(new.astype(int)-old).max(2)>0
            if not diff.any(): continue
            m=ndi.binary_dilation(diff,iterations=2).astype(float)
            fr[i]=yuv.patch(fr[i],new,m); n_patched+=1
    raw=ED+'build.yuv'; fr.tofile(raw)
    cmd=['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','yuv420p','-s','480x854','-r','24','-i',raw,
         '-i',audio,'-map','0:v','-map','1:a','-c:v','libx264','-preset','slow','-crf',str(crf),'-profile:v','high',
         '-pix_fmt','yuv420p','-colorspace','smpte170m','-color_primaries','bt709','-color_trc','bt709','-color_range','tv',
         '-c:a','aac','-b:a','192k','-ar','44100','-movflags','+faststart','-shortest',out_path]
    subprocess.run(cmd,check=True); os.remove(raw)
    print('frames retouchées:',n_patched,'->',out_path)
if __name__=='__main__':
    build(sys.argv[1], sys.argv[3:], sys.argv[2])
