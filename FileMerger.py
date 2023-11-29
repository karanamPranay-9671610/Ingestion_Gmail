import os
import re
import PyPDF2

def pdf_merger(directories):
    for input_directory, output_directory in directories.items():
        pdf_dict = {}
        os.makedirs(output_directory, exist_ok=True)
        for filename in os.listdir(input_directory):
            if filename.endswith(".pdf"):
                base_name = re.sub(r'_page_\d+', '', filename)
                pdf_file_path = os.path.join(input_directory, filename)
                if base_name not in pdf_dict:
                    pdf_dict[base_name] = [pdf_file_path]
                else:
                    pdf_dict[base_name].append(pdf_file_path)

        for base_name, pdf_files in pdf_dict.items():
            pdf_writer = PyPDF2.PdfWriter()

            for pdf_file_path in pdf_files:
                pdf_reader = PyPDF2.PdfReader(pdf_file_path)
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)

            output_file = os.path.join(output_directory, f'{base_name}')
            with open(output_file, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

            for pdf_file_path in pdf_files:
                os.remove(pdf_file_path)
directories = {"Classification\/bill of lading": "Final\/Bill of Lading", "Classification\/Corresp": "Final\/Corresp", "Classification\/DrayInv": "Final\/DrayInv", "Classification\/cash receipt": "Final\/CashReceipt", "Classification\/Lumper": "Final\/Lumper", "Classification\/Weight Ticket": "Final\/WeightTicket"}
pdf_merger(directories)
