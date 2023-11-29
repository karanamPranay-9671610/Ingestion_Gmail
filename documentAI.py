import os
from google.api_core.client_options import ClientOptions
from google.cloud import documentai

def docAI(file):
    try:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getcwd() + '/Vertex1.json'
        PROJECT_ID = "fluted-anthem-402505"
        LOCATION = "eu"  # Format is 'us' or 'eu'
        PROCESSOR_ID = "cb8b457cd930d03f"  # Create processor in Cloud Console
        FILE_PATH = file
        MIME_TYPE = "application/pdf"

        # Instantiates a client
        docai_client = documentai.DocumentProcessorServiceClient(
            client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")
        )
        RESOURCE_NAME = docai_client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)

        # Read the file into memory
        with open(FILE_PATH, "rb") as image:
            image_content = image.read()

        # Load Binary Data into Document AI RawDocument Object
        raw_document = documentai.RawDocument(content=image_content, mime_type=MIME_TYPE)

        # Configure the process request
        request = documentai.ProcessRequest(name=RESOURCE_NAME, raw_document=raw_document)

        # Use the Document AI client to process the sample form
        result = docai_client.process_document(request=request)

        document_object = result.document
        text = document_object.text
        return text
    except Exception as e:
        print("The Classification Document AI was Failed to extract text from the PDF")
