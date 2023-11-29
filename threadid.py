import base64
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import base64

from download_attachments import download_attachment

from settings import token, gmail_authenticate

# get the Gmail API service
service = gmail_authenticate(token)


def thread(maxResults=None, date=None):
    if maxResults is not None:

        threads = service.users().threads().list(userId='me', labelIds=['INBOX'], maxResults=maxResults).execute().get(
            'threads')

        return threads

    else:

        # Modify the query to include the date and time
        query = f'in:inbox is:unread after:{int(date)}'

        threads = service.users().messages().list(userId='me', q=query).execute()

        return threads

# print(thread(maxResults=1))
# a = thread()[0]['id']
# response_json = service.users().messages().get(userId='me', id=a).execute()
# # message_body = response_json['payload']['parts'][1]['body']['data']
# # decoded_message_body = base64.urlsafe_b64decode(message_body).decode('utf-8')


# threads = thread( date = "1697964650")
# # #
# print(threads)
# response = service.users().threads().get(userId='me', id=threads['messages'][0]['threadId']).execute()
# print(response['messages'][0]['id'],'\n\n', response['messages'][0]['threadId'])


# #
# # # Get the last message in the thread
# # last_message = response['messages'][-1]
# #
# # # Retrieve and print the last message's body
# # message_body = last_message['payload']['parts'][0]['body']['data']
# # decoded_message_body = base64.urlsafe_b64decode(message_body).decode('utf-8')
#
# message = response['messages'][-1]
# headers = message['payload']['headers']
# for header in headers:
#     name = header['name']
#     value = header['value']
#     if name.lower() == 'subject':
#         print('subject  ==  ' , value)
#     elif name.lower() == 'from':
#         print('sender  ==  ', value)
#     elif name.lower() == 'date':
#         print('date  ==  ' , value)
# # Decode and extract the message body
# print(message)
# try:
#     if 'body' in message['payload']['parts'][0]:
#         # print(message['snippet'])
#         # length = message['payload']['parts'][1]
#         # print(len(message['payload']['parts']),'\n',length)
#         if 'data' in message['payload']['parts'][1]['body']:
#             body = base64.urlsafe_b64decode(message['payload']['parts'][0]['body']['data']).decode('utf-8')
#             print(body)
# except Exception as e:
#     print(e)
#
# # print(decoded_message_body)
#
# # thread()
# # for i in thread():
# #     print(i)
#
