import os
import glob
import multiprocessing
import uuid
from Splitting import split
import time
from Conversion import convert_tiff_folder_to_pdf
from pdf_processor import pdf_segregate
from FileMerger import pdf_merger
from Invoice import DARYINV
from billofLading import BOL
from Lumper import LUMPER
from WeightTicket import WEIGHTTICKET
from CashReceipt import CASHRECEIPT
from ExtractDOCAI import ExtractDocAI
from Renaming_Files import renaming
from Email_extraction import extractor

extractor()     # Extracting all the PDF's from the emails
def process_pdf(file_path):
    try:
        print(f"Processing {file_path}")
        pdf_segregate(file_path)
    except Exception as e:
        return (file_path, e)

temp_folder = os.getcwd() + "\Base_Folder"
file_pattern = "*.pdf"

convert_tiff_folder_to_pdf(temp_folder, temp_folder)    # This Function helps us to convert if there are any .tif file in the respective folder they will be converted into .pdf

def rename_pdfs_with_uuid(folder_path, file_pattern='*.pdf'):
    """
    :param folder_path: The Folder which the file names in that folder to be renamed with uuid.
    :param file_pattern: which type of extension files need to be change the name of the files.
    In this function first we are taking all the files with the *.pdf then renaming them with uuid4
    This could generate the unique identifier name for each and every pdf.
    """
    [os.rename(pdf, os.path.join(os.path.dirname(pdf), str(uuid.uuid4()) + '.pdf')) for pdf in glob.glob(os.path.join(folder_path, file_pattern))]
rename_pdfs_with_uuid(temp_folder)

def pdf_main():
    split()
    file_pattern = "*.pdf"
    folder_path = os.getcwd() + "\Split Folder\/"
    file_list = glob.glob(folder_path + file_pattern)

    num_processes = 7
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(process_pdf, file_list)

    for result in results:
        if isinstance(result, tuple) and len(result) == 2:
            file_path, exception = result
            print(f"Exception occurred while processing {file_path}: {exception}")

    directories = {"Classification\/bill of lading": "Final\/Bill of Lading", "Classification\/Corresp": "Final\/Corresp", "Classification\/DrayInv": "Final\/DrayInv", "Classification\/cash receipt": "Final\/CashReceipt", "Classification\/Lumper": "Final\/Lumper", "Classification\/Weight Ticket": "Final\/WeightTicket"}
    pdf_merger(directories)
    pool.close()
    pool.join()
#     renaming()  # Which will rename the PDF's Add the Prefix letter of the type of the PDF.
# bol_folder_path = os.getcwd() + "/Final/Bill of Lading/"
# bol_file_list = glob.glob(bol_folder_path + file_pattern)
# drayinv_folder_path = os.getcwd() + "/Final/DrayInv/"
# inv_file_list = glob.glob(drayinv_folder_path + file_pattern)
# lumper_folder_path = os.getcwd() + "/Final/Lumper/"
# lumper_file_list = glob.glob(lumper_folder_path + file_pattern)
# weightticket_folder_path = os.getcwd() + "/Final/WeightTicket/"
# weightticket_file_list = glob.glob(weightticket_folder_path + file_pattern)
# cashreceipt_folder_path = os.getcwd() + "/Final/CashReceipt/"
# cashreceipt_file_list = glob.glob(cashreceipt_folder_path + file_pattern)
#
# def bol_process_pdf(file):
#     filename = os.path.basename(file)
#     text = ExtractDocAI(file)
#     output = BOL(text, file, filename)
#     print(output)
#
# def bol_main():
#     num_processes = 7
#     with multiprocessing.Pool(processes=num_processes) as pool:
#         results = pool.map(bol_process_pdf, bol_file_list)
#     pool.close()
#     pool.join()
#
# def inv_process_pdf(file):
#     filename = os.path.basename(file)
#     text = ExtractDocAI(file)
#     output = DARYINV(text, file, filename)
#     print(output)
#
# def inv_main():
#     num_processes = 7
#     with multiprocessing.Pool(processes=num_processes) as pool:
#         results = pool.map(inv_process_pdf, inv_file_list)
#     pool.close()
#     pool.join()
#
# def lumper_process_pdf(file):
#     filename = os.path.basename(file)
#     text = ExtractDocAI(file)
#     output = LUMPER(text, file, filename)
#     print(output)
#
# def lumper_main():
#     num_processes = 7
#     with multiprocessing.Pool(processes=num_processes) as pool:
#         results = pool.map(lumper_process_pdf, lumper_file_list)
#     pool.close()
#     pool.join()
#
# def cashreceipt_process_pdf(file):
#     filename = os.path.basename(file)
#     text = ExtractDocAI(file)
#     output = CASHRECEIPT(text, file, filename)
#     print(output)
#
# def cashreceipt_main():
#     num_processes = 7
#     with multiprocessing.Pool(processes=num_processes) as pool:
#         results = pool.map(cashreceipt_process_pdf, cashreceipt_file_list)
#     pool.close()
#     pool.join()
#
# def weightticket_process_pdf(file):
#     filename = os.path.basename(file)
#     text = ExtractDocAI(file)
#     output = WEIGHTTICKET(text, file, filename)
#     print(output)
#
# def weightticket_main():
#     num_processes = 7
#     with multiprocessing.Pool(processes=num_processes) as pool:
#         results = pool.map(weightticket_process_pdf, weightticket_file_list)
#     pool.close()
#     pool.join()


if __name__ == "__main__":
    start_time = time.time()
    pdf_main()
    # p1 = multiprocessing.Process(target=bol_main)
    # p2 = multiprocessing.Process(target=inv_main)
    # p3 = multiprocessing.Process(target=lumper_main)
    # p4 = multiprocessing.Process(target=weightticket_main)
    # p5 = multiprocessing.Process(target=cashreceipt_main)
    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # p5.start()
    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    # p5.join()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Total execution time: {execution_time} seconds")
