from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

main_menu_kbd = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Услуги отеля")],
        [KeyboardButton(text="Заказ еды в номер")],
        [KeyboardButton(text="Достопримечательности города")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Что интересует?"
)