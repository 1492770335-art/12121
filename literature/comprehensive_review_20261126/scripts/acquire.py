from collect import *
import argparse
def run():
    p=argparse.ArgumentParser();p.add_argument('--priority',default='P0');p.add_argument('--new-only',action='store_true');args=p.parse_args()
    statepath=PRIVATE/('state_expansion.json' if args.new_only else 'state.json')
    if args.new_only and not statepath.exists():statepath=PRIVATE/'state_expansion_partial.json'
    state=json.loads(statepath.read_text(encoding='utf-8'));rows=state['rows'];meta=state['meta'];out=[]
    for name in ['download_manifest_p0.csv','download_manifest.csv']:
        f=BASE/name
        if f.exists():out.extend(csv.DictReader(f.open(encoding='utf-8-sig')))
    # This run does not repeat URLs already failed in this same collection session.
    failures={a['source_url']:a['error'] for a in out if a.get('status')=='download_failed' and a.get('error')!='title_first_page_requires_review'}
    import collect
    if args.new_only:collect.REQUEST_TIMEOUT=8
    original_get=collect.get
    def resumable_get(url,binary=False):
        if url in failures:
            cache=CACHE/hashlib.sha256(url.encode()).hexdigest()
            if not cache.exists():raise RuntimeError('earlier attempt this session: '+failures[url])
        return original_get(url,binary)
    collect.get=resumable_get
    # Keep actual previous attempts, append fresh verified successes.
    todo=[r for r in rows if r['priority']==args.priority and (not args.new_only or r['paper_id'].startswith('N'))]
    if args.new_only:
        attempted={a['paper_id'] for a in out}
        todo=[r for r in todo if r['paper_id'] not in attempted]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6 if args.new_only else 5) as ex:
        futures=[ex.submit(acquire_one,r,meta.get(r['paper_id'],{})) for r in todo]
        for f in concurrent.futures.as_completed(futures):
            try:out.extend(f.result())
            except Exception as e:print('worker failure',e,flush=True)
            csvwrite('download_manifest.csv',out)
    print('acquired priority',args.priority,len(todo),flush=True)
if __name__=='__main__':run()
