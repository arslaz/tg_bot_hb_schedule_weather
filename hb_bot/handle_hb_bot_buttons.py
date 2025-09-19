from aiogram.fsm.context import FSMContext
from datetime import datetime

from get_keybord import *
from stategroup import *
from json_file import *

async def handle_hb_bot_buttons(message: Message, state: FSMContext):
    if message.text == "🎂 Добавить ДР":
        await message.answer(
            "✅ Отлично! Давай добавим день рождения 🎂\n\n"
            "Как зовут именинника?",
            reply_markup=get_cancel_keyboard()
        )
        await state.set_state(AddBirthday.name)

    elif message.text == "📋 Список ДР":
        user_id = str(message.from_user.id)
        birthdays = get_date(user_id)

        if not birthdays:
            await message.answer(
                "У тебя пока нет добавленных дней рождения.",
                reply_markup=get_hb_bot_keyboard()
            )
            return

        message_text = "📅 Твои дни рождения:\n\n"
        for i, bday in enumerate(birthdays, 1):
            try:
                date_obj = datetime.strptime(bday['date'], '%Y-%m-%d')
                pretty_date = date_obj.strftime('%d.%m.%Y')
            except:
                pretty_date = bday['date']

            message_text += f"{i}. {bday['name']} - {pretty_date}\n"
            if user_id in bot_config['admin'] and bday['user']:
                message_text += f"   👤 Уведомлять: {bday['user']}\n"
            message_text += "\n"

        await message.answer(
            message_text,
            reply_markup=get_hb_bot_keyboard()
        )

    elif message.text == "⬅️ Назад к выбору бота":
        await state.set_state(MainMenuState.choosing_bot)
        await message.answer(
            "Выбери бота для использования:",
            reply_markup=get_start_keyboard()
        )

    elif message.text == "❌ Отмена":
        current_state = await state.get_state()
        if current_state and "AddBirthday" in str(current_state):
            await state.set_state(HBBotState.main_menu)
            await message.answer(
                "Операция отменена.",
                reply_markup=get_hb_bot_keyboard()
            )
        else:
            await message.answer(
                "Нечего отменять.",
                reply_markup=get_hb_bot_keyboard()
            )