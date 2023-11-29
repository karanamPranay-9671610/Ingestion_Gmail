import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pranay@9671610",
    database="pdfextraction"
)
conn.autocommit = True
cursor = conn.cursor()
conn.commit()

def create_tables():
    sql = """
        CREATE TABLE IF NOT EXISTS invoice (
            `Invoice_date` VARCHAR(255),
            `Invoice_number` VARCHAR(255),
            `Bill_to` VARCHAR(255),
            `Ship_Via` VARCHAR(255),
            `Ship_to` VARCHAR(255),
            `Remit_to` VARCHAR(255),
            `Items` VARCHAR(255),
            `Total_Amount` VARCHAR(255),
            `Balance_Due` VARCHAR(255),
            `Ref_number` VARCHAR(255),
            `uuid` VARCHAR(255)
        );
        """
    cursor.execute(sql)
    sql = """
        CREATE TABLE IF NOT EXISTS lumper(
        `load_number` VARCHAR(255),
        `date` VARCHAR(255),
        `ship_from_address` VARCHAR(255),
        `ship_to_address` VARCHAR(255),
        `transaction_fee` VARCHAR(255),
        `amount` VARCHAR(255),
        `total_paid` VARCHAR(255),
        `po_number` VARCHAR(255),
        `receipt_number` VARCHAR(255),
        `work_date` VARCHAR(255),
        `carrier` VARCHAR(255),
        `vendor` VARCHAR(255),
        `trailer_number` VARCHAR(255),
        `total_payments` VARCHAR(255),
        `uuid` VARCHAR(255)
    );
    """
    cursor.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS weightticket(
            `vendor_address` VARCHAR(255),
            `ticket_number` VARCHAR(255),
            `truck_number` VARCHAR(255),
            `po_number` VARCHAR(255),
            `customer_name` VARCHAR(255),
            `customer_address` VARCHAR(255),
            `product` VARCHAR(255),
            `date_out` VARCHAR(255),
            `time_out` VARCHAR(255),
            `date_in` VARCHAR(255),
            `time_in` VARCHAR(255),
            `gross_weight` VARCHAR(255),
            `tare_weight` VARCHAR(255),
            `net_weight` VARCHAR(255),
            `quantity` VARCHAR(255),
            `uuid` VARCHAR(255)
    );
    """
    cursor.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS cashreceipt(
        `date` VARCHAR(255),
        `paid_by` VARCHAR(255),
        `bol_po_number` VARCHAR(255),
        `trailer_number` VARCHAR(255),
        `tractor_number` VARCHAR(255),
        `location` VARCHAR(255),
        `payment_method` VARCHAR(255),
        `driver_name` VARCHAR(255),
        `service` VARCHAR(255),
        `comments` VARCHAR(255),
        `total_amount` VARCHAR(255),
        `uuid` VARCHAR(255)
    );
    """
    cursor.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS bol(
        `BOL_Number` VARCHAR(255),
        `Shipper` VARCHAR(255),
        `BL_Number` VARCHAR(255),
        `SW_Number` VARCHAR(255),
        `Order_Number` VARCHAR(255),
        `Order_Date` VARCHAR(255),
        `Ship_Date` VARCHAR(255),
        `Cust_PO_Number` VARCHAR(255),
        `Ship_To` VARCHAR(255),
        `Sold_To` VARCHAR(255),
        `Ship_Via` VARCHAR(255),
        `FOB` VARCHAR(255),
        `Trailer_No` VARCHAR(255),
        `Seal_No` VARCHAR(255),
        `Delivery_Address_Po` VARCHAR(255),
        `total_quantity` VARCHAR(255),
        `cubes` VARCHAR(255),
        `Total_weight` VARCHAR(255),
        `tare_weight` VARCHAR(255),
        `Gross_Weight` VARCHAR(255),
        `Time_In` VARCHAR(255),
        `Time_Out` VARCHAR(255),
        `Date` VARCHAR(255),
        `Agent_Date` VARCHAR(255),
        `uuid` VARCHAR(255)
        );
        """
    cursor.execute(sql)

create_tables()