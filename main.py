# import os
# import glob
# import multiprocessing
# from UUID import conversionUUID
# from Splitting import split
# import time
# from Conversion import convert_tiff_folder_to_pdf
# from pdf_processor import pdf_segregate
# from FileMerger import pdf_merger
# from File_Extractor import extract
#
# def process_pdf(file_path):
#     try:
#         print(f"Processing {file_path}")
#         pdf_segregate(file_path)
#     except Exception as e:
#         return (file_path, e)
#
# temp_folder = os.getcwd() + "/Base_Folder"
# convert_tiff_folder_to_pdf(temp_folder, temp_folder)
#
# def pdf_main():
#     conversionUUID()
#     split()
#     file_pattern = "*.pdf"
#     folder_path = os.getcwd() + "/Split Folder/"
#     file_list = glob.glob(folder_path + '/' + file_pattern)
#
#     num_processes = multiprocessing.cpu_count() - 5  # Use all available CPU cores
#
#     start_time = time.time()
#
#     with multiprocessing.Pool(processes=num_processes) as pool:
#         results = pool.map(process_pdf, file_list)
#
#     for result in results:
#         if isinstance(result, tuple) and len(result) == 2:
#             file_path, exception = result
#             print(f"Exception occurred while processing {file_path}: {exception}")
#
#     directories = {"Classification/bill of lading": "Final/Bill of Lading", "Classification/Corresp": "Final/Corresp", "Classification/DrayInv": "Final/DrayInv", "Classification/cash receipt": "Final/CashReceipt", "Classification/Lumper": "Final/Lumper", "Classification/Weight Ticket": "Final/WeightTicket"}
#     pdf_merger(directories)
#     pool.close()
#     pool.join()
#     extract()
#     end_time = time.time()
#     execution_time = end_time - start_time
#     print(f"Total execution time: {execution_time} seconds")
#
# if __name__ == "__main__":

#     pdf_main()
