from aiogram.fsm.state import State, StatesGroup


class NightReportForm(StatesGroup):
    make_table = State()
    product_list = State()
    packaging_list = State()
    wait_weight = State()
    weight_input = State()
    end_report = State()