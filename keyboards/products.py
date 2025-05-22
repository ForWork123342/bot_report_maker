from services.google_sheets import get_sheet_data
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_products():
    builder = InlineKeyboardBuilder()
    product_list = get_sheet_data("products")


    for i in range(1, len(product_list)):
        builder.button(text= product_list[i][1], callback_data=f'product_{product_list[i][0]}')
    return builder
    