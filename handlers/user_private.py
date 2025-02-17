from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, or_f, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from keyboards.kbd import setup_kbd, setup_inline_kbd
from database import models

upr = Router()


async def orm_get_item(session: AsyncSession):
    query = select(models.Vodka)
    result = await session.execute(query)
    return result.scalars().all()


class MainMenu(StatesGroup):
    hotel_services = State()
    restoraunt = State()

class Hotel(StatesGroup):
    transfer = State()
    sauna = State()
    laundry = State()

class RestorauntMenu(StatesGroup):
    kitchen = State()
    bar = State()

class BarMenu(StatesGroup):
    alcohol = State()
    alcoholfree = State()



@upr.message(CommandStart(),)
async def for_start(message: types.Message):
    await message.answer(text="Привет, что интересует?", reply_markup=setup_kbd(
        "Услуги отеля", "Ресторан", placeholder="Что интересует?" 
    ))


@upr.message(or_f(Command("services"), F.text == "Услуги отеля"))
async def hotel_services(message: types.Message, state: FSMContext):
    await message.answer(text="Выберите услугу", reply_markup=setup_kbd(
        "Трансфер", "Сауна", "Прачечная", "Назад", placeholder="Куда двигаемся?", sizes=(2,1)
    ))
    await state.set_state(MainMenu.hotel_services)

@upr.message(F.text.in_(["Трансфер", "Сауна", "Прачечная"]))
async def hotel_services_list(message: types.Message, state:FSMContext):
    if message.text == "Трансфер":
        await message.answer(text="Подадим черную жемчужину!", reply_markup=setup_kbd(
            "Назад"
        ))
        await state.set_state(Hotel.transfer)
    if message.text == "Сауна":
        await message.answer(text="Уже топим печь?", reply_markup=setup_kbd(
            "Назад"
        ))
        await state.set_state(Hotel.sauna)
    if message.text == "Прачечная":
        await message.answer(text="Отстираем, отгладим!", reply_markup=setup_kbd(
            "Назад"
        ))
        await state.set_state(Hotel.laundry)



@upr.message(or_f(Command("menu"), F.text == "Ресторан"))
async def restoraunt_menu(message: types.Message, state: FSMContext):
    await message.answer(text="Поесть или выпить? А может и первое, и второе?", reply_markup=setup_kbd(
        "Меню кухни", "Меню бара", "Назад", placeholder="Куда двигаемся?", sizes=(2,1)
    ))
    await state.set_state(MainMenu.restoraunt)

@upr.message(StateFilter(MainMenu.restoraunt), F.text.in_(["Меню бара", "Меню кухни"]))
async def restoraunt_menu_list(message: types.Message, state: FSMContext):
    if message.text == "Меню бара":
        await message.answer("Выберите категорию напитков", reply_markup=setup_kbd(
            "Алкоголь", "Безалкогольные напитки", "Назад", placeholder="Выберите категорию", sizes=(2, 1)
        ))
        await state.set_state(RestorauntMenu.bar)
    if message.text == "Меню кухни":
        await message.answer("Выберите категорию блюд", reply_markup=setup_kbd(
            "Салаты", "Супы", "Паста", "К пиву", "Холодные закуски", "Горячие блюда", "Пицца",
            "Гарниры", "Десерты", "Соусы", "Назад", placeholder="Выберите категорию", sizes=(4, 3, 3, 1)
        ))
        await state.set_state(RestorauntMenu.kitchen)

@upr.message(StateFilter(RestorauntMenu.bar), F.text.in_(["Алкоголь", "Безалкогольные напитки"]))
async def bar_menu(message: types.Message, state: FSMContext):
    if message.text == "Алкоголь":
        await message.answer(text="Вот категории напитков:", reply_markup=setup_kbd(
            "Водка", "Виски", "Ром", "Коньяк", "Джин", "Текила", "Ликёры", "Коктейли",
            "Вермут", "Пиво", "Настойки", "Вина", "Назад", placeholder="Что заинтересовало?", sizes=(4, 4, 4, 1)
        ))
        await state.set_state(BarMenu.alcohol)
    if message.text == "Безалкогольные напитки":
        await message.answer(text="Вот категории напитков:", reply_markup=setup_kbd(
            "Чай", "Кофе", "Соки", "Б/А Пиво", "Газировка", "Назад", placeholder="Что заинтересовало?", sizes=(3, 2, 1)
        ))
        await state.set_state(BarMenu.alcoholfree)

@upr.message(StateFilter(BarMenu.alcohol), F.text == "Водка")
async def vodka(message: types.Message, state: FSMContext, session: AsyncSession):
    for item in await orm_get_item(session):
        await message.answer(text="vodka", reply_markup=setup_inline_kbd(btns={f"{item.name}": "some"}))


#BACK BUTTON

@upr.message(StateFilter("*"), F.text == "Назад")
async def back(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state == MainMenu.hotel_services or current_state == MainMenu.restoraunt:
        await message.answer(text="Что интересует?", reply_markup=setup_kbd(
        "Услуги отеля", "Ресторан", placeholder="Что интересует?"
        ))
   
    if current_state in Hotel:
        await message.answer(text="Выберите услугу", reply_markup=setup_kbd(
        "Трансфер", "Сауна", "Прачечная", "Назад", placeholder="Куда двигаемся?", sizes=(2,1)
        ))
        await state.set_state(MainMenu.hotel_services)
    
    if current_state in RestorauntMenu:
        await message.answer(text="Поесть или выпить? А может и первое, и второе?", reply_markup=setup_kbd(
        "Меню кухни", "Меню бара", "Назад", placeholder="Куда двигаемся?", sizes=(2,1)
        ))
        await state.set_state(MainMenu.restoraunt)
    
    if current_state in BarMenu:
        await message.answer("Выберите категорию напитков", reply_markup=setup_kbd(
            "Алкоголь", "Безалкогольные напитки", "Назад", placeholder="Выберите категорию", sizes=(2, 1)
        ))
        await state.set_state(RestorauntMenu.bar)