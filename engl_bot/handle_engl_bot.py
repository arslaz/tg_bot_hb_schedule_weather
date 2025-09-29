from aiogram.fsm.context import FSMContext
from datetime import datetime

from get_keybord import *
from stategroup import *
from json_file import *
from engl_bot.reg_all import *
async def handle_engl_bot(message: Message, state: FSMContext):
    if message.text == "✏ Добавить урок":
        await state.set_state(AddLess.engl_less)
        await message.answer(
            "✅ Отлично! Давай добавим уроки\n\n"
            "В какой день был урок\n"
            "Пример: Пятница 10.02.2022",
            reply_markup=get_cancel_keyboard()
        )


    elif message.text == "✒ Пометить как оплачено":
        await state.set_state(AddLess.engl_pay)
        await message.answer(
            "✅ Отлично! Давай пометим оплачено\n\n"
            "сколько уроков вы оплатили\n"
            "Пример: 5",
            reply_markup=get_cancel_keyboard()
        )


    elif message.text == "✉ Начать спам":
        await add_spam(message, state)


    elif message.text == "📋 Список уроков":
        lessons = get_engl()
        if not lessons:
            await message.answer(
                "У тебя пока нет уроков.",
                reply_markup=get_engl_bot_keyboard()
            )
            return

        message_text = "📅 Твои уроки:\n\n"
        for i, bless in enumerate(lessons, 1):

            message_text += f"{i}. {bless['date']} -  оплачено: {bless['pay']}\n"
            message_text += "\n"

        await message.answer(
            message_text,
            reply_markup=get_engl_bot_keyboard()
        )

    elif message.text == "⬅️ Назад к выбору бота":
        await state.set_state(MainMenuState.choosing_bot)
        await message.answer(
            "Выбери бота для использования:",
            reply_markup=get_start_keyboard()
        )

    elif message.text == "❌ Отмена":
        current_state = await state.get_state()
        if "EnglBot" and "AddLess" in str(current_state):
            await state.set_state(EnglBot.engl_menu)
            await message.answer(
                "Операция отменена.",
                reply_markup=get_engl_bot_keyboard()
            )
        else:
            await message.answer(
                "Нечего отменять.",
                reply_markup=get_engl_bot_keyboard()
            )