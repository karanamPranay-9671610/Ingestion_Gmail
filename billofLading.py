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

def BOL(text, file, filename):
    """
    :param text: the text extracted from the PDF through Document AI
    :param filename: the pdf name
    :param file: The exact filePath where the pdf is located
    :return: the extracted json information from the Palm2.0 model
    """
    response = model.predict("""
     you are fully trained extraction bot. You are trained only on BOL documents.
    Extract all the information mentioned below.
    you have an inbuilt json decoder which can format the output in a valid json structure.
    {
    "BOL_Number":"",
    "Shipper":{},
    "BL_Number":"",
    "SW_Number":"",
    "Order_Number":"",
    "Order_Date":"",
    "Ship_Date":"",
    "Cust_PO_Number":"",
    "Ship_To":{},
    "Sold_To":{},
    "Ship_Via":"",
    "FOB" :"",
    "Trailer_No":"",
    "Seal_No":"",
    "Delivery_Address_Po":"",
    "total_quantity":"",
    "cubes":"",
    "Total_weight":"",
    "tare_weight":"",
    "Gross_Weight":"",
    "Time_In":"",
    "Time_Out":"",
    "Date":"",
    "Agent_Date":""
    } 
    if there are any null values do not present them in the output.
    remove all the spaces in the output.
    Present the output in the valid json format."""+text, **parameters)

    data = response.text
    opening_brace_index = data.find('{')

    # Extract the content starting from the opening brace '{'
    if opening_brace_index != -1:
        text = data[opening_brace_index:].replace("```", "")
    else:
        print("Opening brace '{' not found in the JSON data.")
    data = json.loads(text)
    print(data)
    connection = MongoClient("mongodb+srv://Pranay:Pranay%409671610@pdfextraction.mj0vgph.mongodb.net/")
    mydatabase = connection['PDFExtraction']
    record = data
    rec = mydatabase.BOL.insert_one(record)
    # filename = filename.rsplit('.', maxsplit=1)[0]
    df = pd.DataFrame.from_dict(data, orient='index').T
    df['uuid'] = str(filename)
    # df['filepath'] = str(file)
    headers = ['BOL_Number', 'Shipper', 'BL_Number', 'SW_Number', 'Order_Number', 'Order_Date', 'Ship_Date',
               'Cust_PO_Number', 'Ship_To', 'Sold_To', 'Ship_Via', 'FOB', 'Trailer_No', 'Seal_No',
               'Delivery_Address_Po', 'total_quantity', 'cubes', 'Total_weight', 'tare_weight', 'Gross_Weight',
               'Time_In', 'Time_Out', 'Date', 'Agent_Date', 'uuid']
    for i in headers:
        if i not in df.columns:
            df[i] = ''
    df = df[headers]
    df.to_csv('bol.csv', index=False)
    sql = """
    INSERT INTO pdfextraction.bol (
    BOL_Number, Shipper, BL_Number, SW_Number,
    Order_Number, Order_Date, Ship_Date, Cust_PO_Number,
    Ship_To, Sold_To, Ship_Via, FOB,
    Trailer_No, Seal_No, Delivery_Address_Po, total_quantity,
    cubes, Total_weight, tare_weight, Gross_Weight,
    Time_In, Time_Out, Date, Agent_Date,
    uuid
    )
    VALUES (
        %s, %s, %s, %s,
        %s, %s, %s, %s,
        %s, %s, %s, %s,
        %s, %s, %s, %s,
        %s, %s, %s, %s,
        %s, %s, %s, %s,
        %s
    )
                """
    try:
        with open('bol.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # This skips the 1st row which is the header.
            for record in reader:
                cursor.execute(sql, record)
                conn.commit()
    except Exception as e:
        print("Failed to insert BOL data in the SQL DataBase Error from billofLading Module")
    return data
