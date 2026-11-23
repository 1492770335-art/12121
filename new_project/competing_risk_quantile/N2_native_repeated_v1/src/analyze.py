#!/usr/bin/env python3
"""Pair native estimator errors on exactly the same Oracle patient-treatment-p records."""
from __future__ import annotations
from pathlib import Path
import argparse, json
import numpy as np
import pandas as pd

MECHS=('aligned','cause_tradeoff','time_varying')
METH=('PengFine','CRRSF','SurvivalBoost')
CENS=(20,45)
PGRID={'q1':(.06,.12,.18,.24),'qall':(.15,.25,.35,.45)}
KEY=['mechanism','replicate','censor_target','endpoint','p','patient_id','a']


def oracle_rows(data:Path)->pd.DataFrame:
    out=[]
    for mech in MECHS:
        for rep in range(4):
            tr=pd.read_csv(data/f'{mech}_r{rep:02d}_oracle_test.csv')
            for censor in CENS:
                for end,ps in PGRID.items():
                    for p in ps:
                        true=tr[f'true_{end}_p{p:.2f}'].to_numpy(dtype=float)
                        out.append(pd.DataFrame(dict(mechanism=mech,replicate=rep,
                          censor_target=censor,endpoint=end,p=p,
                          patient_id=tr.patient_id.to_numpy(int),a=tr.a.to_numpy(int),true_q=true)))
    df=pd.concat(out,ignore_index=True)
    if df.duplicated(KEY).any():raise ValueError('duplicate Oracle keys')
    return df


def read_prediction(path:Path, method:str, master:pd.DataFrame)->pd.DataFrame:
    frame=master[KEY].copy()
    if not path.exists():
        frame[f'pred_{method}']=np.nan
        return frame
    pred=pd.read_csv(path)
    pred=pred.loc[pred['method']==method]
    if pred.duplicated(KEY).any():raise ValueError(f'duplicate rows {method}')
    if (pred['method']!=method).any():raise ValueError(f'wrong method {method}')
    if not pred.empty:
        compare=pred.merge(master,on=KEY,how='left',suffixes=('_prediction','_oracle'),validate='one_to_one')
        if compare['true_q_oracle'].isna().all():pass
        delta=(compare.true_q_prediction-compare.true_q_oracle).abs()
        if (delta.fillna(0)>1e-4).any():raise ValueError(f'true quantile mismatch for {method}')
        if (pred['pred_q'].notna() & ((pred['pred_q'] < 0) | (pred['pred_q'] >= 3))).any():
            raise ValueError(f'out-of-window quantile for {method}')
    frame=frame.merge(pred[KEY+['pred_q']].rename(columns={'pred_q':f'pred_{method}'}),on=KEY,how='left',validate='one_to_one')
    return frame


def detail(master:pd.DataFrame,others:list[pd.DataFrame])->pd.DataFrame:
    df=master.copy()
    for f in others:df=df.merge(f,on=KEY,how='left',validate='one_to_one')
    df['true_reach']=df.true_q.notna()
    for method in METH:df[f'reach_{method}']=df[f'pred_{method}'].notna()
    df['common_scorable']=df['true_reach']
    for method in METH:df['common_scorable']&=df[f'reach_{method}']
    for method in METH:
        df[f'ae_{method}']=(df[f'pred_{method}']-df['true_q']).abs()
    return df


def aggregates(data:pd.DataFrame):
    keys=['mechanism','replicate','censor_target','endpoint','p']
    summary=[];pair=[]
    for key,frame in data.groupby(keys,sort=True):
        count=int(frame['true_reach'].sum())
        common=frame[frame['common_scorable']]
        for m in METH:
            valid=frame[frame['true_reach'] & frame[f'reach_{m}']]
            summary.append(dict(zip(keys,key),method=m,n_total=len(frame),n_true_reachable=count,
              n_pred_reachable=int(frame[f'reach_{m}'].sum()),
              n_scorable=len(valid),
              n_common=len(common),
              n_false_finite=int((~frame['true_reach'] & frame[f'reach_{m}']).sum()),
              n_missed_true=int((frame['true_reach'] & ~frame[f'reach_{m}']).sum()),
              mae_self=float(valid[f'ae_{m}'].mean()) if len(valid) else np.nan,
              mae_common=float(common[f'ae_{m}'].mean()) if len(common) else np.nan))
        for a,b in [('PengFine','CRRSF'),('PengFine','SurvivalBoost'),('CRRSF','SurvivalBoost')]:
            pair.append(dict(zip(keys,key),method_a=a,method_b=b,n_common=len(common),
                 delta_mae_common=float((common[f'ae_{a}']-common[f'ae_{b}']).mean()) if len(common) else np.nan))
    return pd.DataFrame(summary),pd.DataFrame(pair)


def treatment_ranking(data:pd.DataFrame)->pd.DataFrame:
    groupkeys=['mechanism','replicate','censor_target','endpoint','p']
    result=[]
    for key,frame in data.groupby(groupkeys,sort=True):
        pivot=frame.pivot(index='patient_id',columns='a',values=['true_q']+[f'pred_{m}' for m in METH])
        truediff=pivot[('true_q',1)]-pivot[('true_q',0)]
        truevalid=np.isfinite(truediff) & (np.abs(truediff)>1e-8)
        for m in METH:
            dm=pivot[(f'pred_{m}',1)]-pivot[(f'pred_{m}',0)]
            valid=truevalid & np.isfinite(dm)
            result.append(dict(zip(groupkeys,key),method=m,
                n_true_ordered=int(truevalid.sum()),n_pred_ordered=int(valid.sum()),
                n_misrank=int((valid & (np.sign(dm)!=np.sign(truediff))).sum()),
                mae_treatment_delta=float(np.mean(np.abs(dm[valid]-truediff[valid]))) if valid.any() else np.nan))
    return pd.DataFrame(result)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--data',type=Path,required=True)
    p.add_argument('--r-pred',type=Path,required=True)
    p.add_argument('--py-pred',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
    master=oracle_rows(a.data)
    frames=[read_prediction(a.r_pred,'PengFine',master),read_prediction(a.r_pred,'CRRSF',master),
            read_prediction(a.py_pred,'SurvivalBoost',master)]
    data=detail(master,frames)
    summ,pair=aggregates(data)
    rank=treatment_ranking(data)
    data.to_csv(a.output/'all_patient_predictions.csv.gz',index=False,compression='gzip',float_format='%.9f')
    summ.to_csv(a.output/'replicate_level_mae.csv',index=False,float_format='%.9f')
    pair.to_csv(a.output/'replicate_level_pairwise.csv',index=False,float_format='%.9f')
    rank.to_csv(a.output/'replicate_level_ranking.csv',index=False,float_format='%.9f')
    # Paired differences use independent repeated TRAINING datasets as units.
    groupkeys=['mechanism','censor_target','endpoint','p','method_a','method_b']
    rows=[]
    for key,fr in pair.groupby(groupkeys,sort=True):
        d=fr['delta_mae_common'].dropna().to_numpy(float)
        rows.append(dict(zip(groupkeys,key),reps_with_score=len(d),
           mean_delta_mae_common=float(d.mean()) if len(d) else np.nan,
           mcse=float(d.std(ddof=1)/np.sqrt(len(d))) if len(d)>1 else np.nan,
           min_common_n=int(fr.n_common.min()),mean_common_n=float(fr.n_common.mean())))
    paired=pd.DataFrame(rows)
    paired.to_csv(a.output/'paired_mc_summary.csv',index=False,float_format='%.9f')
    quality={'n_oracle_records':len(master),'n_all_method_common_scorable':int(data.common_scorable.sum()),
          'n_oracle_true_reachable':int(data.true_reach.sum()),
          'number_repetitions_per_grid':4,
          'note':'4 training repetitions only; no statistical superiority claim; patient-level unit for MAE, training-repetition unit for MCSE'}
    for m in METH:
        quality[m]={'n_finite_predictions':int(data[f'reach_{m}'].sum()),
                    'n_missed':int((data.true_reach & ~data[f'reach_{m}']).sum()),
                    'n_false_finite':int((~data.true_reach & data[f'reach_{m}']).sum()),
                    'n_predicted_zero':int((data[f'pred_{m}']==0).sum())}
    (a.output/'quality.json').write_text(json.dumps(quality,indent=2,ensure_ascii=False)+'\n')
    # Fully automated short report; data numbers from executed estimator outputs only.
    lines=['# N2-R1 原生估计器多重复试验：自动汇总报告','',
       '**性质：**独立新课题，主要比较 Q1 与 Qall 的分位数估计；本轮 4 次训练重复为方法验证，不支持临床优效/最终模型选择。','',
       f'- Oracle 逐患者—治疗—p 记录：{len(master)}。',
       f'- 真实严格内点记录：{int(data.true_reach.sum())}；三方法共同可评分：{int(data.common_scorable.sum())}。','',
       '|方法|有限预测数|真实可达漏报|真实不可达误报|预测时间恰为0|','|---|---:|---:|---:|---:|']
    for m in METH:
        row=quality[m]
        lines.append(f'|{m}|{row["n_finite_predictions"]}|{row["n_missed"]}|{row["n_false_finite"]}|{row["n_predicted_zero"]}|')
    lines.extend(['','具体数值详见 replicate_level_mae.csv、replicate_level_pairwise.csv、paired_mc_summary.csv、replicate_level_ranking.csv。',
                  '','**限制**：只有 4 个重复；原生算法函数类和超参不同；仅能在共同可评分人群上严格配对，必须同时报告各方法的可达率与漏报。',
                  '','此文由 analyze.py 从实际预测表生成，不是预先猜测的赢家报告。'])
    (a.output/'REPORT.md').write_text('\n'.join(lines)+'\n')
    print('PASS analysis: oracle',len(master),'common',int(data.common_scorable.sum()),flush=True)

if __name__=='__main__':main()