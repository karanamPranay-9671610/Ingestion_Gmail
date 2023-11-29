from ClassificationModel import model
import os
import shutil
from documentAI import docAI
try:
    def pdf_segregate(file):
        print(f"Classifying {file}")
        text = docAI(file)
        pdf_type = model(text)
        pdf_type = pdf_type.strip().lower()

        if pdf_type == "bol":
            folder_path = os.getcwd() + "\Classification\/bill of lading"
            shutil.move(file, folder_path)

        elif pdf_type == "weight ticket":
            folder_path = os.getcwd() + "\Classification\/Weight Ticket"
            shutil.move(file, folder_path)

        elif pdf_type == "cash receipt":
            folder_path = os.getcwd() + "\Classification\/cash receipt"
            shutil.move(file, folder_path)

        elif pdf_type == "invoice" or pdf_type == "drayinv":
            folder_path = os.getcwd() + "\Classification\/DrayInv"
            shutil.move(file, folder_path)

        elif pdf_type == "lumper":
            folder_path = os.getcwd() + "\Classification\/Lumper"
            shutil.move(file, folder_path)

        elif pdf_type == "corresp":
            folder_path = os.getcwd() + "\Classification\/Corresp"
            shutil.move(file, folder_path)

        else:
            folder_path = os.getcwd() + "\Classification\/Attention"
            shutil.move(file, folder_path)  # MOVE THE FILE TO RESPECTIVE FOLDER PATH
except Exception as e:
    print("Classification of the PDF got Failed in Processor Module")
