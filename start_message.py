from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from get_keybord import get_start_button
from json_file import add_subscriber
from config import *

async def cmd_start(message: Message, state: FSMContext):
    chat_id = str(message.chat.id)
    if chat_id not in bot_config['admin']:
        await message.answer("Нет доступа")
        return

    await state.clear()
    await message.answer(
        "Привет! Нажми 🚀 Запустить, чтобы получать расписание автоматически.",
        reply_markup=get_start_button()
    )


async def handle_start_button(message: Message):
    if message.text == "🚀 Запустить":
        is_new = add_subscriber(message.chat.id)
        if is_new:
            await message.answer(
                "✅ Бот запущен! Расписание будет приходить автоматически, когда появится новое.",
                reply_markup=None
            )
        else:
            await message.answer("Вы уже подписаны.")