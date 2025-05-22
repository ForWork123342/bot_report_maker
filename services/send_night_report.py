import gspread
from google.oauth2.service_account import Credentials
from .helper.helper import change_table

def get_google_sheet_client():
    creds = Credentials.from_service_account_file("credentials.json", scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ])
    return gspread.authorize(creds)

def send_night_report(data: list):
    return change_table(data)