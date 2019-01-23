from tabula import read_pdf
import re
import PyPDF2

reader = PyPDF2.PdfFileReader(open('C:/Users/shbhagwa/Downloads/sample.pdf', mode='rb'))
n = reader.getNumPages()

dict = {}

for page in range(1, n+1):
    df = []
    df.append(read_pdf('C:/Users/shbhagwa/Downloads/sample.pdf', pages=page))
    dict[page] = df
print(dict)