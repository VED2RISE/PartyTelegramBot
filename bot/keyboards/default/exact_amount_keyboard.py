from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

exact_amount_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("В начало"),
        ],
    ],
    resize_keyboard=True
)
