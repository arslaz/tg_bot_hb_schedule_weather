from aiogram.fsm.context import FSMContext

from get_keybord import *
from stategroup import *
from config import *

async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(MainMenuState.choosing_bot)
    chat_id = str(message.chat.id)
    if chat_id in bot_config['admin']:
        await message.answer(
            '🎉 Привет! Я бот с различными функциями!\n\n'
            'Выбери, какого бота хочешь использовать:\n'
            '🎂 HB_bot - напоминания о днях рождения\n'
            '🇺🇸 Английский - сколько прошло уроков, сколько оплачено\n'
            '📋 Расписание - расписанием уроков\n\n'
            'Выбери бота на клавиатуре ниже 👇',
            reply_markup=get_start_keyboard()
        )
    else:
        await message.answer(
            '🎉 Привет, ты можешь просто полюбоваться на этого бота\n\n'
            '😂 Функции тебе не доступны\n'
            '💀У тебя нету никаких прав, если ты считаешь что с тобой поступаю не правильно, можешь обратиться к админу вот его тг: 🤡\n'
            'ты скорее всего отлетишь в долгий игнор, так что не утруждайся'
        )