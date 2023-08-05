import PyPDF2

template = PyPDF2.PdfReader(open('twopage.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('img.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)
  
    