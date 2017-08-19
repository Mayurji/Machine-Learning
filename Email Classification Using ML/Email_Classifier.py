from __future__ import print_function
import httplib2
import os
import re
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from DateTime import DateTime
import base64
import email
import csv
import pandas as pd


global mail_SNIPPET
global mail_MAILID
global mail_SUBJECT
global mail_SPAM
global mail_dateTime
global emailClassification


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly https://www.googleapis.com/auth/gmail.modify'
CLIENT_SECRET_FILE = '/Users/XXXXXX/Documents/Google Gmail API /client_secret.json'
APPLICATION_NAME = 'Email_Classifier'

mail_SPAM = []
mail_SNIPPET = []
mail_MAILID = []
mail_SUBJECT = []
mail_dateTime = []


class GeneratingDataSet():
    def createCSV(self):
        path = '/Users/XXXXXXXX/Documents/Google Gmail API /'
        fileName = 'EmailClass.csv'
        with open(path+fileName,'w') as f:
            w = csv.writer(f)
            list1 = ["Date"] + ["SPAM"] + ["SNIPPET"] + ["MAIL_ID"] +["SUBJECT"]
            w.writerow(list1)
            f.close()

    def DateTimeFormat(self,time):
        dayhours = ['0','1','2','3','4','5','6','7','8','9']
        months = ['1','2','3','4','5','6','7','8','9']
        days = ['1','2','3','4','5','6','7','8','9']
        minus = '-'
        addition = '+'
        global x 
        if minus in time:
            splittz = time.split(minus)
            y = DateTime(splittz[0])
            x = [y.parts()]
            month = str(x[0][1])
            day = str(x[0][2])
            hours = str(x[0][3])
            if month in months:
                month = '0'+month
                #return month
            if day in days:
                day = '0'+day
                #return day
            if hours in dayhours:
                hours = '0'+hours
                #return hours
            return int(str(x[0][0])+month+day+hours) 
        elif addition in time:
            splitTZ = time.split('+')
            y = DateTime(splitTZ[0])
            x = [y.parts()]
            month = str(x[0][1])
            day = str(x[0][2])
            hours = str(x[0][3])
            if str(x[0][1]) in months:
                month = '0'+month
                #return month
            if str(x[0][2]) in days:
                day = '0'+day
                #return day
            if str(x[0][3]) in dayhours:
                hours = '0'+hours
                #return hours
            return int(str(x[0][0])+month+day+hours)

    def nextPage(self,results,service):
        if 'nextPageToken' in results:
            messages = []
            page_token = results['nextPageToken']
            response = service.users().messages().list(userId='me',pageToken=page_token,includeSpamTrash=True).execute()
            return response

    def getDetails(self,results,service):
        emailClassifier = pd.read_csv('/Users/XXXXXXXXX/Documents/Google Gmail API /EmailClass.csv',header=None,encoding='ISO-8859-1')
        for i in range(len(results['messages'])):
        #for i in range(2):
            message = service.users().messages().get(userId='me', id=results['messages'][i]['id'],format='full').execute()
            #print(message)
            try:
                if "SPAM" in message['labelIds']:
                    mail_SPAM.append(1)
                else:
                    mail_SPAM.append(0)
                
                if message['snippet']:
                    mail_SNIPPET.append(message['snippet'].lower())
                else:
                    mail_SNIPPET.append("")
                
                for j in range(len(message['payload']['headers'])):
                    if message['payload']['headers'][j]['name'] == 'From':
                        m = re.search('<(.+?)>', message['payload']['headers'][j]['value'])
                        if m:
                            found = m.group(1)
                            mail_MAILID.append(found.lower())
                        else:
                            mail_MAILID.append("")
                        
                    elif message['payload']['headers'][j]['name'] == "Subject":
                        if message['payload']['headers'][j]['value']:
                            mail_SUBJECT.append(message['payload']['headers'][j]['value'].lower())
                        else:
                            mail_SUBJECT.append("")

                    elif message['payload']['headers'][j]['name'] == 'Date':
                        if message['payload']['headers'][j]['value']:
                            mail_dateTime.append(self.DateTimeFormat(message['payload']['headers'][j]['value']))
                            #print(mail_dateTime)
                        else:
                            mail_dateTime.append("")
                            
            except KeyError:
                print(message)
                flags = None

    def get_credentials(self):
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

def fetchEmails():
    GenDataSet = GeneratingDataSet()
    credentials = GenDataSet.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    results = service.users().messages().list(userId='me',includeSpamTrash=True).execute()
    count = 0
    GenDataSet.getDetails(results,service)
    for x in range(1):
        newResult = GenDataSet.nextPage(results,service)
        print("Next Page Result ")
        results = newResult
        GenDataSet.getDetails(newResult,service)

    return [mail_dateTime,mail_SPAM,mail_SNIPPET,mail_MAILID,mail_SUBJECT]

def main():
    GenDataSet = GeneratingDataSet()
    GenDataSet.createCSV()
    fetchEmails()
    
    with open('/Users/XXXXXXXXX/Documents/Google Gmail API /EmailClass.csv','a') as f:
            w = csv.writer(f)
            w.writerows(zip(mail_dateTime,mail_SPAM,mail_SNIPPET,mail_MAILID,mail_SUBJECT))
            f.close()
    
if __name__ == '__main__':
    main()