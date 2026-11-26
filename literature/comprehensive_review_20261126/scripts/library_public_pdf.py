"""Try official PDFs for already licensed XML articles; do not fabricate pagination."""
from library_core_fetch import one
from library_audit import *
def run():
    rows=[]
    official={
      'I10':'https://academic.oup.com/biostatistics/article-pdf/15/3/526/599536/kxt059.pdf',
      'I12':'https://link.springer.com/content/pdf/10.1186/1471-2288-13-152.pdf',
      'I14':'https://journals.sagepub.com/doi/pdf/10.1177/09622802241242325',
      'N2b4fb3717a':'https://link.springer.com/content/pdf/10.1186/s12874-026-02960-8.pdf',
      'N39eca4fc6b':'https://www.mdpi.com/2072-6694/18/10/1665/pdf',
      'N982a041314':'https://link.springer.com/content/pdf/10.1007/s00277-026-06881-w.pdf',
      'Nabaf548cd2':'https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2026.1795475/pdf'}
    for a in read('fulltext_library/license_audit.csv'):
        if a['decision']!='public_allowed' or a['format']!='xml':continue
        pid=a['paper_id'];u=official.get(pid)
        if u:rows.append((pid,u,'main','official publisher PDF corresponding to licensed JATS'))
    attempts=[];audit=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        for a in ex.map(one,rows):
            attempts.append(a)
            if a['status']=='downloaded':audit.append(audit_one(a))
    csvwrite('fulltext_library/public_pdf_attempts.csv',attempts);csvwrite('fulltext_library/public_pdf_audit.csv',audit)
if __name__=='__main__':run()
