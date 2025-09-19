from aiogram.fsm.context import FSMContext
from datetime import datetime

from get_keybord import *
from stategroup import *
from json_file import *

async def name_proce(message: Message, state: FSMContext):
    if message.text == "❌ Отмена":
        await state.set_state(HBBotState.main_menu)
        await message.answer(
            "Операция отменена.",
            reply_markup=get_hb_bot_keyboard()
        )
        return

    await state.update_data(name=message.text)
    await message.answer(
        "✅ Отлично! Теперь введи дату рождения в формате:\n"
        "ГОД-МЕСЯЦ-ДЕНЬ\n\n"
        "Например: 1889-04-20\n",
        reply_markup=get_cancel_keyboard()
    )
    await state.set_state(AddBirthday.date)


async def date_proce(message: Message, state: FSMContext):
    if message.text == "❌ Отмена":
        await state.set_state(HBBotState.main_menu)
        await message.answer(
            "Операция отменена.",
            reply_markup=get_hb_bot_keyboard()
        )
        return

    user_id = str(message.from_user.id)
    try:
        date_str = message.text
        datetime.strptime(date_str, '%Y-%m-%d')
        await state.update_data(date=message.text)
    except ValueError:
        await message.answer(
            "❌ Неверный формат даты. Пожалуйста, введи дату в формате ГОД-МЕСЯЦ-ДЕНЬ:\n"
            "Например: 1889-04-20",
            reply_markup=get_cancel_keyboard()
        )
        return

    if user_id in bot_config['admin']:
        await message.answer(
            "✅ Отлично! Теперь введи user_id или username для уведомлений:\n"
            "(или напиши 'нет' если не нужно уведомлять)",
            reply_markup=get_cancel_keyboard()
        )
        await state.set_state(AddBirthday.user)
    else:
        user_data = await state.get_data()
        add_birthday(message.from_user.id, user_data['name'], user_data['date'], None)
        await state.set_state(HBBotState.main_menu)
        await message.answer(
            f"✅ Отлично! День рождения {user_data['name']} добавлен!\n"
            f"Я буду напоминать тебе о нем заранее!",
            reply_markup=get_hb_bot_keyboard()
        )


async def user_proce(message: Message, state: FSMContext):
    if message.text == "❌ Отмена":
        await state.set_state(HBBotState.main_menu)
        await message.answer(
            "Операция отменена.",
            reply_markup=get_hb_bot_keyboard()
        )
        return

    user_input = message.text.lower()
    if user_input in ['нет', 'no', 'none']:
        user_input = "None"

    await state.update_data(user=user_input)
    user_data = await state.get_data()
    add_birthday(message.from_user.id, user_data['name'], user_data['date'], user_data['user'])
    await state.set_state(HBBotState.main_menu)

    if user_data['user']:
        message_text = f"✅ Отлично! День рождения {user_data['name']} добавлен!\n👤 Уведомления для: {user_data['user']}"
    else:
        message_text = f"✅ Отлично! День рождения {user_data['name']} добавлен!\n🔕 Уведомления отключены"

    await message.answer(
        message_text,
        reply_markup=get_hb_bot_keyboard()
    )