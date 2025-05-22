from services.google_sheets import get_sheet_data
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_workers():
    builder = InlineKeyboardBuilder()
    worker_list = get_sheet_data("workers")


    for i in range(1, len(worker_list)):
        builder.button(text= worker_list[i][1] + ' ' + worker_list[i][2] + ' ' + worker_list[i][3], callback_data=f'worker_{worker_list[i][0]}')
    return builder
    

