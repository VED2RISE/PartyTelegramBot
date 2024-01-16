from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

discount_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Да"),
            KeyboardButton("Нет"),
        ],
        [
            KeyboardButton("В начало"),
        ]
    ],
    resize_keyboard=True
)
