"""Paired V8 native-method smoke: latest 2026-11-24 M1/M2 hazards frozen."""
import numpy as np
import csv,hashlib,json,sys
from pathlib import Path
L=3.; R=int(sys.argv[1]) if len(sys.argv)>1 else 2
NTRAIN=700; NTEST=2000; out=Path(__file__).parent/'data';out.mkdir(exist_ok=True)
def hazards(z,m):
 z1,z2=z.T; b1=.18*np.exp(.15*z1+.15*z2);b2=.15*np.exp(-.10*z1+.20*z2)
 h=np.zeros((len(z),2,2,2))
 h[:,0,0,:]=b1[:,None];h[:,0,1,:]=b2[:,None]
 if m=='M1':
  h[:,0,0,0]*=2;h[:,0,0,1]*=.5;h[:,0,1,0]*=.5;h[:,0,1,1]*=2
  h[:,1,0,:]=h[:,0,0,:]*np.exp(np.log(.6)+.65*z1)[:,None]
  h[:,1,1,:]=h[:,0,1,:]*np.exp(np.log(2)+.25*(2*z2-1))[:,None]
 elif m=='M2':
  h[:,1,0,0]=b1*np.exp(np.log(.5)+.35*z1)
  h[:,1,0,1]=b1*np.exp(np.log(2.5)+.35*z1)
  h[:,1,1,:]=b2[:,None]*np.exp(np.log(.7)+.25*(2*z2-1))[:,None]
 return h
def make_sample(rng,m,n):
 z=np.column_stack([rng.uniform(-1,1,n),rng.binomial(1,.5,n)])
 a=rng.binomial(1,.5,n)
 rate=hazards(z,m)[np.arange(n),a];total=rate.sum(axis=1);E=rng.exponential(1,n)
 early=E<=total[:,0]
 t=np.where(early,E/total[:,0],1+(E-total[:,0])/total[:,1])
 seg=np.where(early,0,1);p1=rate[np.arange(n),0,seg]/total[np.arange(n),seg]
 j=np.where(rng.random(n)<p1,1,2)
 C=rng.exponential(1/.08,n); x=np.minimum(t,C);status=np.where(t<=C,j,0)
 return z,a,x,status
streams=np.random.SeedSequence(42).spawn(20)
manifest=[]
for rep in range(R):
 rngtest=np.random.default_rng(streams[rep]);Z=np.column_stack([rngtest.uniform(-1,1,NTEST),rngtest.binomial(1,.5,NTEST)])
 coin=rngtest.binomial(1,.5,NTEST)
 for mi,m in enumerate(('M1','M2')):
  rng=np.random.default_rng(np.random.SeedSequence([2026112407,rep,mi]))
  z,a,x,status=make_sample(rng,m,NTRAIN)
  tr=np.column_stack([z,a,x,status,(status>0).astype(int),(status==1).astype(int),(status==2).astype(int),np.full(NTRAIN,.5)])
  te=np.column_stack([np.arange(NTEST),Z,coin])
  p=out/f'train_{m}_r{rep+1}.csv'; q=out/f'test_{m}_r{rep+1}.csv'
  np.savetxt(p,tr,delimiter=',',header='Z1,Z2,Trt,obs_time,status,D.0,D.1,D.2,piz',comments='',fmt='%.17g')
  np.savetxt(q,te,delimiter=',',header='id,Z1,Z2,tie_coin',comments='',fmt='%.17g')
  manifest.append(dict(mechanism=m,rep=rep+1,train_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),test_sha256=hashlib.sha256(q.read_bytes()).hexdigest(),censor_pct=100*np.mean(status==0)))
(out/'manifest.json').write_text(json.dumps(dict(n_train=NTRAIN,n_test=NTEST,R=R,train_seed=2026112407,test_seed=42,censor_rate=.08,results=manifest),indent=2),encoding='utf-8')
print(json.dumps(manifest,indent=2))