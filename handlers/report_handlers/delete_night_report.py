from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from models.report_states import NightReportForm

router = Router(name=__name__)

@router.callback_query(F.data.startswith('delete_report'), NightReportForm.end_report)
async def delete_night_report(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.clear()
    data_after_finish = await state.get_data()
    print(data_after_finish)  
    await callback.answer()