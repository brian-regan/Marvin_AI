
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime
import dateutil.parser
import calendar

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def GetMessage(service, user_id, msg_id):
  """Get a Message with given ID.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()
    #print(message.keys())
    subject = ""
    sender = ""
    date = ""

    headers = message['payload']['headers']

    for header in headers:
            if header['name'] == 'Subject':
                subject = header['value']

            if header['name'] == 'From':
                sender_org = header['value']
                sender = sender_org.replace("<", "(").replace(">", ")")

            if header['name'] == 'Date':
                date_org = header['value']
                date = dateutil.parser.parse(date_org)

                day = date.day
                weekday = calendar.day_name[date.weekday()]
                month = calendar.month_name[date.month]
                date_form = "{0} {1} {2}".format(weekday, day, month)
    
    speech = "On {0}, {1} sent: {2}".format(date_form, sender, subject)

    return speech
  except errors.HttpError, error:
    print('An error occurred: {}'.format(error))



"""Get a list of Messages from the user's mailbox.
"""

from apiclient import errors


def Say_Messages():
  """List all Messages of the user's mailbox matching the query.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    query: String used to filter messages returned.
    Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

  Returns:
    List of Messages that match the criteria of the query. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate ID to get the details of a Message.
  """

  credentials = get_credentials()
  http = credentials.authorize(httplib2.Http())
  service = discovery.build('gmail', 'v1', http=http)
  user_id = 'me'
  query = 'is:unread label:important'


  try:
    response = service.users().messages().list(userId=user_id,
                                               q=query).execute()
    messages = []
    speechs = []

    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id, q=query,
                                         pageToken=page_token).execute()
      messages.extend(response['messages'])

    
    for message in messages:
        speech = GetMessage(service, user_id, message['id'])
        speechs.append(speech)

  except errors.HttpError, error:
    print('An error occurred: {}'.format(error))

  
  if not speechs:
    speechs = ["No unread emails"]
    
  return(speechs)


