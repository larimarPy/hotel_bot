from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

hotel_services_list_kbd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Трансфер"),
            KeyboardButton(text="Сауна"),
            KeyboardButton(text="Прачечная")
        ],
        [
            KeyboardButton(text="Назад в меню")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Что интересует?"
)

back_to_menu_kbd = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Назад к списку")]
    ],
    resize_keyboard=True
)
