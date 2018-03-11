from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

import scheduleSoupToJSON as soupJSON
import JSONtoDatetime as JSONdt

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_id.json'
APPLICATION_NAME = 'KroCal'

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
                                   'calendar-python-quickstart.json')

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

def main():
    # 2014-04-10T00:00:00.000
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build("calendar","v3",http=http)

    soupJSON.makeJSON(args = "") # scrape sched, make soup, dump to json
    datesdict = JSONdt.schedJSONToDT("hours.json") # format json and turn it into a dict
    for key in datesdict.keys():
        print(f"Start: {key}, End: {datesdict[key]}")
        myEvent = {
            "summary":"Work",
            "start":{
                "dateTime":f"{key}","timeZone":"America/Chicago",
            },
            "end":{
            "dateTime":f"{datesdict[key]}","timeZone":"America/Chicago"
            }
        }
        event = service.events().insert(calendarId="primary",body=myEvent).execute()
    os.remove("hours.json") # delete the json file
    print("Done!")

if __name__ == "__main__": main()
