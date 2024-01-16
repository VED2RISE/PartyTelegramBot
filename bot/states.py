from aiogram.dispatcher.filters.state import State, StatesGroup


class Steps(StatesGroup):
    ticket_type = State()
    amount = State()
    exact_amount = State()
    discount = State()
