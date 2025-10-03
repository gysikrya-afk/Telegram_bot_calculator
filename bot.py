import logging
import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot,Dispatcher
from app.heandler import router

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
