import PyPDF2
import sys

input = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger=PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("Total.pdf")

pdf_combiner(input)