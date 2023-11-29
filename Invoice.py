import json
import vertexai
import os
from vertexai.language_models import TextGenerationModel
from pymongo import MongoClient
import pandas as pd
import csv
from pdf_database_tables import cursor, conn

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Vertex1.json"
vertexai.init(project="fluted-anthem-402505", location="us-central1")
model = TextGenerationModel.from_pretrained("text-bison")
parameters = {
    "max_output_tokens": 2048,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 30
}


def DARYINV(text, file, filename):
    """
   :param text: the text extracted from the PDF through Document AI
   :param filename: the pdf name
   :param file: The exact filePath where the pdf is located
   :return: the extracted json information from the Palm2.0 model
   """
    response = model.predict("""
    You are fully trained document reader. You are trained only on Logistic's PDF's.
    You are Trained extraction bot, extract all the information with 100% accuracy.
    you have an inbuilt json decoder which can format the output in a valid json.
    {
    "Invoice_date" : "",
    "Invoice_number" : "",
    "Bill_to" : {},
    "Ship_Via" : {},
    "Ship_to" : {},
    "Remit_to" : "",
    "Items" : [
    {
    "Quantity" : "",
    "Description" : "",
    "Rate" : "",
    "Amount" : "",
    }
    ]
    "Total_Amount" : "",
    "Balance_Due" : "",
    "Ref_number" : ""
    }
    you are trained to extract only the above information with out missing any keys.
    if there are any null values do not present them in the output.
    remove all the spaces in the output.
    Present the output in the valid json format.
    """+text, **parameters)
    # print(response.text)

    data = response.text
    opening_brace_index = data.find('{')
    # Extract the content starting from the opening brace '{'
    if opening_brace_index != -1:
        text = data[opening_brace_index:].replace("```", "")
    else:
        print("Opening brace '{' not found in the JSON data.")
    data = json.loads(text)
    connection = MongoClient("mongodb+srv://Pranay:Pranay%409671610@pdfextraction.mj0vgph.mongodb.net/")
    mydatabase = connection['PDFExtraction']
    record = data
    rec = mydatabase.Invoice.insert_one(record)
    # filename = filename.rsplit('.', maxsplit=1)[0]
    df = pd.DataFrame.from_dict(data, orient='index').T
    df['uuid'] = filename
    # df['filepath'] = file
    headers = ['Invoice_date', 'Invoice_number', 'Bill_to', 'Ship_to', 'Remit_to', 'Items', 'Total_Amount',
               'Balance_Due', 'Ref_number', 'uuid']
    for i in headers:
        if i not in df.columns:
            df[i] = ''
    df = df[headers]
    df.to_csv('invoice.csv', index=False)
    sql = """
        INSERT INTO pdfextraction.invoice (
        Invoice_date, Invoice_number, Bill_to, Ship_to,
        Remit_to, Items, Total_Amount, Balance_Due,
        Ref_number, uuid
        )
        VALUES (
            %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s
        )
    """
    try:
        # Open the CSV file and read data
        with open('invoice.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # This skips the 1st row which is the header.
            for record in reader:
                cursor.execute(sql, record)
                conn.commit()
    except Exception as e:
        print("Failed to insert Invoice data into SQL DataBase Error from Invoice Module.")
    return data
