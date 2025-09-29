from aiogram.fsm.context import FSMContext

from get_keybord import *
from stategroup import *
from schedule_bot.handle_schedule_bot import *

async def handle_bot_selection(message: Message, state: FSMContext):
    if message.text == "🎂 HB_bot":
        await state.set_state(HBBotState.main_menu)
        await message.answer(
            "✅ Выбран HB_bot! \n Здесь ты можешь добавить друзей и их день рождения и всегда помнить о них. \n Выберите действие:",
            reply_markup=get_hb_bot_keyboard()
        )

    elif message.text == "🇺🇸 Английский":
        await state.set_state(EnglBot.engl_menu)
        await message.answer(
            "✅ Выбран HB_bot! \n Здесь ты можешь смотреть сколько уроков прошло, добавлять уроки, смотреть сколько не оплачено и изменять это. \n Выберите действие:",
            reply_markup=get_engl_bot_keyboard()
        )

    elif message.text == "📋 Расписание":
        await state.set_state(ScheduleBotState.schedules_bot)
        await handle_schedules_bot(message, state)