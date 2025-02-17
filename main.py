import os
import asyncio

from aiogram import Dispatcher, Bot, types
from aiogram.fsm.storage.memory import MemoryStorage

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from middleware.db import DataBaseSession

from dao.database import create_db, drop_db, sessionmaker

from handlers.user_private import upr
from common.commands import cmds

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

dp.include_router(upr)


async def on_startup(bot):

    run_param = False
    if run_param:
        await drop_db()

    await create_db()

async def on_shutdown(bot):
    print('бот лег')

async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(DataBaseSession(session_pool=sessionmaker))

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_description(description="Привет, меня зовут Грэй и я готов помочь тебе!(Любой текст здесь)")
    await bot.set_my_commands(commands=cmds, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

