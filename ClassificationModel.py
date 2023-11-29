import os
import vertexai
from vertexai.language_models import TextGenerationModel
def model(text):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Vertex1.json"
    vertexai.init(project="fluted-anthem-402505", location="us-central1")

    model_prediction = TextGenerationModel.from_pretrained("text-bison")
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 2048,
        "top_p": 0.8,
        "top_k": 30
    }
    prompt = """
    You are a full trained document summariser, you are trained to identify all the logistics documents.
    The output should only be the document type.
    Identify the document type with the help of the following keys in the document.
    If the document has billing for the services offered to trucks classify them as "Cash Receipt" document.//washout 
    bills, fuel bills, any service related bills.
    If the document is intended to show the truck weight or gross weight classify it as "Weight Ticket" document.//gross 
    weight, truck weight, empty truck
    if the document Consists of "Invoice",Invoice Date","Reason for impound","Impound Invoice" as headers classify the document as "Invoice" document.
    If the document has load details and linehaul details classify them as "Draylnv" document.
    if the document has the header with Invoice classify them as "Invoice" document.
    if the document has the any of the following keywords "Relay" or "Capstone Logistics" classify the document as "Lumper" document.
    If the document is related to loading and unloading charges then classify the same as "Lumper" document.
    If the document has PACKING LIST as a header then classify the same a "BOL" document.
    If the document has tables and if the tables has headers related to BOL then classify as "BOL" document
    If the document has table having Origin code or Country of Origin or orig Curr ECCN Code as one of the headers then 
    classify it as BOL document.
    If the document is in foreign language classify them under BOL document.
    If the document has FLEET LTL NNETWORK MANIFEST classify them as BOL document.
    If the document has information related to Truck seal then process the same as "BOL" document.
    If the document has strip bill as the header then mark the same as a "BOL" document.
    If the document has Bill of Lading as document header or if BOL number is printed in the document, classify them as "BOL" document.
    If the document has only the following key words "Carrier Confirmation", "Driving Directions","Terms and Conditions",//
    "QuickPay","Cash Advances","Rate Agreement","Carrier Services","Detention Payment","Carrier Acceptance" "ATTN","Accounts Payable Manager" or if the//
    documents are identified as letters, Payment related requests classify them as "Corresp" documents.
    if the document consists of "Carrier Services","Comments","Rate Agreement","Detention Payment","Submitting Required Documents at EMPTY CALL","Shipper ID", "Cash Advances","QuickPay","Paperwork" or identified as an "letter" Classify the document as "Corresp" document.
    If the document has address and other load information if the key words related to Corresp is present then mark them as Corresp documents only.
    """
    # Getting response from the model
    response = model_prediction.predict(prompt + text, **parameters)
    return response.text
