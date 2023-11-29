# Importing necessary libraries
from Mail_marking_as_read import mark_as_read
from database_tables import create_tables, cursor, conn
from download_attachments import download_attachment
from settings import gmail_authenticate, token
from threadid import thread
import shutup
from dateutil import parser
import time

shutup.please()
try:
    def extractor():
        """Function to get latest messages and send it to the process accordingly"""

        # get the Gmail API service
        service = gmail_authenticate(token)
        # Creating the database tables if not exists
        create_tables()

        # Retrieving the latest email datetime from a database
        sql = '''SELECT * FROM email_inference'''
        cursor.execute(sql)
        data = cursor.fetchall()

        if not data:
            # Getting 10 gmails
            list_of_threads = thread(maxResults=10)
            message = service.users().messages().get(userId='me', id=list_of_threads[0]['id']).execute()
            headers = message['payload']['headers']
            for header in headers:
                name = header['name']
                value = header['value']
                if name.lower() == 'date':
                    date = value
            latest_email_datetime = date
            for index in list_of_threads[::-1]:
                message = service.users().messages().get(userId='me', id=index['id']).execute()
                if 'attachmentId' in message['payload']['parts'][0]['body'] or 'attachmentId' in \
                        message['payload']['parts'][1]['body']:
                    attachments = True
                else:
                    attachments = False

                if attachments:
                    # Downloading Attachments
                    message = service.users().messages().get(userId='me', id=index['id']).execute()
                    print(download_attachment(message['id']))
                    mark_as_read(message['id'], service)
            # parsing the datetime from email datetime using dateutil library
            date = parser.parse(latest_email_datetime)

            # converting the GMT time to UNIX time
            date = time.mktime(date.timetuple())

            # Inserting the last email received datetime
            sql = '''INSERT INTO email_inference(last_email_datetime, domain_name) VALUES(%s , 'gmail')'''
            cursor.execute(sql, (int(date),))

        else:
            # Last extracted mail's datetime
            last_email_datetime = data[0][0]
            try:
                # Getting latest emails
                list_of_threads = thread(date=last_email_datetime)
                message = service.users().messages().get(userId='me', id=list_of_threads[0]['id']).execute()
                headers = message['payload']['headers']
                for header in headers:
                    name = header['name']
                    value = header['value']
                    if name.lower() == 'date':
                        date = value
                latest_email_datetime = date
                if list_of_threads:
                    for index in list_of_threads['messages'][::-1]:
                        message = service.users().messages().get(userId='me', id=index['id']).execute()
                        if 'attachmentId' in message['payload']['parts'][0]['body'] or 'attachmentId' in \
                                message['payload']['parts'][1]['body']:
                            attachments = True
                        else:
                            attachments = False

                        if attachments:
                            # Downloading Attachments
                            message = service.users().messages().get(userId='me', id=index['id']).execute()
                            print(download_attachment(message['id']))
                            mark_as_read(message['id'], service)

                    # parsing the datetime from email datetime using dateutil library
                    date = parser.parse(latest_email_datetime)

                    # converting the GMT time to UNIX time
                    unixdate = time.mktime(date.timetuple())

                    sql = "UPDATE email_inference SET last_email_datetime = %s,email_datetimes = %s WHERE last_email_datetime " \
                          "= %s"
                    cursor.execute(sql, (int(unixdate), str(latest_email_datetime), last_email_datetime,))

            except Exception as e:
                print(e)
                pass
except Exception as e:
    print("PDF Downloading from the Email is Failed.")