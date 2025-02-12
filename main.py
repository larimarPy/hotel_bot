import os
import asyncio

from aiogram import Dispatcher, Bot, types

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import upr
from common.commands import cmds

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

dp.include_router(upr)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_name(name="Лоцман Грэй")
    await bot.set_my_description(description="Привет, меня зовут Грэй и я готов помочь тебе!(Любой текст здесь)")
    await bot.set_my_commands(commands=cmds, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

