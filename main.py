from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

from hb_bot.handle_hb_bot_buttons import *
from hb_bot.reg_date import *
from initialization_bot import *
from main_menu import *
from start_message import *
from schedule_bot.handle_schedule_bot import *


async def main():
    storage = MemoryStorage()

    dp = Dispatcher(storage=storage)

    dp.message.register(cmd_start, Command("start"))

    dp.message.register(handle_bot_selection, MainMenuState.choosing_bot)
    dp.message.register(handle_hb_bot_buttons, HBBotState.main_menu)
    dp.message.register(handle_schedules_bot, ScheduleBotState.schedules_bot)
    dp.message.register(name_proce, AddBirthday.name)
    dp.message.register(date_proce, AddBirthday.date)
    dp.message.register(user_proce, AddBirthday.user)

    @dp.message()
    async def handle_other_messages(message: Message, state: FSMContext):
        await message.answer(
            "Используй кнопки ниже 👇",
            reply_markup=get_start_keyboard()
        )
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())