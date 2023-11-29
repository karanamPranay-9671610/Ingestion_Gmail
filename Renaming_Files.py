import os
def renaming():
    Main_folder = os.getcwd() + "\Final"
    for root, dirs, files in os.walk(Main_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            folder_name = os.path.basename(root)
            if folder_name == "Bill of Lading":
                folder_name = "B"
            elif folder_name == "DrayInv":
                folder_name = "I"
            elif folder_name == "WeightTicket":
                folder_name = "W"
            elif folder_name == "CashReceipt":
                folder_name = "C"
            elif folder_name == "Lumper":
                folder_name = "L"
            new_file_name = f"{folder_name}_{file_name}"
            new_file_path = os.path.join(root, new_file_name)
            os.rename(file_path, new_file_path)
            # print(f"Renamed: {file_path} to {new_file_path}")
