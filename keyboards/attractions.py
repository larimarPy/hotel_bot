from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

attractions_kbd = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Назад в меню")]
    ],
    resize_keyboard=True
) 

