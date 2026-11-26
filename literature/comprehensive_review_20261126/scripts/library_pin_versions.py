from library_audit import *
def run():
    rows=read('fulltext_library/license_audit.csv');checks=[]
    for a in rows:
        if a['decision']!='public_allowed' or not a['arxiv_id'] or re.search(r'v\d+$',a['arxiv_id']):continue
        row=dict(paper_id=a['paper_id'],arxiv_id=a['arxiv_id'],original_sha256=a['sha256'],status='',version='',error='')
        try:
            s=(WORK/(a['sha256']+'.arxiv.html')).read_text(encoding='utf-8')
            versions=re.findall(r'(?:\[v|/abs/'+re.escape(a['arxiv_id'])+r'v)(\d+)',s)
            if not versions:raise ValueError('version history not parsed')
            version=a['arxiv_id']+'v'+str(max(map(int,versions)));d,f=get('https://arxiv.org/pdf/'+version)
            if hashlib.sha256(d).hexdigest()!=a['sha256']:raise ValueError('version-specific PDF bytes do not match saved PDF')
            # Recheck that pinned version's actual license is the same.
            raw,_=get('https://arxiv.org/abs/'+version);t=raw.decode('utf-8','replace');m=re.search(r'<div class="abs-license">(.*?)</div>',t,re.S)
            if not m or cc_url(m[1]).replace('https:','http:')!=a['license_url'].replace('https:','http:'):raise ValueError('version-specific license differs')
            a.update(arxiv_id=version,license_evidence_url='https://arxiv.org/abs/'+version,reason='arxiv_pinned_version_hash_and_license_matched')
            (WORK/(a['sha256']+'.arxiv.html')).write_text(t,encoding='utf-8');row.update(status='matched',version=version)
        except Exception as e:
            a.update(decision='local_only',reason='version_specific_license_not_confirmed:'+str(e));row.update(status='withheld',error=str(e))
        checks.append(row);print('pin',row,flush=True)
    csvwrite('fulltext_library/license_audit.csv',rows);csvwrite('fulltext_library/version_pin_checks.csv',checks)
if __name__=='__main__':run()
