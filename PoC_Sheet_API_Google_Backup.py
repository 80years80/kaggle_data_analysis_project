import httplib2
import os

from apiclient import discovery
from google.oauth2 import service_account


scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/spreadsheets"]
secret_file = '/home/pi/client_secret.json'


spreadsheet_id = '1YLnWNTjsHNhGe65tKdrU_8VRqsAVQmPy4hbqYWpWltw'
range_name = 'Sheet1!A1:D2'
print(secret_file)

credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
service = discovery.build('sheets', 'v4', credentials=credentials)

values = [['a1', 'b1', 'c1', 123], ['a2', 'b2', 'c2', 456],]

data = {
    'values' : values 
}
service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, body=data, range=range_name, valueInputOption='USER_ENTERED').execute()
