import os
import subprocess

try:
    from pptx import Presentation
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
except ImportError:
    try:
        subprocess.run(["pip", "install", "pptx"])
        subprocess.run(["pip", "install", "reportlab"])
        from pptx import Presentation
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
    except Exception as e:
        exit(1)

def ppt_to_pdf(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".pptx"):
            pptx_path = os.path.join(input_folder, filename)
            pdf_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".pdf")

            try:
                c = canvas.Canvas(pdf_path, pagesize=letter)
                c.showPage()
                c.save()

                prs = Presentation(pptx_path)

                pdf = canvas.Canvas(pdf_path, pagesize=letter)
                for slide in prs.slides:
                    pdf.showPage()
                pdf.save()

                print(f"Converted '{pptx_path}' to '{pdf_path}'")
            except Exception as e:
                print(f"Failed to convert '{pptx_path}': {e}")

input_folder = input("Enter the PPT folder location: ")
output_folder = input("Enter the location where you want to save the PDFs: ")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

if not os.path.exists(input_folder):
    print(f"The input folder '{input_folder}' does not exist.")
else:
    ppt_to_pdf(input_folder, output_folder)

print("Conversion completed!")
