#!/usr/bin/env python3
"""Native hazardous SurvivalBoost, never substitute a self-written estimator."""
from pathlib import Path
import argparse,importlib.metadata,json,traceback,time
import numpy as np
import pandas as pd
from score_helpers import summarize

def main():
    pa=argparse.ArgumentParser()
    pa.add_argument('--data',type=Path,required=True)
    pa.add_argument('--output',type=Path,required=True)
    args=pa.parse_args();args.output.mkdir(parents=True,exist_ok=True)
    from hazardous import SurvivalBoost
    print('hazardous',importlib.metadata.version('hazardous'))
    res=[];fails=[];timegrid=np.linspace(0,3,301)
    for mech in ('aligned','cause_tradeoff','time_varying'):
        truth=pd.read_csv(args.data/f'{mech}_oracle_test.csv')
        Xtest=truth[['a','z1','z2','az1']]
        for censor in (20,45):
            train=pd.read_csv(args.data/f'{mech}_c{censor}_train.csv')
            X=train[['a','z1','z2','az1']]
            y={'event':train['fstatus'].to_numpy(int),'duration':train['ftime'].to_numpy(float)}
            start=time.monotonic()
            try:
                model=SurvivalBoost(n_iter=40,learning_rate=0.05,max_leaf_nodes=7,
                                    min_samples_leaf=20,show_progressbar=False,
                                    ipcw_strategy='kaplan-meier',random_state=20261123)
                model.fit(X,y)
                all_pred=model.predict_cumulative_incidence(Xtest,times=timegrid)
                if all_pred.shape!=(len(truth),3,len(timegrid)):
                    raise RuntimeError(f'unexpected probability dimensions {all_pred.shape}')
                maxsum=float(np.max(abs(np.sum(all_pred,axis=1)-1)))
                if maxsum>2e-3:raise ValueError(f'probability non-normalization {maxsum}')
                if np.max(all_pred)>1.001 or np.min(all_pred)<-.001:
                    raise ValueError('CIF outside probability range')
                scored=summarize('SurvivalBoost-native',mech,censor,truth,all_pred[:,1,:],timegrid,
                                 run_note=f'version={importlib.metadata.version("hazardous")}; n_iter=40')
                res.append(scored)
                print(mech,censor,'PASS sec=',round(time.monotonic()-start,2), 'mae=',scored.mae.round(3).tolist(), 'n_score=',scored.n_both.tolist(),flush=True)
            except Exception as e:
                fails.append({'method':'SurvivalBoost-native','mechanism':mech,'censor_target':censor,
                              'error':str(e),'traceback':traceback.format_exc()})
                print(mech,censor,'FAIL',str(e),flush=True)
    if res: pd.concat(res,ignore_index=True).to_csv(args.output/'survivalboost_metrics.csv',index=False)
    (args.output/'survivalboost_failures.json').write_text(json.dumps(fails,indent=2))
    (args.output/'survivalboost_versions.json').write_text(json.dumps({x:importlib.metadata.version(x) for x in ['numpy','pandas','scipy','scikit-learn','hazardous']},indent=2))
    if not res:raise SystemExit('No successful SurvivalBoost fits')

if __name__=='__main__':main()
