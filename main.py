from aiogram.filters import Command
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from json_file import *
from start_message import *
from schedule_bot.email_client import *
from schedule_bot.change_message import *
from initialization_bot import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def check_and_send():
    body = await get_unseen_message()
    if body is None:
        return

    text = await edit_text(body)
    subscribers = get_subscribers()

    for chat_id in subscribers:
        try:
            await bot.send_message(chat_id=chat_id, text=text)
        except Exception as e:
            logger.error(f"Ошибка отправки {chat_id}: {e}")

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_and_send, 'interval', minutes=5)
    scheduler.start()
    dp = Dispatcher()

    dp.message.register(cmd_start, Command("start"))
    dp.message.register(handle_start_button, F.text == "🚀 Запустить")

    @dp.message()
    async def fallback(message: Message):
        await message.answer("Напиши /start")

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())