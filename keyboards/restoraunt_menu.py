from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


restoraunt_menu_kbd = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меню кухни")],
        [KeyboardButton(text="Меню бара")],
        [KeyboardButton(text="Назад в меню")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Что выбираем?"
)


kitchen_menu_kbd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Салаты"),
            KeyboardButton(text="Супы"),
            KeyboardButton(text="Паста"),
        ],
        
        [
            KeyboardButton(text="Пицца"),
            KeyboardButton(text="Гарниры"),
            KeyboardButton(text="Десерты"),
        ],

        [
            KeyboardButton(text="Холодные закуски"),
            KeyboardButton(text="Горячие блюда")
        ],
        
        [
            KeyboardButton(text="\"К пиву\""),
            KeyboardButton(text="Соусы"),
        ],

        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Что выбираем?"
)

back_to_kitchen_menu_kbd = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Назад к меню кухни")]
    ],
    resize_keyboard=True
)

bar_menu_kbd = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Алкоголь и коктейли")],
        [KeyboardButton(text="Безалкогольные напитки")],
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Что выбираем?"
)

bar_alcho_kbd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Водка"),
            KeyboardButton(text="Виски"),
            KeyboardButton(text="Ром"),
            KeyboardButton(text="Текила"),
        ],
        [
            KeyboardButton(text="Джин"),
            KeyboardButton(text="Коньяк"),
            KeyboardButton(text="Вина"),
            KeyboardButton(text="Пиво"),
        ],
        [
            KeyboardButton(text="Настойки"),
            KeyboardButton(text="Вермуты"),
            KeyboardButton(text="Коктейли"),
        ],
        
        [KeyboardButton(text="Вернуться"),]
    ],
    resize_keyboard=True
)

back_to_alcho_list = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вернуться к списку")]
    ],
    resize_keyboard=True
)

nonealcho_kbd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Соки"),
            KeyboardButton(text="Газировки"),
            KeyboardButton(text="Вода"),
        ],
        [
            KeyboardButton(text="Вернуться")
        ]
    ],
    resize_keyboard=True
)

back_to_nonealcho_kbd = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вернуться назад")]
    ],
    resize_keyboard=True
)