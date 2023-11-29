import shutil
import json
import vertexai
import os
from vertexai.language_models import TextGenerationModel
from pymongo import MongoClient
import pandas as pd
import csv
from pdf_database_tables import cursor, conn

# Logging into GCS with respective credentials from the Vertex.json file .
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Vertex1.json"
vertexai.init(project="fluted-anthem-402505", location="us-central1")
model = TextGenerationModel.from_pretrained("text-bison")
parameters = {
    "max_output_tokens": 2048,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 30
}


def WEIGHTTICKET(text, file, filename):
    """
   :param text: the text extracted from the PDF through Document AI
   :param filename: the pdf name
   :param file: The exact filePath where the pdf is located
   :return: the extracted json information from the Palm2.0 model
   """
    # base_dir = "Classification"
    #
    # if not os.path.exists(base_dir):
    #     os.mkdir(base_dir)

    response = model.predict("""
    You are fully trained document reader. You are trained only on Logistic's PDF's.
    You are Trained extraction bot, extract all the information with 100% accuracy.
    you have an inbuilt json decoder which can format the output in a valid json.
    {
    "vendor_address" : "",
    "ticket_number" : "",
    "truck_number" : "",
    "po_number" : "",
    "customer_name" : {},
    "customer_address" : "",
    "product" : "",
    "date_out" : "",
    "time_out" : "",
    "date_in" : "",
    "time_in" : "",
    "gross_weight" : "",
    "tare_weight" : "",
    "net_weight" : "",
    "quantity" : ""
    }
    if there are any null values do not present them in the output.
    remove all the spaces in the output.
    Present the output in the valid json format.
    """ + text, **parameters)

    data = response.text
    opening_brace_index = data.find('{')
    # Extract the content starting from the opening brace '{'
    if opening_brace_index != -1:
        text = data[opening_brace_index:].replace("```", "")
    else:
        print("Opening brace '{' not found in the JSON data.")
    data = json.loads(text)
    # Establishing connection
    connection = MongoClient("mongodb+srv://Pranay:Pranay%409671610@pdfextraction.mj0vgph.mongodb.net/")
    # Creating the database
    mydatabase = connection['PDFExtraction']
    record = data
    rec = mydatabase.WEIGHTTICKET.insert_one(record)
    # filename = filename.rsplit('.', maxsplit=1)[0]
    df = pd.DataFrame.from_dict(data, orient='index').T
    df['uuid'] = filename
    # df['filepath'] = file
    headers = ['vendor_address', 'ticket_number', 'truck_number', 'po_number', 'customer_name', 'customer_address',
               'product', 'date_out', 'time_out', 'date_in', 'time_in', 'gross_weight', 'tare_weight',
               'net_weight', 'quantity', 'uuid']
    for i in headers:
        if i not in df.columns:
            df[i] = ''
    df = df[headers]
    df.to_csv('weightticket.csv', index=False)
    # Define the SQL query with backticks for column names
    sql = """
       INSERT INTO pdfextraction.weightticket (
       vendor_address, ticket_number, truck_number, po_number,
       customer_name, customer_address, product, date_out,
       time_out, date_in, time_in, gross_weight,
       tare_weight, net_weight, quantity, uuid
       )
       VALUES (
           %s, %s, %s, %s,
           %s, %s, %s, %s,
           %s, %s, %s, %s,
           %s, %s, %s, %s
       )
    """
    try:
        # Open the CSV file and read data
        with open('weightticket.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # This skips the 1st row which is the header.
            for record in reader:
                cursor.execute(sql, record)
                conn.commit()
    except Exception as e:
        print("Failed to insert Weightticket data into SQL DataBase Error from the WeightTicket Module.")
    return data

