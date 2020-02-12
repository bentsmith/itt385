import PyPDF2

pdf_file = open("C:\\Users\\labuser\\Desktop\\Hello World.pdf", "rb")

pdf = PyPDF2.PdfFileReader(pdf_file)

first_page = pdf.getPage(0)

text = first_page.extractText()

print("First page text is", text)