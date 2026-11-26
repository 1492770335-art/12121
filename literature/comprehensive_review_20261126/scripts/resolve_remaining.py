from collect import *
import html
TITLE_OVERRIDES={'K09':'Diagnosis and management of AML in adults: 2022 recommendations from an international expert panel on behalf of the ELN','K04':'Myeloablative versus Reduced-Intensity Conditioning for Hematopoietic Cell Transplantation in Acute Myelogenous Leukemia and Myelodysplastic Syndromes—Long-Term Follow-Up of the BMT CTN 0901 Clinical Trial','G13':'Flexible parametric proportional-hazards and proportional-odds models for censored survival data, with application to prognostic modelling and estimation of treatment effects'}
def run():
    state=json.loads((PRIVATE/'state.json').read_text(encoding='utf-8'));rows=state['rows'];meta=state['meta'];ss={s['id']:s for s in csv.DictReader((BASE/'literature_catalog.csv').open(encoding='utf-8-sig'))}
    todo=[r for r in rows if r['status'].startswith('unresolved')]
    out=[]
    def one(r):
        pid=r['paper_id'];title=TITLE_OVERRIDES.get(pid,r['title']);s=ss[pid]
        try:
            u='https://api.crossref.org/works?'+urllib.parse.urlencode({'query.title':title,'rows':8})
            j=js(u)['message'];query('Crossref',u,j.get('total-results','NA'),len(j['items']),'exact title recheck for unresolved seed')
            cand=sorted(j['items'],key=lambda m:(sim(title,(m.get('title') or [''])[0]),m.get('type')=='journal-article'),reverse=True)
            for cr in cand:
                ct=(cr.get('title') or [''])[0]
                if sim(title,ct)<.86:continue
                author=norm(s['author_hint']).split()[0];names=norm(' '.join(a.get('family','') for a in cr.get('author',[])))
                if author not in ['authors','author'] and author not in names:continue
                rnew=crrow(cr,s);rnew['title']=' '.join(html.unescape(re.sub('<[^>]+>','',rnew['title'])).split());rnew['discovery_source']='unresolved seed exact-title recheck'
                ep={}
                try:
                    hits=epsearch('DOI:"'+rnew['doi']+'"');ep=next((e for e in hits if e.get('doi','').lower()==rnew['doi']),{})
                    for k in ['pmid','pmcid']:rnew[k]=ep.get(k,'')
                except Exception:pass
                print('resolved extra',pid,flush=True);return r,rnew,dict(cr=cr,ep=ep)
        except Exception as e:print('still pending',pid,str(e),flush=True)
        return r,None,{}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for old,new,m in ex.map(one,todo):
            if new:rows.remove(old);rows.append(new);meta[new['paper_id']]=m
    # Preserve previous query records rather than replacing the seed log.
    old=list(csv.DictReader((BASE/'search_log.csv').open(encoding='utf-8-sig')))
    save_state(rows,meta);csvwrite('search_log.csv',old+LOG)
if __name__=='__main__':run()
