from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from keyboards.workers import get_workers
from models.report_states import NightReportForm


router = Router(name=__name__)

@router.message(F.text, Command("night_report"))
async def night_report(message: Message, state: FSMContext):
    inline_buttons = get_workers()

    await state.set_data({
        "night_report_date": [],  # contain | data | worker name | product | pakaging | waight | 
        "current_row": 0,
        "fullness": 0
    })

    inline_buttons.adjust(1)
    await message.answer(
        text="Кто делает репорт?",
        reply_markup=inline_buttons.as_markup()
    )
    await state.set_state(NightReportForm.make_table)
    await message.bot.delete_message(message.chat.id, message.message_id)


