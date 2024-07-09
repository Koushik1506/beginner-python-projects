import PyPDF2


def pdf_merger(pdf_files):
    merger = PyPDF2.PdfMerger()
    for file in pdf_files:
        op_file = open(file, "rb")
        pdf_reader = PyPDF2.PdfReader(op_file)
        merger.append(pdf_reader)
        op_file.close()
    merger.write("merged.pdf")
    merger.close()


number_of_files_to_be_merged = int(input("Enter Number of PDF files to be merged: "))
if number_of_files_to_be_merged < 2:
    raise ValueError("You Need Minimum 2 PDFs To Be Merged")
pdf_files = []
for i in range(number_of_files_to_be_merged):
    files = input(f"Enter pdf-{i + 1} file name: ")
    pdf_files.append(files)
pdf_merger(pdf_files)
print("\"PDF Merge is Successful\"")

