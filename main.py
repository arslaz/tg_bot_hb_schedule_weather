from aiogram.filters import Command
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

from hb_bot.handle_hb_bot_buttons import *
from hb_bot.reg_date import *
from initialization_bot import *
from main_menu import *
from start_message import *
from schedule_bot.handle_schedule_bot import *
from engl_bot.handle_engl_bot import *
from engl_bot.reg_all import *

async def main():
    storage = MemoryStorage()

    dp = Dispatcher(storage=storage)

    dp.message.register(cmd_start, Command("start"))

    scheduler.start()

    dp.message.register(handle_bot_selection, MainMenuState.choosing_bot)
    dp.message.register(handle_hb_bot_buttons, HBBotState.main_menu)
    dp.message.register(handle_schedules_bot, ScheduleBotState.schedules_bot)

    dp.message.register(handle_engl_bot, EnglBot.engl_menu)
    dp.message.register(add_spam, EnglBot.engl_spam)
    dp.message.register(add_less, AddLess.engl_less)
    dp.message.register(add_pay, AddLess.engl_pay)

    dp.callback_query.register(yes_callback, F.data == "yes")
    dp.callback_query.register(no_callback, F.data == "no")

    dp.message.register(name_proce, AddBirthday.name)
    dp.message.register(date_proce, AddBirthday.date)
    dp.message.register(user_proce, AddBirthday.user)

    @dp.message()
    async def handle_other_messages(message: Message, state: FSMContext):
        await message.answer(
            "Используй кнопки ниже 👇, перезапустите бота копкой \start это может помочь",
            reply_markup=get_start_keyboard()
        )
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())