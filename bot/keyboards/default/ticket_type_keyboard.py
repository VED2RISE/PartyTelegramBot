from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ticket_type_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Premium 🏆"),
            KeyboardButton("Standard 🥈"),
        ],
    ],
    resize_keyboard=True
)
