from services.google_sheets import get_sheet_data
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_products(prev_data: list):
    builder = InlineKeyboardBuilder()
    product_list = get_sheet_data("products")
    

    for i in range(1, len(product_list)):
        temp = '\t⚖️'
        for j in range(len(prev_data)):
            if prev_data[j][2] == product_list[i][0]:
                temp = f'\t{prev_data[j][4]}'
        builder.button(text= (product_list[i][1] + temp), callback_data=f'product_{product_list[i][0]}')
    return builder
    