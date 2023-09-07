import os
import subprocess

try:
    import comtypes.client
except ImportError:
    try:
        subprocess.run(["pip", "install", "python-pptx"])
        subprocess.run(["pip", "install", "comtypes"])
        import comtypes.client

    except Exception as e:
        exit(1)

import os

def ppt_to_pdf(input_folder, output_folder):
    powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
    powerpoint.Visible = 1  
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".pptx"):
            pptx_path = os.path.join(input_folder, filename)
            pdf_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".pdf")
            
            try:
                presentation = powerpoint.Presentations.Open(pptx_path)
                presentation.SaveAs(pdf_path, 32)  #32 is for PDF 
                presentation.Close()
                print(f"Converted '{pptx_path}' to '{pdf_path}'")
            except Exception as e:
                print(f"Failed to convert '{pptx_path}': {e}")

    powerpoint.Quit()

if __name__ == "__main__":
    input_folder = input("Enter the PPT folder location: ")
    output_folder = input("Enter the location where you want to save the PDFs: ")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if not os.path.exists(input_folder):
        print(f"The input folder '{input_folder}' does not exist.")
    else:
        ppt_to_pdf(input_folder, output_folder)

    print("Conversion completed!")
