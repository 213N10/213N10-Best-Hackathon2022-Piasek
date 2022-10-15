import PyPDF2 
    
pdfFileObj = open('testerinho.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
pageObj = pdfReader.getPage(1) 
texter = pageObj.extractText()

texter = texter.split("\n")
texter.pop(0)
texter.pop(0)
texter.pop(0)

cnt = 0
while cnt < len(texter):
    if ("\"" not in texter[cnt]):
        texter.pop(cnt)
        cnt -= 1
    cnt += 1
print(texter)  

pdfFileObj.close() 