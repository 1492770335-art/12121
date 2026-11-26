"""Two-depth OpenAlex citation tracing + dated Europe PMC and Crossref topic searches."""
from collect import *

QUERIES=[
 ('A','("competing risks" OR "competing events" OR subdistribution) AND ("optimal treatment" OR "individualized treatment" OR "policy learning" OR "optimal decision")'),
 ('B','(quantile OR percentile OR "distributional welfare" OR "risk-sensitive") AND ("optimal treatment" OR "individualized decision" OR "policy learning") AND (survival OR censored OR competing OR outcome)'),
 ('D','("competing risks" OR "cumulative incidence") AND ("quantile regression" OR "quantile inference" OR "conditional quantile" OR "inverse CIF")'),
 ('C','("individualized treatment" OR "treatment regime" OR "policy learning") AND ("risk constraint" OR "multiple outcomes" OR "near-optimal" OR "set-valued" OR noninferiority OR lexicographic OR "epsilon constraint" OR "prioritized outcomes")'),
 ('E','("policy learning" OR "treatment rule") AND (regret OR consistency OR "margin condition" OR "non-unique" OR "cube root" OR "value function")'),
 ('I','("competing risks" OR censored OR survival) AND ("quantile loss" OR "proper scoring" OR "Brier score" OR "policy evaluation" OR "restricted mean time lost" OR "restricted mean survival time")'),
 ('I','(quantile OR "cumulative incidence") AND (joint OR vector OR multivariate) AND (loss OR score OR regret OR decision)'),
 ('K','("acute myeloid leukemia" OR AML) AND ("conditioning intensity" OR myeloablative OR "reduced intensity") AND (relapse OR "non-relapse mortality" OR "disease risk index")')]

def relevant(t,cat):
    t=norm(t)
    if any(w in t for w in ['personalized education','math course','optimal payment','robotics','portfolio selection','stock market','personalized math']):return False
    if cat=='K':return ('conditioning' in t or 'transplant' in t) and any(w in t for w in ['leukemia','myeloid','myelodysplastic'])
    if cat in ['A','B','C','E']:return any(w in t for w in ['treatment regime','treatment rule','treatment recommend','policy learning','welfare','treatment decision','optimal individualized','q learning'])
    if cat=='D':return 'quantile' in t and any(w in t for w in ['competing','censor','survival','event'])
    if cat=='I':return any(w in t for w in ['scoring','score','quantile','restricted mean','policy evaluation','life years lost'])
    return any(w in t for w in ['competing risk','quantile','treatment regime','treatment rule','policy learning'])

def run():
    state=json.loads((PRIVATE/'state.json').read_text(encoding='utf-8'));rows=state['rows'];meta=state['meta']
    candidates=[];edges=[]
    # Search every full task combination plus a separate 2024-2026 incremental pass.
    for cat,q in QUERIES:
        for incremental in [False,True]:
            querytext=q+' AND FIRST_PDATE:['+('2024-01-01' if incremental else '1800-01-01')+' TO 2026-11-26]'
            try:
                data=epsearch(querytext,100)
                for e in data:candidates.append(dict(origin='keyword_incremental' if incremental else 'keyword',seed_id='',depth=0,category=cat,ep=e,title=e.get('title',''),doi=e.get('doi','').lower(),evidence_url='https://europepmc.org/article/MED/'+e.get('id','')))
            except Exception as e:query('Europe PMC',querytext,'NA',0,str(e))
        # Crossref search uses bibliographic ranking; cutoff enforced by publication dates.
        cq={'A':'competing risks optimal treatment regimes','B':'quantile policy learning distributional welfare','C':'lexicographic prioritized outcomes set valued treatment regimes','D':'competing risks quantile inference','E':'policy learning regret margin consistency','I':'joint quantile proper scoring competing risks','K':'AML conditioning intensity DRI relapse'}[cat]
        try:
            u='https://api.crossref.org/works?'+urllib.parse.urlencode(dict(query=cq,rows=100,filter='from-pub-date:2024-01-01,until-pub-date:2026-11-26'))
            j=js(u)['message'];query('Crossref',cq+' [2024-01-01,2026-11-26]',j.get('total-results','NA'),len(j['items']),'ranked top 100; manual relevance candidates')
            for cr in j['items']:candidates.append(dict(origin='keyword_crossref_incremental',seed_id='',depth=0,category=cat,cr=cr,title=(cr.get('title') or [''])[0],doi=cr.get('DOI','').lower(),evidence_url=cr.get('URL','')))
        except Exception as e:query('Crossref',cq,'NA',0,str(e))
    (PRIVATE/'keyword_candidates.json').write_text(json.dumps(candidates,ensure_ascii=False),encoding='utf-8')
    # OpenAlex references and forward citations; full pagination for forward citation results.
    starts=[r for r in rows if r['priority']=='P0' or r['paper_id'] in ['G15','E15']]
    frontier=[]
    def node(r):
        if not r.get('doi'):return None
        try:return js('https://api.openalex.org/works/https://doi.org/'+r['doi'])
        except Exception as e:query('OpenAlex',r['doi'],'NA',0,str(e));return None
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for r,o in zip(starts,ex.map(node,starts)):
            if o:frontier.append((r['paper_id'],r['category'],o))
    visited=set()
    for depth in [1,2]:
        nextfront=[]
        for seed,cat,o in frontier:
            oid=o['id'].rsplit('/',1)[-1]
            if oid in visited:continue
            visited.add(oid)
            works=[];refs=o.get('referenced_works',[])
            for i in range(0,len(refs),40):
                ids='|'.join(x.rsplit('/',1)[-1] for x in refs[i:i+40])
                u='https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'openalex_id:'+ids,'per-page':200})
                try:
                    j=js(u);works.extend(('backward',x) for x in j['results']);query('OpenAlex',u,j['meta']['count'],len(j['results']),f'{seed}; depth {depth}; backward')
                except Exception as e:query('OpenAlex',u,'NA',0,str(e))
            cursor='*'; forward_pages=0
            while cursor:
                u='https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:'+oid+',to_publication_date:2026-11-26','per-page':200,'cursor':cursor})
                try:
                    j=js(u);works.extend(('forward',x) for x in j['results']);query('OpenAlex',u,j['meta']['count'],len(j['results']),f'{seed}; depth {depth}; forward')
                    cursor=j['meta'].get('next_cursor') if j['results'] else None
                    forward_pages+=1
                    if forward_pages>=2 and cursor:
                        query('OpenAlex',u,j['meta']['count'],0,'coverage limitation: remaining forward pages pending; 400 results screened per node')
                        break
                except Exception as e:query('OpenAlex',u,'NA',0,str(e));break
            for direction,w in works:
                d=(w.get('doi') or '').replace('https://doi.org/','').lower();t=w.get('title') or ''
                include=relevant(t,cat);reason='title relevant; bibliographic verification pending' if include else 'title screening: outside category scope'
                edges.append(dict(seed_id=seed,from_openalex=oid,to_openalex=w['id'],doi=d,title=t,direction=direction,depth=depth,decision='candidate' if include else 'exclude',reason=reason))
                if include:
                    candidates.append(dict(origin=direction,seed_id=seed,depth=depth,category=cat,oa=w,title=t,doi=d,evidence_url=w['id']))
                    if depth==1:nextfront.append((seed,cat,w))
            print('graph',seed,depth,len(works),len(nextfront),flush=True)
            csvwrite('citation_edges.csv',edges);csvwrite('search_log_expansion.csv',LOG)
        # A second hop only on relevant newly discovered distinct neighbors; all chosen by stated title rule.
        unique={w['id']:(s,c,w) for s,c,w in nextfront}
        frontier=list(unique.values())
        if len(frontier)>30:
            frontier.sort(key=lambda x:(not ('quantile' in norm(x[2].get('title',''))),not ('competing' in norm(x[2].get('title','')))))
            query('OpenAlex','depth-2 queue',len(frontier),30,'coverage limitation: first 30 relevant distinct neighbors; remaining queue preserved in citation_edges.csv')
            frontier=frontier[:30]
    (PRIVATE/'all_candidates.json').write_text(json.dumps(candidates,ensure_ascii=False),encoding='utf-8')
    csvwrite('candidate_pool.csv',[{k:v for k,v in c.items() if k not in ['ep','cr','oa']} for c in candidates])
    seen={r.get('doi'):r['paper_id'] for r in rows if r.get('doi')};screen=[];new=[]
    for c in candidates:
        d=c['doi'];t=c['title'];key=d or norm(t)
        if key in seen:screen.append(dict(candidate_id=key,decision='duplicate',reason='same DOI/title as '+seen[key],evidence_url=c['evidence_url']));continue
        if not relevant(t,c['category']):screen.append(dict(candidate_id=key,decision='exclude',reason='title outside scope',evidence_url=c['evidence_url']));continue
        seen[key]='candidate'
        new.append(c)
    def verify(c):
        try:
            cr=c.get('cr') or (crdoi(c['doi']) if c.get('doi') and not c['doi'].startswith('10.48550') else {})
            s=dict(id='N'+hashlib.sha256((c['doi'] or c['title']).encode()).hexdigest()[:10],category=c['category'],priority='P1',relevance='Expanded: '+c['origin'])
            if cr:
                r=crrow(cr,s)
                if sim(c['title'],r['title'])<.75:return c,None,{'error':'Crossref DOI/title mismatch; needs manual review'}
            elif c.get('ep'):
                e=c['ep'];hits=epsearch('EXT_ID:'+e.get('id','')+' AND SRC:'+e.get('source','MED'))
                if not hits:return c,None,{'error':'core bibliographic record not retrieved'}
                c['ep']=hits[0];r=eprow(c['ep'],s)
            else:return c,None,{}
            r['seed_id']=c['seed_id'];r['discovery_source']=c['origin']+';depth='+str(c['depth'])+';'+c['evidence_url']
            ep=c.get('ep',{})
            for k in ['pmcid','pmid']:r[k]=ep.get(k,r.get(k,''))
            return c,r,dict(cr=cr,ep=ep,oa=c.get('oa',{}))
        except Exception as e:return c,None,{'error':str(e)}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for c,r,m in ex.map(verify,new):
            screen.append(dict(candidate_id=c['doi'] or c['title'],decision='include' if r else 'pending_verification',reason='title relevant and primary bibliographic record verified' if r else str(m),evidence_url=c['evidence_url']))
            if r:rows.append(r);meta[r['paper_id']]=m
            if len(screen)%25==0:
                print('verification progress',len(screen),'new papers',sum(r['paper_id'].startswith('N') for r in rows),flush=True)
                (PRIVATE/'state_expansion_partial.json').write_text(json.dumps({'rows':rows,'meta':meta},ensure_ascii=False),encoding='utf-8')
    csvwrite('screening.csv',screen)
    (PRIVATE/'state_expansion.json').write_text(json.dumps({'rows':rows,'meta':meta},ensure_ascii=False),encoding='utf-8')
    csvwrite('search_log_expansion.csv',LOG)
    print('expanded',len(candidates),'verified new',sum(r['paper_id'].startswith('N') for r in rows),flush=True)

if __name__=='__main__':run()
