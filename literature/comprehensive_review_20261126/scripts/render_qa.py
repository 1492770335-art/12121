from collect import PRIVATE
import pymupdf
files=[next((PRIVATE/x).glob('*.pdf')) for x in ['B02','B03','E02','A02']]
sheet=pymupdf.open();page=sheet.new_page(width=1000,height=1400)
for i,p in enumerate(files):
    doc=pymupdf.open(p);pix=doc[0].get_pixmap(matrix=pymupdf.Matrix(1,1))
    x,y=(i%2)*500,(i//2)*700
    page.insert_image(pymupdf.Rect(x,y+25,x+490,y+685),pixmap=pix)
    page.insert_text((x+5,y+15),p.parent.name)
(PRIVATE/'qa').mkdir(exist_ok=True);page.get_pixmap().save(PRIVATE/'qa/followup_contact_sheet.png')
