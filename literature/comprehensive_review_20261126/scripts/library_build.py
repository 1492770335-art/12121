"""Build a licensed, page-addressable reading library without rewriting mathematics."""
from library_audit import *
import shutil, importlib.metadata
from collections import defaultdict,Counter

def dump(p,value):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
def write(p,text):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')
def page_info(doc,page,i):
    text=page.get_text(sort=False)
    fonts=[s.get('font','') for b in page.get_text('dict')['blocks'] if b.get('type')==0 for l in b.get('lines',[]) for s in l.get('spans',[])]
    math=bool(re.search(r'[∑∏∫√≤≥∈∀∃∂∞βγθλστ]|\(\d+[a-z]?\)',text)) or any(re.search(r'CM(?:MI|SY|EX)|Math|Symbol|MSBM',f,re.I) for f in fonts)
    lines=[l.strip() for l in text.splitlines() if l.strip()]
    hints=[l for l in lines[:4]+lines[-4:] if re.fullmatch(r'\d{1,4}|[ivxlcdm]{1,8}',l,re.I)]
    anchors=[]
    for line in lines:
        m=re.match(r'^(Theorem|Lemma|Proposition|Corollary|Assumption|Condition|Proof|Appendix|Supplement(?:ary)?)(?:\s+([A-Z]?\.?\d+(?:\.\d+)*|[A-Z]))?',line,re.I)
        if m:anchors.append(m[0])
    return text,dict(pdf_page=i+1,pdf_page_label=page.get_label() or '',printed_number_candidates=hints,has_math_or_equation_number=math,requires_formula_check=math,text_layer_available=bool(text.strip()),replacement_character_count=text.count('\ufffd'),anchors=list(dict.fromkeys(anchors)))

def pdf_transcript(a,dest):
    p=Path(a['local_path']);doc=pymupdf.open(p);pages=[]
    intro=f"# {CAT[a['paper_id']]['title']}\n\nOriginal PDF: [original.pdf](original.pdf). SHA256: `{a['sha256']}`.\n\nThis is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.\n\n"
    md=[intro];txt=[intro.replace('# ','')]
    for i,page in enumerate(doc):
        text,info=page_info(doc,page,i);pages.append(info)
        note='FORMULA CHECK REQUIRED: original PDF page '+str(i+1)+'.' if info['requires_formula_check'] else 'Technical extraction; compare with original PDF page '+str(i+1)+'.'
        if not info['text_layer_available']:note+=' NO TEXT LAYER: no OCR or invented transcription supplied.'
        label='; PDF label '+info['pdf_page_label'] if info['pdf_page_label'] else ''
        md.extend([f"## PDF page {i+1}{label}\n\n{note}\n\n",'````text\n'+text+'\n````\n\n'])
        txt.extend([f"\n\f===== ORIGINAL PDF PAGE {i+1}{label} =====\n{note}\n",text,'\n'])
    write(dest/'fulltext.md',''.join(md));write(dest/'fulltext.txt',''.join(txt));dump(dest/'page_map.json',pages)
    return pages

def jats_transcript(a,dest):
    root=ET.parse(a['local_path']).getroot();equations=[]
    def tag(e):return e.tag.rsplit('}',1)[-1]
    def render(e):
        name=tag(e)
        if name in ['tex-math','math']:
            if name=='tex-math':
                s=''.join(e.itertext());equations.append(dict(kind='original_jats_tex_math',source_id=e.attrib.get('id',''),text=s));return '\n````latex\n'+s+'\n````\n'
            s=ET.tostring(e,encoding='unicode');equations.append(dict(kind='original_mathml',source_id=e.attrib.get('id',''),text=s));return '\n````xml\n'+s+'\n````\n'
        if name in ['inline-graphic','graphic']:
            href=e.attrib.get('{http://www.w3.org/1999/xlink}href','');return '[ORIGINAL IMAGE / POSSIBLE FORMULA: '+href+'; not reconstructed]'
        s=e.text or ''
        for c in e:s+=render(c)+(c.tail or '')
        if name=='title':return '\n\n### '+s+'\n\n'
        if name in ['sec','p','disp-formula','table-wrap','ref','app','caption','list-item']:return '\n'+s+'\n'
        return s
    parts=['# '+CAT[a['paper_id']]['title']+'\n\nSource: [original.xml](original.xml).\n\nPAGINATION UNAVAILABLE: this original JATS XML does not supply a verified PDF page map. Sections and original formula markup are preserved; no PDF pages are invented. TeX-math and MathML blocks below are original XML content, not reconstructed equations. Formula images remain unresolved and are flagged.\n\n']
    for path in ['.//article-meta/abstract','./body','./back']:
        for node in root.findall(path):parts.append(render(node))
    text='\n'.join(parts);write(dest/'fulltext.md',text);write(dest/'fulltext.txt',text);dump(dest/'original_formula_markup.json',equations)
    return []

def run():
    audits=read('fulltext_library/license_audit.csv')
    extra=ROOT/'new_artifact_audit.csv'
    if extra.exists():audits+=read('fulltext_library/new_artifact_audit.csv')
    pdfextras=ROOT/'public_pdf_audit.csv'
    if pdfextras.exists():audits+=read('fulltext_library/public_pdf_audit.csv')
    ids=sorted({a['paper_id'] for a in audits}|set(CORE))
    bypid=defaultdict(list)
    for a in audits:bypid[a['paper_id']].append(a)
    # Hash-identical files are stored once, while each paper_id retains its own directory.
    owners={};public_files=[];artifact_index=[];index=[];mathpages=[];notes_count=0
    texrows=read('fulltext_library/latex_acquisition.csv') if (ROOT/'latex_acquisition.csv').exists() else []
    texmap={x['arxiv_id']:x for x in texrows}
    for pid in ids:
        r=CAT[pid];folder=ROOT/r['category']/pid;folder.mkdir(parents=True,exist_ok=True)
        arr=bypid[pid];entry=dict(paper_id=pid,category=r['category'],title=r['title'],authors=r['authors'],doi=r.get('doi',''),year=r.get('year_issue') or r.get('year_online') or r.get('year_publication',''),original_url=r['source_url'],local_fulltext=any(a['artifact_type']=='main' for a in arr),public_pdf=[],public_markdown=[],public_txt=[],original_tex=[],public_xml=[],supplements=[],license_decisions=[],hash_duplicate_of=[],readme=(folder/'README.md').relative_to(ROOT).as_posix())
        observed=[]
        for a in arr:
            if a['decision']!='public_allowed':
                entry['license_decisions'].append(dict(sha256=a['sha256'],decision='local_only',reason=a['reason'],license_url=a['license_url'],source_url=a['source_url']))
                if Path(a['local_path']).suffix.lower()=='.pdf':
                    doc=pymupdf.open(a['local_path'])
                    for i,page in enumerate(doc):
                        _,info=page_info(doc,page,i)
                        if info['anchors']:observed.append(dict(pdf_page=i+1,sha256=a['sha256'],anchors=info['anchors'][:6]))
                continue
            key=a['sha256']
            if key in owners:
                paths=owners[key];entry['hash_duplicate_of'].append(paths['paper_id'])
            else:
                dest=folder/'artifacts'/key[:12];dest.mkdir(parents=True,exist_ok=True)
                suffix=Path(a['local_path']).suffix.lower();original=dest/('original'+suffix);shutil.copyfile(a['local_path'],original)
                metadata={k:v for k,v in a.items() if k!='local_path'}
                metadata.update(title=r['title'],authors=r['authors'],doi=r.get('doi',''),license_scope='This exact file/version only; not other publisher versions',reuse='Noncommercial research collection; respect each file license and third-party exclusions',transformation='Technical format extraction only; original bytes unchanged; no translation or mathematical correction')
                # Public proof is minimal rights metadata, never an unrestricted abstract-page scrape.
                if a['reason'] in ['arxiv_exact_version_creative_commons','arxiv_pinned_version_hash_and_license_matched']:
                    s=(WORK/(key+'.arxiv.html')).read_text(encoding='utf-8');m=re.search(r'<div class="abs-license">(.*?)</div>',s,re.S);metadata['original_rights_html']=m[0] if m else ''
                proof=WORK/(key+'.pdf_license.json')
                if proof.exists():metadata['printed_pdf_license_locations']=json.loads(proof.read_text(encoding='utf-8'))
                dump(dest/'provenance_and_license.json',metadata)
                if suffix=='.pdf':
                    pages=pdf_transcript(a,dest)
                    mathpages.extend(dict(paper_id=pid,artifact_sha256=key,**p) for p in pages if p['requires_formula_check'] or not p['text_layer_available'])
                elif suffix=='.xml':pages=jats_transcript(a,dest)
                else:raise ValueError('Unsupported public artifact '+str(original))
                paths=dict(paper_id=pid,original=original.relative_to(ROOT).as_posix(),md=(dest/'fulltext.md').relative_to(ROOT).as_posix(),txt=(dest/'fulltext.txt').relative_to(ROOT).as_posix(),tex=[],license=a['license_url'],format=suffix,pages=len(pages),provenance=(dest/'provenance_and_license.json').relative_to(ROOT).as_posix())
                aid=a.get('arxiv_id','');tr=texmap.get(aid,{})
                if aid and tr.get('status')=='downloaded_original_tex':
                    sourcefolder=WORK/'tex'/aid
                    for source in sourcefolder.rglob('*.tex'):
                        target=dest/'latex'/source.relative_to(sourcefolder);target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target);paths['tex'].append(target.relative_to(ROOT).as_posix())
                    shutil.copyfile(sourcefolder/'source_manifest.json',dest/'latex'/'source_manifest.json')
                owners[key]=paths
                artifact_index.append(dict(paper_id=pid,sha256=key,artifact_type=a['artifact_type'],original=paths['original'],markdown=paths['md'],txt=paths['txt'],latex=';'.join(paths['tex']),license_url=a['license_url'],source_url=a['source_url'],pdf_pages=paths['pages'] if suffix=='.pdf' else '',pagination='original_pdf_physical_pages' if suffix=='.pdf' else 'no_verified_pdf_pagination'))
            entry['license_decisions'].append(dict(sha256=key,decision='public_allowed',license_url=a['license_url'],source_url=a['source_url'],provenance=paths['provenance']))
            if a['artifact_type']=='supplement':entry['supplements'].append(paths['original'])
            elif paths['format']=='.pdf':entry['public_pdf'].append(paths['original'])
            else:entry['public_xml'].append(paths['original'])
            entry['public_markdown'].append(paths['md']);entry['public_txt'].append(paths['txt']);entry['original_tex']+=paths['tex']
        for key in ['public_pdf','public_xml','public_markdown','public_txt','original_tex','supplements']:entry[key]=list(dict.fromkeys(entry[key]))
        entry['status']='public_fulltext' if entry['public_pdf'] or entry['public_xml'] else 'local_only' if entry['local_fulltext'] else 'not_acquired'
        dump(folder/'metadata.json',entry)
        body=[f"# {pid} — {r['title']}", '',r['authors'], '',f"DOI: {r.get('doi') or 'not assigned / not resolved'}",f"Original: {r['source_url']}",f"Availability: **{entry['status']}**",'']
        for field,label in [('public_pdf','Original PDF'),('public_xml','Original JATS XML'),('public_markdown','Full-text Markdown'),('public_txt','Full-text TXT'),('original_tex','Original TeX'),('supplements','Supplement')]:
            for path in entry[field]:body.append(f"- {label}: [{Path(path).name}]({os.path.relpath(ROOT/path,folder).replace(os.sep,'/')})")
        if not entry['public_markdown']:body.append('No full-text Markdown/TXT is published for this entry. See licensing decisions in metadata.json; a public URL or arXiv nonexclusive distribution license is not a redistribution grant.')
        body.extend(['','[Original reading-location note](reading_note.md). This note is a preparation record, not a completed theorem review.'])
        write(folder/'README.md','\n'.join(body)+'\n')
        note=[f"# {pid}：版本与精读准备札记",'',f"题名：{r['title']}。原文入口：{r['source_url']}。",'',f"目录研究用途：{r.get('relevance','')}。这项用途来自检索目录，尚未据此认定原文定理适用于本项目。",'','本札记记录文件身份、实际扫描到的位置和后续精读问题，不复制受限正文，也不声称已完成证明有效性审核。']
        if observed:
            note+=['','在本地原始PDF中观察到以下定位（物理页码；不同SHA代表不同版本）：']
            note += [f"- PDF第{x['pdf_page']}页；文件 `{x['sha256'][:12]}`；标签："+'、'.join(x['anchors']) for x in observed[:12]]
        elif entry['local_fulltext']:note+=['','已核对本地全文文件；未用自动扫描结果虚构定理编号。实际文件及许可状态见metadata.json。']
        else:note+=['','正文尚未取得。当前只可核对书目与原文入口，不能填写原文定理、公式或页码。']
        note+=['','后续精读检查：先确定统计目标、数据结构与版本，再分别记录识别条件、估计条件和决策边界条件。对每个拟引用的结论，应沿正文—附录—外部引理核对依赖；比较条件分位数、边际分位数、CIF反演和净分布目标时，不预设它们相同。公式以原始PDF及作者TeX为准。']
        write(folder/'reading_note.md','\n'.join(note)+'\n');notes_count+=1;index.append(entry)
    dump(ROOT/'index.json',index);csvwrite('fulltext_library/artifact_index.csv',artifact_index)
    csvwrite('fulltext_library/index.csv',[{k:(';'.join(v) if isinstance(v,list) and (not v or isinstance(v[0],str)) else json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v) for k,v in r.items()} for r in index])
    dump(ROOT/'formula_page_flags.json',mathpages)
    # Preserve cross-ID duplicate evidence instead of silently inflating file counts.
    hashids=defaultdict(set)
    for a in audits:hashids[a['sha256']].add(a['paper_id'])
    dump(ROOT/'duplicate_files.json',[dict(sha256=h,paper_ids=sorted(v)) for h,v in hashids.items() if len(v)>1])
    summary=dict(entries=len(index),baseline_paper_ids=len({a['paper_id'] for a in read('fulltext_library/license_audit.csv')}),baseline_artifact_records=len(read('fulltext_library/license_audit.csv')),all_audited_artifact_records=len(audits),unique_audited_hashes=len({a['sha256'] for a in audits}),public_entries=sum(r['status']=='public_fulltext' for r in index),local_only_entries=sum(r['status']=='local_only' for r in index),not_acquired_entries=sum(r['status']=='not_acquired' for r in index),public_unique_artifacts=len(artifact_index),public_original_pdf=sum(a['original'].endswith('.pdf') for a in artifact_index),public_original_xml=sum(a['original'].endswith('.xml') for a in artifact_index),public_markdown=len(artifact_index),public_txt=len(artifact_index),original_tex_files=sum(len(o['tex']) for o in owners.values()),reading_notes=notes_count,formula_flagged_pages=len(mathpages),core_new_fulltexts=len({a['paper_id'] for a in audits if a['paper_id'] in CORE and a['artifact_type']=='main'}),built_at=stamp())
    dump(ROOT/'summary.json',summary)
    overview=['# 可公开全文与精读入口','', '本目录用于通过GitHub按paper_id读取资料。文件的许可、版本和数学保真度均单独记录。全文仅公开在明确许可允许的范围内；NC/ND/SA条件继续适用。本库用于非商业学术研究，不授予超出原许可的使用权。','', 'PDF保持原始字节不变。Markdown/TXT按原始PDF物理页分段，不重构或纠正公式；每个含数学符号或公式编号的页面均提示核对原PDF。作者原始TeX以字节及SHA256保留，未编译。XML来源没有可验证PDF分页时，使用结构化章节索引，并明确写明无PDF分页。','', '## 统计','', '```json',json.dumps(summary,ensure_ascii=False,indent=2),'```','','## 读取方法','', '先读[index.csv](index.csv)或[index.json](index.json)，再按条目的public_markdown/public_txt/original_tex路径读取。大文件可用GitHub fetch_file的start_line/end_line分段。公式页标记见[formula_page_flags.json](formula_page_flags.json)。原文、转换稿、原始TeX和补充材料不能互相替代。','', '完整许可逐文件记录见[license_audit.csv](license_audit.csv)、[new_artifact_audit.csv](new_artifact_audit.csv)以及各artifact下provenance_and_license.json。hash重复记录见[duplicate_files.json](duplicate_files.json)。','', '## 文献入口','','|paper_id|类别|状态|原始PDF|Markdown|TeX文件数|','|---|---|---|---|---|---:|']
    for r in index:overview.append(f"|[{r['paper_id']}]({r['readme']})|{r['category']}|{r['status']}|{len(r['public_pdf'])}|{len(r['public_markdown'])}|{len(r['original_tex'])}|")
    write(ROOT/'README.md','\n'.join(overview)+'\n')
    print(json.dumps(summary,ensure_ascii=False),flush=True)
if __name__=='__main__':run()
