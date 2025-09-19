from aiogram.fsm.context import FSMContext

from get_keybord import *
from stategroup import *

async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(MainMenuState.choosing_bot)
    await message.answer(
        '🎉 Привет! Я бот с различными функциями!\n\n'
        'Выбери, какого бота хочешь использовать:\n'
        '🎂 HB_bot - напоминания о днях рождения\n'
        '🌈 Погода - прогноз погоды\n'
        '📋 Расписание - расписанием уроков\n\n'
        'Выбери бота на клавиатуре ниже 👇',
        reply_markup=get_start_keyboard()
    )