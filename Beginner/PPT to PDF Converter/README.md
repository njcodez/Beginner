# PowerPoint to PDF Converter
This Python script allows you to convert PowerPoint (PPTX) files into PDF format. It leverages Microsoft PowerPoint to perform the conversion. By following the instructions below, you can easily convert your PPTX files to PDFs.

## Prerequisites

Before using this script, make sure you have the following:

Python: You need Python installed on your computer. You can download and install Python from the official website: https://www.python.org/downloads/.

comtypes Library: The comtypes library is used to interface with Microsoft PowerPoint. Install it using pip:

## Copy code
pip install comtypes
Microsoft PowerPoint: This script requires Microsoft PowerPoint to be installed on your computer as it utilizes PowerPoint for the conversion process. Ensure that PowerPoint is available on your system.

##Usage
Clone or Download the Repository: Clone this repository to your local machine or download the script file to a directory of your choice.

## Run the Script:

Open a terminal or command prompt.

Navigate to the directory where you saved the script.

Run the script by executing the following command:

## Copy code
python ppt2pdf.py
Follow the On-Screen Instructions:

You will be prompted to enter the location of the folder containing your PPTX files.
Next, specify the location where you want to save the converted PDF files.
### Conversion Process:

The script will use Microsoft PowerPoint to convert each PPTX file in the input folder to PDF format.
The PDF files will be saved in the specified output folder.
The script will display progress messages for each conversion.

#### Completion:

Once all conversions are complete, you will see the message "Conversion completed!".

## Important Notes
Ensure that you have read and write permissions for both the input and output folders.
Verify that the PPTX files you want to convert are present in the input folder.
The script utilizes Microsoft PowerPoint for conversion, so make sure it is installed and available on your system.
The script is designed to handle errors gracefully and will display error messages if any issues occur during the conversion process.

## Customization
You can modify the script to fit your specific needs. For example, you can customize the output file naming convention or add error handling specific to your environment.

# Disclaimer
This script uses Microsoft PowerPoint for the conversion process and relies on its availability and functionality. The script is provided as-is, and the accuracy and performance of the conversion depend on your system's configuration.

Please use this script responsibly and ensure that you have the necessary legal rights to convert the PPTX files you intend to process.

## Credits
This script was developed with the help of the comtypes library to interact with Microsoft PowerPoint. Credits to the authors and contributors of the comtypes library for enabling this functionality.

Feel free to use and modify this script to suit your needs. If you encounter any issues or have questions, please don't hesitate to reach out for assistance.
