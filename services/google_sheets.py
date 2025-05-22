import gspread
from google.oauth2.service_account import Credentials
from config_reader import config

def get_google_sheet_client():
    creds = Credentials.from_service_account_file("credentials.json", scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ])
    return gspread.authorize(creds)

def get_sheet_data(list_name: str):
    client = get_google_sheet_client()
    sheet = client.open_by_key(config.google_sheets_data.get_secret_value())
    sheet_data = sheet.worksheet(list_name).get_all_values()
    return sheet_data 
