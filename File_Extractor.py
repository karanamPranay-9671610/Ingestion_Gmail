import os
import glob
from ExtractDOCAI import ExtractDocAI
from billofLading import BOL
from Invoice import DARYINV
from WeightTicket import WEIGHTTICKET
from CashReceipt import CASHRECEIPT
from Lumper import LUMPER
def extract():
    bol_folder_path = os.getcwd() + "/Final/Bill of Lading/"
    file_pattern = "*.pdf"
    bol_file_list = glob.glob(bol_folder_path + '/' + file_pattern)
    for i in bol_file_list:
        filename = os.path.basename(i)
        text = ExtractDocAI(i)
        BOL(text, i, filename)
    drayinv_folder_path = os.getcwd() + "/Final/DrayInv/"
    inv_file_list = glob.glob(drayinv_folder_path + '/' + file_pattern)
    for i in inv_file_list:
        filename = os.path.basename(i)
        text = ExtractDocAI(i)
        DARYINV(text, i, filename)
    weightticket_folder_path = os.getcwd() + "/Final/WeightTicket/"
    WT_file_list = glob.glob(weightticket_folder_path + '/' + file_pattern)
    for i in WT_file_list:
        filename = os.path.basename(i)
        text = ExtractDocAI(i)
        WEIGHTTICKET(text, i, filename)
    cashreceipt_folder_path = os.getcwd() + "/Final/CashReceipt/"
    CR_file_list = glob.glob(cashreceipt_folder_path + '/' + file_pattern)
    for i in CR_file_list:
        filename = os.path.basename(i)
        text = ExtractDocAI(i)
        CASHRECEIPT(text, i, filename)
    lumper_folder_path = os.getcwd() + "/Final/Lumper/"
    Lumper_file_list = glob.glob(lumper_folder_path + '/' + file_pattern)
    for i in Lumper_file_list:
        filename = os.path.basename(i)
        text = ExtractDocAI(i)
        LUMPER(text, i, filename)
# import os
# import glob
# from ExtractDOCAI import ExtractDocAI
# from billofLading import BOL
# from DaryInv import DARYINV
# from WeightTicket import WEIGHTTICKET
# from CashReceipt import CASHRECEIPT
# from Lumper import LUMPER
# from multiprocessing import Pool
#
# def process_file(file_path):
#     filename = os.path.basename(file_path)
#     text = ExtractDocAI(file_path)
#     return filename, text
#
# def extract():
#     bol_folder_path = os.getcwd() + "/Final/Bill of Lading/"
#     file_pattern = "*.pdf"
#     bol_file_list = glob.glob(bol_folder_path + '/' + file_pattern)
#     drayinv_folder_path = os.getcwd() + "/Final/DrayInv/"
#     inv_file_list = glob.glob(drayinv_folder_path + '/' + file_pattern)
#     weightticket_folder_path = os.getcwd() + "/Final/WeightTicket/"
#     WT_file_list = glob.glob(weightticket_folder_path + '/' + file_pattern)
#     cashreceipt_folder_path = os.getcwd() + "/Final/CashReceipt/"
#     CR_file_list = glob.glob(cashreceipt_folder_path + '/' + file_pattern)
#     lumper_folder_path = os.getcwd() + "/Final/Lumper/"
#     Lumper_file_list = glob.glob(lumper_folder_path + '/' + file_pattern)
#
#     file_list = bol_file_list + inv_file_list + WT_file_list + CR_file_list + Lumper_file_list
#
#     num_processes = 7
#     with Pool(num_processes) as pool:
#         results = pool.map(process_file, file_list)
#
#     for filename, text in results:
#         if bol_folder_path in filename:
#             BOL(text, filename, filename)
#         elif drayinv_folder_path in filename:
#             DARYINV(text, filename, filename)
#         elif weightticket_folder_path in filename:
#             WEIGHTTICKET(text, filename, filename)
#         elif cashreceipt_folder_path in filename:
#             CASHRECEIPT(text, filename, filename)
#         elif lumper_folder_path in filename:
#             LUMPER(text, filename, filename)
