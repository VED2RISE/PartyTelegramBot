from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

amount_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("1"),
        ],
        [
            KeyboardButton("2"),
            KeyboardButton("3"),
            KeyboardButton("4"),
        ],
        [
            KeyboardButton("5"),
            KeyboardButton("6"),
            KeyboardButton("7"),
        ],
    ],
    resize_keyboard=True
)
