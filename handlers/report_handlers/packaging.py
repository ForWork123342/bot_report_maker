from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from datetime import date

from models.report_states import NightReportForm
from keyboards.packaging import get_packaging
router = Router(name=__name__)

@router.callback_query(F.data.startswith('product_'), NightReportForm.packaging_list)
async def handle_packaging_selection(callback: CallbackQuery, state: FSMContext):
    product_id = callback.data.split('_')[1]
    
    data = await state.get_data()
    data["current_row"] = data["fullness"]

    for i in range(len(data["report_data"])):
        if data["report_data"][i][2] == product_id:
            data["current_row"] = i
            break

    current_row = data.get("current_row", 0)

    if "report_data" in data and len(data["report_data"]) > current_row:
        data["report_data"][current_row][2] = product_id
    
    await state.update_data(product=product_id)
    await state.update_data({
        "report_data": data["report_data"],
        "current_row" : data["current_row"]
    })

    packaging_list = get_packaging()

    packaging_list.adjust(1)
    await callback.message.edit_text("Выберите тару:", reply_markup=packaging_list.as_markup())
    await state.set_state(NightReportForm.wait_weight)
    await callback.answer()