"""Reviewed corrections from primary sources and local author-supplied materials."""
from collect import *

DOIS={'J01':'10.1007/s10463-018-0700-y','B05':'10.1080/01621459.2016.1155993','B06':'10.1080/01621459.2026.2664228','B10':'10.3982/ecta10582','A05':'10.1214/17-aoas1057'}
DOIS.update({'E09':'10.3982/ecta13288','I05':'10.1198/016214506000001437'})
DOIS.update({'H12':'10.1111/ectj.12097','J04':'10.1017/cbo9780511802256'})
DOIS.update({'B08':'10.1111/j.1468-0262.2005.00570.x','A07':'10.1007/s10985-016-9376-x'})
def run():
    s=json.loads((PRIVATE/'state.json').read_text(encoding='utf-8')); rows=s['rows'];meta=s['meta']
    seeds={s['id']:s for s in csv.DictReader((BASE/'literature_catalog.csv').open(encoding='utf-8-sig'))}
    changes=[]
    for pid,doi in DOIS.items():
        try:
            cr=crdoi(doi);r=crrow(cr,seeds[pid]);r['discovery_source']='reviewed_primary_source_correction';r['verification_evidence']='https://api.crossref.org/works/'+doi
            # Validate overrides rather than trusting an asserted DOI.
            if pid=='A05' and 'survival' not in r['title'].lower():raise ValueError('override mismatch')
            if pid=='G01' and 'transition' not in r['title'].lower():raise ValueError('override mismatch')
            if pid=='B08' and 'quantile treatment' not in r['title'].lower():raise ValueError('override mismatch')
            old=next((x for x in rows if x['paper_id']==pid),None)
            if old:changes.append(dict(paper_id=pid,old_title=old['title'],old_doi=old.get('doi',''),new_title=r['title'],new_doi=r['doi'],evidence_url=r['verification_evidence']));rows.remove(old)
            rows.append(r);meta[pid]=dict(cr=cr,ep={});print('corrected',pid,r['title'],flush=True)
        except Exception as e:print('correction pending',pid,str(e),flush=True)
    csvwrite('bibliographic_corrections.csv',changes)
    # JMLR's journal record has no assigned article DOI; arXiv DOI is a preprint identifier.
    r=next(x for x in rows if x['paper_id']=='C02')
    r.update(doi='',journal='Journal of Machine Learning Research',year_online='2020',year_issue='2020',arxiv='2004.02772',source_url='https://jmlr.org/papers/v21/20-334.html',verification_evidence='https://jmlr.org/papers/v21/20-334.html',status='metadata_verified_journal',version='JMLR 21(183):1-28; no article DOI assigned')
    for r in rows:
        import html
        r['title']=' '.join(html.unescape(re.sub(r'<[^>]+>','',r['title'])).split())
        if r['paper_id']=='G01':
            r.update(authors='Odd O. Aalen and Søren Johansen',journal='Scandinavian Journal of Statistics',year_issue='1978',doi='',status='metadata_verified_institutional_archive',source_url='https://www.math.ku.dk/bibliotek/arkivet/preprints-fra-ims/1977/preprint_1977_-_no_6_aalen__odd__johansen__s_ren_-_an_empirical_transition_matrix_for_non-homogeneous---.pdf',version='1977 institutional preprint linked to 1978 journal article; DOI not located',verification_evidence='https://www.math.ku.dk/bibliotek/arkivet/preprints-fra-ims/1977/ ; journal bibliographic details cross-checked against core references')
        if r['paper_id']=='A03':r['arxiv']='2204.04052'
        if r['paper_id']=='B06':r['arxiv']='2507.11255'
        if r['paper_id']=='I15' and r.get('doi','').startswith('10.32614/'):
            r.update(status='unresolved_wrong_software_candidate',doi='',journal='',authors='',title=seeds['I15']['title_or_search_phrase'],source_url=seeds['I15']['source_url'],verification_evidence='CRAN software candidate rejected; primary eScholarship record still to verify')
    # Compare original literature directories without modifying them.
    existing=[]
    for name in ['01_Qian_Murphy_2011.md','02_Zhou_2023_and_Wang_2018.md','03_Luedtke_Chambaz_2020.md','04_Near_Optimal_AITR.md','05_pending_originals.md','README.md']:
        url='https://raw.githubusercontent.com/1492770335-art/12121/main/literature/decision_theory_review_20261126/'+name
        try:
            data,_=get(url);text=data.decode('utf-8')
            for d in re.findall(r'10\.\d{4,9}/[a-zA-Z0-9._;()/:-]+',text):existing.append(dict(path='literature/decision_theory_review_20261126/'+name,doi=d.rstrip('.,;)').lower()))
        except Exception as e:print('prior source read failed',name,str(e),flush=True)
    for folder in ['quantile_treatment_rules','decision_theory_review_20261126']:
        root=BASE.parent/folder
        for p in root.rglob('*.md'):
            text=p.read_text(encoding='utf-8',errors='replace')
            for d in re.findall(r'10\.\d{4,9}/[a-zA-Z0-9._;()/:-]+',text):
                d=d.rstrip('.,;)').lower(); existing.append(dict(path=p.relative_to(BASE.parent.parent).as_posix(),doi=d))
    csvwrite('existing_literature_crosswalk.csv',existing)
    save_state(rows,meta)

if __name__=='__main__':run()
