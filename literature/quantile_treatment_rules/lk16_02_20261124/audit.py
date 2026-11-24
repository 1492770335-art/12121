"""Run locally: python audit.py P-5370.zip. Requires numpy pandas scipy statsmodels scikit-learn.
Outputs aggregate summaries only. Do not commit the source dataset."""
import sys, zipfile, io, hashlib
import numpy as np
import pandas as pd
from scipy.linalg import qr
from scipy.stats import chi2
from statsmodels.duration.hazard_regression import PHReg
from sklearn.linear_model import LogisticRegression

p=sys.argv[1]
with zipfile.ZipFile(p) as z:
    d=pd.read_sas(io.BytesIO(z.read(next(n for n in z.namelist() if n.endswith('.sas7bdat')))),format='sas7bdat')
print('sha256',hashlib.sha256(open(p,'rb').read()).hexdigest(),'shape',d.shape)
d['A']=(d.strataf>=3).astype(int)
d['DRI']=d.strataf.isin([2,4]).astype(int)
v=d.dropna(subset=['intxrel','rel','trm','dfs']).copy()
assert (v.rel+v.trm==v.dfs).all() and (v.intxrel>0).all() and (v.intxrel<=v.intxsurv+1e-8).all()
v['J']=v.trm+2*v.rel
print('missing',d.isna().sum().to_dict(),'valid',len(v),'centers',v.dummyccn.nunique())
def aj(g):
    t=g.intxrel.to_numpy(); j=g.J.to_numpy(); s=1.; f=np.zeros(2); out=[]
    for u in np.unique(t):
        n=(t>=u).sum(); e=np.array([((t==u)&(j==k)).sum() for k in [1,2]])
        f+=s*e/n; s*=1-e.sum()/n; out.append((u,*f,1-s))
    return np.array(out)
def summarize(g):
    a=aj(g); vals=[]
    for t in [6,12,24,36]:
        ix=np.searchsorted(a[:,0],t,side='right')-1
        vals.extend(a[ix,1:].round(4) if ix>=0 else [0]*3)
    qs=[]
    for col,p in [(3,.5),(1,.05),(1,.1),(1,.15),(1,.2)]:
        hit=a[(a[:,col]>=p)&(a[:,0]<=36),0]
        qs.append(round(hit[0],2) if len(hit) else 'NR')
    print(len(g),g.J.value_counts().sort_index().to_dict(),'risk36',int((g.intxrel>=36).sum()),'CIFs',vals,'Q',qs)
for k,g in [('all',v),*v.groupby('A'),*v.groupby('strataf')]:
    print(k,end=' '); summarize(g)
for name,g in [('AML',v[v.disease==10]),('AML CR1/2',v[(v.disease==10)&v.amstatprgp.isin([2,3])])]:
    print(name,len(g),g.A.value_counts().to_dict(),g.DRI.value_counts().to_dict(),g.dummyccn.nunique()); summarize(g)
for c in ['agegpff','kps','hctcigpc','disease','DRI','amstatprgp','distatus']:
    print(c,pd.crosstab(v[c],v.A).to_dict())
print('centers both',int((pd.crosstab(v.dummyccn,v.A)>0).all(axis=1).sum()))
v['status']=np.where(v.disease==10,'AML_'+v.amstatprgp.astype(int).astype(str),'MDS_'+v.distatus.astype(int).astype(str))
v['hct']=v.hctcigpc.replace({4:3,5:3}); v['era']=(v.yeartx>=2013).astype(int)
cols=['agegpff','sex','kps','hct','DRI','status','wbcdxgp','donorgp_final','drsex','drcmvprf','era']
X=pd.get_dummies(v[cols].astype(str),drop_first=True,dtype=float)
_,r,ix=qr(np.column_stack([np.ones(len(X)),X]),pivoting=True,mode='economic')
rank=(np.abs(np.diag(r))>1e-8).sum(); keep=[i-1 for i in ix[:rank] if i>0]; X=X.iloc[:,keep]
assert 0 in ix[:rank]
ps=LogisticRegression(max_iter=1000).fit(X,v.A).predict_proba(X)[:,1]
print('PS quantiles',np.quantile(ps,[0,.01,.05,.5,.95,.99,1]),'outside .1-.9',np.mean((ps<.1)|(ps>.9)))
X.insert(0,'A',v.A); X['A_DRI']=v.A*v.DRI
for cause in [1,2]:
    fit=PHReg(v.intxrel,X,status=(v.J==cause).astype(int),ties='breslow').fit()
    print('cause',cause,'HR A/interaction',np.exp(fit.params[[0,-1]]),'p',fit.pvalues[[0,-1]])
    cut=6.001
    late=v.intxrel.to_numpy()>cut
    t=np.r_[np.minimum(v.intxrel,cut),v.intxrel[late]]
    entry=np.r_[np.zeros(len(v)),np.full(late.sum(),cut)]
    event=(v.J==cause).to_numpy().astype(int)
    status=np.r_[event*(~late),event[late]]
    xx=pd.concat([X,X.loc[late]],ignore_index=True)
    xx['A_late']=np.r_[np.zeros(len(v)),X.loc[late,'A']]
    xx['A_DRI_late']=np.r_[np.zeros(len(v)),X.loc[late,'A_DRI']]
    alt=PHReg(t,xx,status=status,entry=entry,ties='breslow').fit()
    lr=2*(alt.llf-fit.llf)
    print('time-varying treatment joint LRT',lr,chi2.sf(lr,2),'early/late HR low DRI',np.exp([alt.params[0],alt.params[0]+alt.params[-2]]),'high DRI',np.exp([alt.params[0]+alt.params[-3],alt.params[0]+alt.params[-3]+alt.params[-2]+alt.params[-1]]))
