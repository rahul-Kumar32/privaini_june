import PyPDF2


pdffileobj = open('privaini.pdf', 'rb')

pdfreader = PyPDF2.PdfFileReader(pdffileobj)

print(f"no of pages: {pdfreader.numPages}")

pageobj = pdfreader.getPage(0)

text = pageobj.extractText()

pdffileobj.close()

with open("demo.txt", "a") as file:
    file.writelines(text)