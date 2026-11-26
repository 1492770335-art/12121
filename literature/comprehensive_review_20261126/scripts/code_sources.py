from collect import *

REPOS=[('A02','cwzhou/itrSurv'),('C02','menghaomiao/aitr'),('B06','xiajunwen1007/JASA-SCL-code'),('A03','cran/QTOCen'),('B01','cran/quantoptr')]
def run():
    out=[]
    for pid,repo in REPOS:
        u='https://api.github.com/repos/'+repo
        a=dict(paper_id=pid,artifact_type='code',version='',status='',source_url='https://github.com/'+repo,final_url='',license='',license_evidence='',local_path='',repo_path='',sha256='',bytes='',pages='',fetched_at=stamp(),error='')
        try:
            info=js(u);branch=info['default_branch'];head=js(u+'/commits/'+branch)['sha'];lic=info.get('license') or {};a.update(version=head,license=lic.get('spdx_id','license_unclear'),license_evidence=u+'/license')
            # Pinned archive, preserved locally, do not execute any downloaded scripts.
            url='https://codeload.github.com/'+repo+'/zip/'+head;d,f=get(url)
            if not zipfile.is_zipfile(io.BytesIO(d)):raise ValueError('not a ZIP archive')
            p=PRIVATE/pid/(repo.replace('/','_')+'_'+head[:12]+'.zip');p.parent.mkdir(exist_ok=True);p.write_bytes(d)
            a.update(status='downloaded',final_url=f,local_path=str(p),sha256=hashlib.sha256(d).hexdigest(),bytes=len(d))
            evidence=BASE/'license_evidence'/f'{pid}_code.json';evidence.parent.mkdir(exist_ok=True);evidence.write_text(json.dumps({'repository':repo,'commit':head,'license':lic,'attribution':info.get('owner',{}).get('login'),'source':a['source_url']},ensure_ascii=False,indent=2),encoding='utf-8')
        except Exception as e:a.update(status='download_failed',error=str(e))
        out.append(a);print('code',pid,a['status'],flush=True)
    csvwrite('code_manifest.csv',out)
    # Analyses may contain restricted cohort data: retain author-published link only.
    csvwrite('code_links.csv',[dict(paper_id='A02',source_url='https://github.com/cwzhou/Analyses/tree/main/Simulations',status='source_link_only',reason='README links author simulation scripts; full repository contains data folders; archive not downloaded')])
if __name__=='__main__':run()
