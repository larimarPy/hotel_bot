from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, or_f

from keyboards.main_menu import main_menu_kbd
from keyboards.hotel_services import hotel_services_list_kbd, back_to_menu_kbd
from keyboards.restoraunt_menu import back_to_nonealcho_kbd, back_to_alcho_list, kitchen_menu_kbd, bar_menu_kbd, restoraunt_menu_kbd, back_to_kitchen_menu_kbd, bar_alcho_kbd, nonealcho_kbd
from keyboards.attractions import attractions_kbd

upr = Router()


@upr.message(CommandStart())
async def start_cdm(message: types.Message):
    await message.answer(text="some text here", reply_markup=main_menu_kbd)

@upr.message(F.text == "Назад в меню")
async def hotel_services(message: types.Message):
    await message.answer(text="some text here", reply_markup=main_menu_kbd)


# hotel_services

@upr.message(or_f(Command("services"), (F.text == "Услуги отеля")))
async def hotel_services(message: types.Message):
    await message.answer(text="Вот список услуг отеля", reply_markup=hotel_services_list_kbd)

@upr.message(F.text == "Трансфер")
async def hotel_services(message: types.Message):
    await message.answer(text="Тут что-то про трасфер", reply_markup=back_to_menu_kbd)

@upr.message(F.text == "Сауна")
async def hotel_services(message: types.Message):
    await message.answer(text="Тут что-то про сауну", reply_markup=back_to_menu_kbd)

@upr.message(F.text == "Прачечная")
async def hotel_services(message: types.Message):
    await message.answer(text="Тут что-то про прачечную", reply_markup=back_to_menu_kbd)

@upr.message(F.text == "Назад к списку")
async def hotel_services(message: types.Message):
    await message.answer(text="Вот список услуг отеля", reply_markup=hotel_services_list_kbd)


# restoraunt menu

@upr.message(or_f(Command("menu"), (F.text == "Заказ еды в номер")))
async def hotel_services(message: types.Message):
    await message.answer(text="выберите", reply_markup=restoraunt_menu_kbd)

@upr.message(F.text == "Меню бара")
async def hotel_services(message: types.Message):
    await message.answer(text="выберите", reply_markup=bar_menu_kbd)

@upr.message(F.text == "Назад")
async def hotel_services(message: types.Message):
    await message.answer(text="выберите", reply_markup=restoraunt_menu_kbd)

# kitchen menu
@upr.message(F.text == "Меню кухни")
async def hotel_services(message: types.Message):
    await message.answer(text="выберите", reply_markup=kitchen_menu_kbd)

@upr.message(F.text == "Салаты")
async def hotel_services(message: types.Message):
    await message.answer(text="Информация", reply_markup=back_to_kitchen_menu_kbd)

@upr.message(F.text == "Супы")
async def hotel_services(message: types.Message):
    await message.answer(text="Информация", reply_markup=back_to_kitchen_menu_kbd)

@upr.message(F.text == "Паста")
async def hotel_services(message: types.Message):
    await message.answer(text="Информация", reply_markup=back_to_kitchen_menu_kbd)

@upr.message(F.text == "Пицца")
async def hotel_services(message: types.Message):
    await message.answer(text="Информация", reply_markup=back_to_kitchen_menu_kbd)

@upr.message(F.text == "Холодные закуски")
async def hotel_services(message: types.Message):
    await message.answer(text="Информация", reply_markup=back_to_kitchen_menu_kbd)

@upr.message(F.text == "Горячие блюда")
async def hotel_services(message: types.Message):
    await message.answer(text="Информация", reply_markup=back_to_kitchen_menu_kbd)

@upr.message(F.text == "Гарниры")
async def hotel_services(message: types.Message):
    await message.answer(text="Информация", reply_markup=back_to_kitchen_menu_kbd)

@upr.message(F.text == "\"К пиву\"")
async def hotel_services(message: types.Message):
    await message.answer(text="Информация", reply_markup=back_to_kitchen_menu_kbd)

@upr.message(F.text == "Десерты")
async def hotel_services(message: types.Message):
    await message.answer(text="Информация", reply_markup=back_to_kitchen_menu_kbd)

@upr.message(F.text == "Соусы")
async def hotel_services(message: types.Message):
    await message.answer(text="Информация", reply_markup=back_to_kitchen_menu_kbd)

@upr.message(F.text == "Назад к меню кухни")
async def back_to_kitchen_menu(message: types.Message):
    await message.answer(text="выберите", reply_markup=kitchen_menu_kbd)

# bar menu
@upr.message(F.text == "Алкоголь и коктейли")
async def alcho(message: types.Message):
    await message.answer(text="Вот список категорий", reply_markup=bar_alcho_kbd)

@upr.message(F.text == "Вернуться")
async def bar_categories(message: types.Message):
    await message.answer(text="Выберите", reply_markup=bar_menu_kbd)

@upr.message(F.text == "Водка")
async def alcho(message: types.Message):
    await message.answer(text="text", reply_markup=back_to_alcho_list)

@upr.message(F.text == "Виски")
async def alcho(message: types.Message):
    await message.answer(text="text", reply_markup=back_to_alcho_list)

@upr.message(F.text == "Ром")
async def alcho(message: types.Message):
    await message.answer(text="text", reply_markup=back_to_alcho_list)

@upr.message(F.text == "Текила")
async def alcho(message: types.Message):
    await message.answer(text="text", reply_markup=back_to_alcho_list)

@upr.message(F.text == "Джин")
async def alcho(message: types.Message):
    await message.answer(text="text", reply_markup=back_to_alcho_list)

@upr.message(F.text == "Коньяк")
async def alcho(message: types.Message):
    await message.answer(text="text", reply_markup=back_to_alcho_list)

@upr.message(F.text == "Вина")
async def alcho(message: types.Message):
    await message.answer(text="text", reply_markup=back_to_alcho_list)

@upr.message(F.text == "Пиво")
async def alcho(message: types.Message):
    await message.answer(text="text", reply_markup=back_to_alcho_list)

@upr.message(F.text == "Настойки")
async def alcho(message: types.Message):
    await message.answer(text="text", reply_markup=back_to_alcho_list)

@upr.message(F.text == "Вермуты")
async def alcho(message: types.Message):
    await message.answer(text="text", reply_markup=back_to_alcho_list)

@upr.message(F.text == "Коктейли")
async def alcho(message: types.Message):
    await message.answer(text="text", reply_markup=back_to_alcho_list)

@upr.message(F.text == "Вернуться к списку")
async def alcho(message: types.Message):
    await message.answer(text="some text", reply_markup=bar_alcho_kbd)

@upr.message(F.text == "Безалкогольные напитки")
async def alcho(message: types.Message):
    await message.answer(text="some text", reply_markup=nonealcho_kbd)

@upr.message(F.text == "Вернуться назад")
async def alcho(message: types.Message):
    await message.answer(text="some text", reply_markup=nonealcho_kbd)

@upr.message(F.text == "Соки")
async def bar(message: types.Message):
    await message.answer(text="Список соков", reply_markup=back_to_nonealcho_kbd)
    
@upr.message(F.text == "Газировки")
async def bar(message: types.Message):
    await message.answer(text="Список газировки", reply_markup=back_to_nonealcho_kbd)

@upr.message(F.text == "Вода")
async def bar(message: types.Message):
    await message.answer(text="Список воды", reply_markup=back_to_nonealcho_kbd)


# attractions

@upr.message(F.text == "Достопримечательности города")
async def attractions(message: types.Message):
    await message.answer(text="Тут можно что-то про достопримечательности: маршруты, что посмотреть, про экскурсии", reply_markup=attractions_kbd)
