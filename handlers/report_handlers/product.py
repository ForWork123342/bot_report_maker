from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from datetime import date

from models.report_states import NightReportForm
from keyboards.products import get_products

router = Router(name=__name__)

@router.callback_query(
    F.data.startswith('worker_') | F.data.startswith('add_product'),
    StateFilter(NightReportForm.end_report, NightReportForm.make_table)
)
async def handle_worker_selection(callback: CallbackQuery, state: FSMContext):


    current_state = await state.get_state()
    
    if current_state == NightReportForm.make_table.state:
        worker_id = callback.data.split('_')[1] # get worker id from button
        await state.update_data(worker=worker_id)

        current_date = date.today().isoformat()  # get data 
        report_data = []

        for _ in range(10):
            report_data.append([current_date, worker_id, None, None, None, None, None]) # contain | data | worker name | product | pakaging | waight | package weight | product weight |

        await state.update_data({
            "report_data": report_data,
            "current_row": 0,
            "fullness" : 0
        })

    
    prev_data = await state.get_data()

    product_list = get_products(prev_data["report_data"])
    product_list.adjust(1)
    await callback.message.edit_text("Выберите продукт:", reply_markup=product_list.as_markup())
    await state.set_state(NightReportForm.packaging_list)
    await callback.answer()

