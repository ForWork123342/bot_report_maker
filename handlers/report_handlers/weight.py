from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from models.report_states import NightReportForm

router = Router(name=__name__)

@router.callback_query(F.data.startswith('packaging_'), NightReportForm.wait_weight)
async def handle_packaging_selection(callback: CallbackQuery, state: FSMContext):
    packaging_id = callback.data.split('_')[1]
    await state.update_data(packaging=packaging_id)
    
    data = await state.get_data()
    current_row = data.get("current_row", 0)

    if "report_data" in data and len(data["report_data"]) > current_row:
        data["report_data"][current_row][3] = packaging_id
    
    await state.update_data(product=packaging_id)
    await state.update_data({
        "report_data": data["report_data"]
    })
    
    await callback.message.edit_text(
        "📝 Введите вес/количество в кг (например, 5.2):",
        reply_markup=None 
    )
    await state.set_state(NightReportForm.weight_input)  
    await callback.answer()