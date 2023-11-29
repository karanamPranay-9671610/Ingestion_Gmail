# # # # import pandas as pd
# # # # import csv
# # # # from database_tables import cursor, conn
# # # # user_dict = {
# # # #     'Invoice date': '3/16/2023',
# # # #     'Invoice number': '10154813',
# # # #     'Bill to': {
# # # #         'Name': 'Bairgain Furniture Warehouse',
# # # #         'Address': '3401 Tomahawk Dr.\nColumbus, GA 31907'
# # # #     },
# # # #     'Ship to': {
# # # #         'Name': 'Bairgain Furniture Warehouse',
# # # #         'Address': '3731 Macon Rd.\nColumbus, GA 31907'
# # # #     },
# # # #     'Remit to': 'Affordable Furniture Mfg. Co. Inc.\nPO Box 770299\nMemphis, TN 38177-0299',
# # # #     'Items': [
# # # #         {'Quantity': '5.0000', 'Description': '2450-SEQA\n2450-Recliner Sequoina Ash', 'Rate': '160.0000', 'Amount': '800.00'},
# # # #         {'Description': 'SSC\nSales Surcharge', 'Amount': '208.00'}
# # # #     ],
# # # #     'Total Amount': '1,008.00',
# # # #     'Balance Due': None,
# # # #     'Ref number': None
# # # # }
# # # #
# # # # # Create a DataFrame and transpose it
# # # # df = pd.DataFrame.from_dict(user_dict, orient='index').T
# # # # df.to_csv('invoice.csv', index=False)
# # # #
# # # #
# # # # # Open the CSV file and read data
# # # # with open('invoice.csv', mode='r') as csv_file:
# # # #     csv_reader = csv.reader(csv_file)
# # # #     header = next(csv_reader)  # Skip the header row
# # # #
# # # #     for row in csv_reader:
# # # #         # Define the SQL query with backticks for column names
# # # #         sql = """
# # # #             INSERT INTO invoice (
# # # #                 `Invoice date`, `Invoice number`, `Bill to`, `Ship to`,
# # # #                 `Remit to`, `Items`, `Total Amount`, `Balance Due`, `Ref number`
# # # #             )
# # # #             VALUES (
# # # #                 %s, %s, %s, %s, %s, %s, %s, %s, %s
# # # #             )
# # # #         """
# # # #
# # # #         # Execute the SQL query with the row data
# # # #         cursor.execute(sql, tuple(row))
# # # #         conn.commit()
# # # #
# # # import os
# # # import time
# # #
# # # import pandas as pd
# # # data = {'text': ['i', 'am', 'pranay']}
# # # df = pd.DataFrame(data)
# # # result = ' '.join(df['text'])
# # # print(result)
# # import uuid
# # import os
# # import glob
# # import pandas as pd
# # from faker import Faker
# # import random
# # def conversionUUID():
# #     def rename_pdf_with_uuid(file_path):
# #         new_file_path = os.path.join(os.path.dirname(file_path), str(uuid.uuid4()) + '.pdf')
# #         os.rename(file_path, new_file_path)
# #
# #     folder_path = os.getcwd() + "/Base_Folder/"
# #     file_pattern = "*.pdf"
# #     file_list = glob.glob(folder_path + '/' + file_pattern)
# #     for i in file_list:
# #         new_file_path = rename_pdf_with_uuid(i)
# #     return None
# # # conversionUUID()
# # wt_file_list = ['17e040f8-9afb-414c-8cf1-3429aa3c1c81.pdf', '2692240a-a931-4248-b040-cae39660e897.pdf', '60463259-dc30-455a-be40-ea5b6d490f77.pdf', '6bde8ba9-8af3-4b09-8453-8cfc413bbcfc.pdf', '9d3877f0-6ad8-43fe-a189-febac6464e42.pdf', 'c26a4b77-a423-4923-b4e6-4c5f6470427c.pdf', 'c88682ff-782d-459d-8c7d-6f657b749004.pdf', 'd0be430e-81c6-4732-b9eb-108df8d6b4d5.pdf']
# # fake = Faker()
# # random.seed(42)
# # common_commodities = ['Electronics', 'Clothing', 'Automotive Parts', 'Machinery', 'Food Products', 'Furniture', 'Medical Supplies', 'Chemicals', 'Textiles']
# # num_records = 300
# # data = {
# #     'Date_In': [fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S') for _ in range(num_records)],
# #     'Date_Out': [fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S') for _ in range(num_records)],
# #     'PO_Number': [f'{random.randint(1000000, 9999999)}' for _ in range(num_records)],
# #     'Vendor_Address': [fake.city() + ', ' + random.choice(['TX', 'IL', 'NC', 'WI', 'Dallas']) for _ in range(num_records)],
# #     'Customer_Name': [fake.company() for _ in range(num_records)],
# #     'Product_Name': [random.choice(common_commodities) for _ in range(num_records)],
# #     'Ticket_Number': [f'{random.randint(100000, 999999)}' for _ in range(num_records)],
# #     'Truck_Number': [f'{random.randint(10000, 99999)}' for _ in range(num_records)],
# #     'Gross_Weight': [round(random.uniform(5000, 20000), 2) for _ in range(num_records)],
# #     'Tare_Weight': [round(random.uniform(1000, 5000), 2) for _ in range(num_records)],
# #     'Net_Weight': [0.0] * num_records,  # Initialize to 0.0 for now
# #     'Quantity': [random.randint(1, 100) for _ in range(num_records)],
# #     'UUID': [random.choice(wt_file_list) for _ in range(num_records)],
# # }
# # for i in range(num_records):
# #     data['Net_Weight'][i] = round(data['Gross_Weight'][i] - data['Tare_Weight'][i], 2)
# # df_weight_ticket = pd.DataFrame(data)
# # df_weight_ticket.to_csv("weightticket_fake_data.csv")
# # print(df_weight_ticket)
# import fitz  # PyMuPDF
#
# def pdf_to_images(pdf_path, image_path_prefix):
#     doc = fitz.open(pdf_path)
#     for page_number in range(doc.page_count):
#         page = doc[page_number]
#         image = page.get_pixmap()
#         image.save(image_path_prefix + f"_page_{page_number + 1}.png")
#
#     doc.close()
#
# # Usage
# pdf_to_images("Base_Folder/cropped_image.pdf", "cropped_image")
import uuid
import os
import glob

temp_folder = os.getcwd() + "/Base_Folder"
file_pattern = "*.pdf"
def rename_pdfs_with_uuid(folder_path, file_pattern='*.pdf'):
    """
    :param folder_path: The Folder which the file names in that folder to be renamed with uuid.
    :param file_pattern: which type of extension files need to be change the name of the files.
    In this function first we are taking all the files with the *.pdf then renaming them with uuid4
    This could generate the unique identifier name for each and every pdf.
    """
    [os.rename(pdf, os.path.join(os.path.dirname(pdf), str(uuid.uuid4()) + '.pdf')) for pdf in glob.glob(os.path.join(folder_path, file_pattern))]
rename_pdfs_with_uuid(temp_folder)