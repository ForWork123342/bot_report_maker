from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from models.report_states import NightReportForm
router = Router(name=__name__)


@router.message(NightReportForm.weight_input)
async def handle_weight_input(message: Message, state: FSMContext):
    weight = message.text.strip()
    
    
    try:
        weight_value = float(weight.replace(',', '.'))  # На случай, если вводят "5,2" вместо "5.2"
    except ValueError:
        await message.answer("❌ Ошибка! Введите число (например: 5.2 или 10):")
        return  # Остаемся в состоянии weight_input
    
    data = await state.get_data()
    current_row = data.get("current_row", 0)
    fullnes = data.get("fullness", 0)

   

    if "report_data" in data and len(data["report_data"]) > current_row:
        data["report_data"][current_row][4] = weight_value


    await state.update_data(weight=weight_value)
    await state.update_data({
        "report_data": data["report_data"]
    })



    data = await state.get_data()

    for row in data["report_data"]:
        print(row)

    builder = InlineKeyboardBuilder()

    builder.button(text='🍏 Другой продукт', callback_data='add_product')
    if True:
        builder.button(text="🏁 Закончить отчет!", callback_data='finish_night_report')
    await state.set_state(NightReportForm.end_report)  

    if fullnes == current_row and fullnes < 10:
        fullnes += 1 
    
    await state.update_data(fullness=fullnes)
    await message.answer(
        f"✅ Данные сохранены:\n"
        f"⚖️ Вес: {weight_value}\n\n"
        f"Хотите добавить еще один продукт?",
        reply_markup=builder.as_markup()
        )