import os

temp = "Base_Folder"
base_dir = "Classification"
base_dir1 = "Final"
temp_path = os.getcwd() + "\Classification\/"
temp_path1 = os.getcwd() + "\Final\/"

def create_folders():

    if not os.path.exists(temp):
        os.makedirs(temp)

    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    if not os.path.exists(base_dir1):
        os.makedirs(base_dir1)

    if not os.path.exists(temp_path + "bill of lading"):
        os.makedirs(temp_path + "bill of lading")

    if not os.path.exists(temp_path1 + "Bill of Lading"):
        os.makedirs(temp_path1 + "Bill of Lading")

    if not os.path.exists(temp_path + "cash receipt"):
        os.makedirs(temp_path + "cash receipt")

    if not os.path.exists(temp_path1 + "CashReceipt"):
        os.makedirs(temp_path1 + "CashReceipt")

    if not os.path.exists(temp_path + "Corresp"):
        os.makedirs(temp_path + "Corresp")

    if not os.path.exists(temp_path1 + "Corresp"):
        os.makedirs(temp_path1 + "Corresp")

    if not os.path.exists(temp_path + "DrayInv"):
        os.makedirs(temp_path + "DrayInv")

    if not os.path.exists(temp_path1 + "DrayInv"):
        os.makedirs(temp_path1 + "DrayInv")

    if not os.path.exists(temp_path + "Lumper"):
        os.makedirs(temp_path + "Lumper")

    if not os.path.exists(temp_path1 + "Lumper"):
        os.makedirs(temp_path1 + "Lumper")

    if not os.path.exists(temp_path + "Weight Ticket"):
        os.makedirs(temp_path + "Weight Ticket")

    if not os.path.exists(temp_path1 + "WeightTicket"):
        os.makedirs(temp_path1 + "WeightTicket")

    if not os.path.exists(temp_path + "Attention"):
        os.makedirs(temp_path + "Attention")

    if not os.path.exists("Split Folder"):
        os.makedirs("Split Folder")

    return None
create_folders()