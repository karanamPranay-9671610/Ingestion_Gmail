import os
from PyPDF2 import PdfReader, PdfWriter
import glob

def split():
    """
    In this function we are going to split the Multipages pdf into single page pdf using PyPDF library.
    Bcz PyPDF have in built function to split every page.
    The pdf which are there in Base_folder will get separated into single page pdf, and they will be created at Split Folder.
    the main file will be removed from the base folder the pdf pages are separated.
    """
    try:
        files = glob.glob(os.path.join(os.getcwd(), 'Base_Folder', '*.pdf'))

        for pdf_path in files:
            with open(pdf_path, 'rb') as f:
                reader = PdfReader(f)
                folder_path = os.path.join(os.getcwd(), 'Split Folder')
                for page_num, selected_page in enumerate(reader.pages):
                    writer = PdfWriter()
                    writer.add_page(selected_page)
                    output_filename = os.path.join(folder_path, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_page_{page_num + 1}.pdf")

                    with open(output_filename, 'wb') as out:
                        writer.write(out)

                    print(f"Created a PDF: {output_filename}")
            os.remove(pdf_path)
        return None
    except Exception as e :
        print("The Splitting of the PDF is Failed in Splitting Module")
