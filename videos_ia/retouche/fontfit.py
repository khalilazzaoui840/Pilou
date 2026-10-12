import numpy as np, glob, os
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi
FD=os.environ.get('PILOU_WORK','travail')+'/fonts/'
ED=os.environ.get('PILOU_WORK','travail')+'/edit/'
def fillmask(a):
    r,g,b=[a[...,i].astype(int) for i in range(3)]
    white=(r>185)&(g>185)&(b>185)
    blue=(b>190)&(r<150)&(b-r>70)
    return white|blue
def words_from_frame(idx):
    a=np.asarray(Image.open(ED+f'full/{idx:04d}.png').convert('RGB'))[520:600]
    m=fillmask(a)
    # columns
    cols=np.where(m.any(0))[0]
    # split words by gaps > 8px
    groups=[];start=cols[0];prev=cols[0]
    for c in cols[1:]:
        if c-prev>9: groups.append((start,prev)); start=c
        prev=c
    groups.append((start,prev))
    out=[]
    for x0,x1 in groups:
        sub=m[:,x0:x1+1]; ys=np.where(sub.any(1))[0]
        out.append(((x0,x1,ys[0]+520,ys[-1]+520),sub[ys[0]:ys[-1]+1]))
    return out
def render(word,font):
    im=Image.new('L',(800,200),0); d=ImageDraw.Draw(im)
    d.text((20,20),word,font=font,fill=255)
    a=np.asarray(im)>127
    ys=np.where(a.any(1))[0]; xs=np.where(a.any(0))[0]
    if len(ys)==0: return np.zeros((1,1),bool)
    return a[ys[0]:ys[-1]+1, xs[0]:xs[-1]+1]
def iou(a,b):
    h=max(a.shape[0],b.shape[0]); w=max(a.shape[1],b.shape[1])
    A=np.zeros((h,w),bool);B=np.zeros((h,w),bool)
    A[:a.shape[0],:a.shape[1]]=a; B[:b.shape[0],:b.shape[1]]=b
    return (A&B).sum()/((A|B).sum())
def loadfont(path,size,wght=None):
    f=ImageFont.truetype(path,size)
    if wght is not None:
        try:
            axes=f.get_variation_axes()
            vals=[]
            for ax in axes:
                nm=ax.get('name',b'')
                nm=nm.decode() if isinstance(nm,bytes) else nm
                vals.append(wght if 'eight' in nm or nm=='wght' else ax['default'])
            f.set_variation_by_axes(vals)
        except Exception as e: return None
    return f
if __name__=='__main__':
    samples={307:['DES','EMBOUTS'],389:['SANS','LUI'],200:['LES','BROSSES'],210:['EN','MÉTAL']}
    targets=[]
    for idx,ws in samples.items():
        got=words_from_frame(idx)
        print(idx,[g[0] for g in got])
        for (bb,m),w in zip(got,ws): targets.append((w,m,bb))
    cands=[(p,None) for p in [q for q in sorted(glob.glob(FD+'Inter*.ttf')) if any(k in q for k in ('Bold','Black','SemiBold'))]+[FD+'Poppins-Bold.ttf',FD+'Poppins-ExtraBold.ttf',FD+'Poppins-SemiBold.ttf']]
    for v in ['Montserrat.ttf','Figtree.ttf','Roboto.ttf','PlusJakarta.ttf']:
        for wg in (600,700,800,900): cands.append((FD+v,wg))
    res=[]
    for path,wg in cands:
        tot=[]
        for w,m,bb in targets:
            best=0
            H=m.shape[0]
            for size in range(18,48):
                f=loadfont(path,size,wg)
                if f is None: break
                r=render(w,f)
                # scale-normalize: resize rendered to target height via nearest compare at same size
                if abs(r.shape[0]-H)>2: continue
                best=max(best,iou(r,m))
            tot.append(best)
        res.append((np.mean(tot),os.path.basename(path),wg,[round(t,2) for t in tot]))
    for r in sorted(res,reverse=True)[:15]: print(r)
