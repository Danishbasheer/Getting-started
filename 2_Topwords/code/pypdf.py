from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFPageInterpreter,PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

def process_page(path,password=""): 
	file=open(path,'rb')
	pages=PDFPage.get_pages(file,password=password)
	rsmgr=PDFResourceManager()
	laout=LAParams()
	bfrstr=StringIO()
	textconv=TextConverter(rsmgr,bfrstr,laparams=laout)
	intprtr=PDFPageInterpreter(rsmgr,textconv)
	for page in pages:
		intprtr.process_page(page)    
	text=bfrstr.getvalue()
	file.close()
	textconv.close()
	bfrstr.close()
	return text
