from library_audit import *
def run():
    locator=[]
    for p in ROOT.rglob('page_map.json'):
        rows=json.loads(p.read_text(encoding='utf-8'));md=(p.parent/'fulltext.md').read_text(encoding='utf-8').splitlines();txt=(p.parent/'fulltext.txt').read_text(encoding='utf-8').splitlines()
        starts=[i+1 for i,l in enumerate(md) if re.match(r'^## PDF page \d+',l)]
        tstarts=[i+1 for i,l in enumerate(txt) if l.startswith('===== ORIGINAL PDF PAGE ')]
        if len(starts)!=len(rows) or len(tstarts)!=len(rows):raise ValueError('line-map page count mismatch '+str(p))
        pid=p.parents[2].name
        for i,r in enumerate(rows):
            r.update(markdown_start_line=starts[i],markdown_end_line=(starts[i+1]-1 if i+1<len(starts) else len(md)),txt_start_line=tstarts[i],txt_end_line=(tstarts[i+1]-1 if i+1<len(tstarts) else len(txt)))
            if r['anchors']:locator.append(dict(paper_id=pid,pdf_page=r['pdf_page'],markdown=(p.parent/'fulltext.md').relative_to(ROOT).as_posix(),start_line=r['markdown_start_line'],end_line=r['markdown_end_line'],observed_labels=';'.join(r['anchors'])))
        p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    csvwrite('fulltext_library/theorem_proof_locator.csv',locator)
    print('line-mapped documents',len(list(ROOT.rglob('page_map.json'))),'locator rows',len(locator),flush=True)
if __name__=='__main__':run()
