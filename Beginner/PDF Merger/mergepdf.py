import os
import subprocess

try:
    import PyPDF2
except ImportError:
    try:
        subprocess.run(["pip", "install", "PyPDF2"])
        import PyPDF2

    except Exception as e:
        exit(1)

def merge_pdfs(input_folder, output_file, file_order=None):

    pdf_merger = PyPDF2.PdfMerger()
    pdf_files = [file for file in os.listdir(input_folder) if file.lower().endswith(".pdf")]
    
    if file_order:
        pdf_files.sort(key=lambda x: file_order.index(x) if x in file_order else len(file_order) + pdf_files.index(x))
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        pdf_merger.append(pdf_path)
    
    with open(output_file, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)

if __name__ == "__main__":
    input_folder = input("Enter the folder location containing PDFs: ")
    output_file = input_folder+".pdf"

    merge_pdfs(input_folder, output_file)
