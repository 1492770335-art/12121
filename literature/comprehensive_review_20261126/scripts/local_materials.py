from collect import *
import shutil
def run():
    rows=[]
    def add(pid,source,url,kind,version,license='',licurl='',public=False):
        d=Path(source).read_bytes();doc=PdfReader(io.BytesIO(d));text=doc.pages[0].extract_text() or ''
        root=BASE/'open_access' if public else PRIVATE
        p=root/pid/Path(source).name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(d)
        rows.append(dict(paper_id=pid,artifact_type=kind,version=version,status='downloaded' if source.startswith(str(PRIVATE)) else 'existing_local_verified',source_url=url,final_url=url,license=license or 'license_unclear; local copy only',license_evidence=licurl,local_path=str(p),repo_path=p.relative_to(BASE).as_posix() if public else '',sha256=hashlib.sha256(d).hexdigest(),bytes=len(d),pages=len(doc.pages),fetched_at=stamp(),error=''))
    root=Path('D:/最后一版/参考文献原文')
    add('A02',str(root/'2411.08315v1.pdf'),'https://arxiv.org/abs/2411.08315v1','main','arXiv v1; 47 pages')
    add('D03',str(root/'peng2009(3).pdf'),'https://doi.org/10.1198/jasa.2009.tm08228','main','existing local publisher copy; restricted distribution')
    add('A03',str(root/'Transformation-Invariant Learning of Optimal Individualized Decision Rules with Time-to-Event Outcomes(1).pdf'),'https://doi.org/10.1080/01621459.2022.2068420','main','existing local version of record')
    add('A03',str(root/'Transformation_supp(1).pdf'),'https://doi.org/10.1080/01621459.2022.2068420','supplement','existing local journal supplement; title and four authors checked')
    add('C02',str(PRIVATE/'JMLR.pdf'),'https://jmlr.org/papers/volume21/20-334/20-334.pdf','main','JMLR final; 28 pages','CC-BY 4.0','https://creativecommons.org/licenses/by/4.0/ ; license printed on PDF page 1',True)
    add('J01',str(PRIVATE/'DVK.pdf'),'https://www.ism.ac.jp/editsec/aism/72/0577.pdf','main','official journal PDF; 29 pages')
    p=BASE/'license_evidence'/'C02_fulltext.md';p.parent.mkdir(exist_ok=True)
    p.write_text('# C02 redistribution evidence\n\nSource: https://jmlr.org/papers/volume21/20-334/20-334.pdf\n\nPDF page 1: License CC-BY 4.0, https://creativecommons.org/licenses/by/4.0/.\n\nAttribution: Haomiao Meng, Ying-Qi Zhao, Haoda Fu and Xingye Qiao (2020), Near-optimal Individualized Treatment Recommendations, JMLR 21(183):1-28.\n\nUnmodified original PDF; attribution requirements: https://jmlr.org/papers/v21/20-334.html.\n',encoding='utf-8')
    csvwrite('local_materials_manifest.csv',rows)
if __name__=='__main__':run()
