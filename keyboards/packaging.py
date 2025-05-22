from services.google_sheets import get_sheet_data
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_packaging():
    builder = InlineKeyboardBuilder()
    packaging_list = get_sheet_data("packaging")


    for i in range(1, len(packaging_list)):
        builder.button(text= packaging_list[i][1], callback_data=f'packaging_{packaging_list[i][0]}')
    return builder
    