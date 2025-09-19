from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender
import time
from get_keybord import *
from stategroup import *
from initialization_bot import *
from schedule_bot.email_client import *
from schedule_bot.change_message import *

async def handle_schedules_bot(message: Message, state: FSMContext):
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        try:
            imap = await connect()
            text = await search_message(imap)
            text = await edit_text(text)
            await state.set_state(MainMenuState.choosing_bot)
            await message.answer(text, reply_markup=get_start_keyboard())
        except:
            await state.set_state(MainMenuState.choosing_bot)
            await message.answer("❌ Ошибка при получении расписания", reply_markup=get_start_keyboard())