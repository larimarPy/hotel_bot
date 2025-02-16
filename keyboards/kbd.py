from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

def setup_kbd(
        *btns: str,
        placeholder: str = None,
        request_contact: int = None,
        request_location: int = None,
        sizes: tuple[int] = (2,),
):
    keyboard = ReplyKeyboardBuilder()

    for index, text in enumerate(btns):
        if request_contact and request_contact == index:
            keyboard.add(KeyboardButton(text=text, request_contact=True))
        elif request_location and request_location == index:
            keyboard.add(KeyboardButton(text=text, request_location=True))
        else:
            keyboard.add(KeyboardButton(text=text))
        
    return keyboard.adjust(*sizes).as_markup(resize_keyboard=True, input_field_placeholder=placeholder)


def setup_inline_kbd(
        *btns: tuple[str, str],
        placeholder: str = None,
        sizes: tuple[int] = (2,)
):
    inline_keyboard = InlineKeyboardBuilder()

    for text, callback_data in enumerate(btns):
        inline_keyboard.add(InlineKeyboardButton(text=text, callback_data=callback_data))

    return inline_keyboard.adjust(*sizes).as_markup()


