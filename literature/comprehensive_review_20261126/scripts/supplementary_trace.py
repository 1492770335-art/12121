from collect import *
from expand import relevant
def run():
    state=json.loads((PRIVATE/'state.json').read_text(encoding='utf-8'));starts=[r for r in state['rows'] if r['paper_id'] in ['A02','I01','G01','J01','G15','E15']];edges=[]
    for r in starts:
        try:
            if r.get('doi'):o=js('https://api.openalex.org/works/https://doi.org/'+r['doi'])
            else:
                data=js('https://api.openalex.org/works?'+urllib.parse.urlencode({'search':r['title'],'per-page':5}))['results']
                o=max(data,key=lambda m:sim(r['title'],m.get('title') or ''))
                if sim(r['title'],o.get('title') or '')<.85:raise ValueError('OpenAlex title match not secure')
            oid=o['id'].rsplit('/',1)[-1];works=[];refs=o.get('referenced_works',[])
            for i in range(0,len(refs),40):
                u='https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'openalex_id:'+'|'.join(x.rsplit('/',1)[-1] for x in refs[i:i+40]),'per-page':200})
                j=js(u);works.extend(('backward',w) for w in j['results']);query('OpenAlex',u,j['meta']['count'],len(j['results']),r['paper_id']+' supplementary depth 1')
            u='https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:'+oid+',to_publication_date:2026-11-26','per-page':200})
            j=js(u);works.extend(('forward',w) for w in j['results']);query('OpenAlex',u,j['meta']['count'],len(j['results']),r['paper_id']+' supplementary forward; first page only; remainder pending if count>200')
            for direction,w in works:
                edges.append(dict(seed_id=r['paper_id'],from_openalex=o['id'],to_openalex=w['id'],doi=(w.get('doi') or '').replace('https://doi.org/',''),title=w.get('title',''),direction=direction,depth=1,decision='candidate' if relevant(w.get('title') or '',r['category']) else 'exclude',reason='Supplementary trace: bibliography and scope screening pending for candidates'))
            print('extra trace',r['paper_id'],len(works),flush=True)
        except Exception as e:query('OpenAlex',r.get('doi') or r['title'],'NA',0,str(e)+'; supplementary trace incomplete')
        csvwrite('citation_edges_supplementary.csv',edges);csvwrite('search_log_trace_supplementary.csv',LOG)
if __name__=='__main__':run()
