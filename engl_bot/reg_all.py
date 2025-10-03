from aiogram.fsm.context import FSMContext
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from aiogram.types import CallbackQuery
import datetime
from get_keybord import *
from stategroup import *
from json_file import *
from initialization_bot import *

scheduler = AsyncIOScheduler()

async def add_less(message: Message, state: FSMContext):
    if message.text == "❌ Отмена":
        await state.set_state(EnglBot.engl_menu)
        await message.answer(
            "Операция отменена.",
            reply_markup=get_engl_bot_keyboard()
        )
        return

    await state.update_data(engl_less=message.text)
    user_data = await state.get_data()
    add_engl( user_data['engl_less'], 'нет')
    await message.answer(
        f"✅ Отлично! Урок {user_data['engl_less']} добавлен!",
        reply_markup=get_engl_bot_keyboard()
    )
    await state.clear()
    await state.set_state(EnglBot.engl_menu)


async def add_pay(message: Message, state: FSMContext):
    if message.text == "❌ Отмена":
        await state.set_state(EnglBot.engl_menu)
        await message.answer(
            "Операция отменена.",
            reply_markup=get_engl_bot_keyboard()
        )
        return
    try:
        int(message.text)
        await state.update_data(engl_pay=int(message.text))
    except ValueError:
        await message.answer(
            'введите корректное число'
        )
        await state.set_state(AddLess.engl_pay)
    bless = await state.get_data()
    lessons = get_engl()
    if not lessons:
        await message.answer(
            "У тебя пока нет уроков.",
            reply_markup=get_engl_bot_keyboard()
        )
        return

    pay_count = bless['engl_pay']
    unpaid_lessons = [lesson for lesson in lessons if lesson['pay'] == 'нет']

    if not unpaid_lessons:
        await message.answer(
            "Нет неоплаченных уроков.",
            reply_markup=get_engl_bot_keyboard()
        )
        return

    if pay_count > len(unpaid_lessons):
        await message.answer(
            f"У тебя только {len(unpaid_lessons)} неоплаченных уроков. "
            f"Не могу отметить {pay_count} уроков.",
            reply_markup=get_engl_bot_keyboard()
        )
        return

    marked_count = 0
    for i in range(pay_count):
        if i < len(unpaid_lessons):
            update_engl(i, "да")
            marked_count += 1

    lessons = get_engl()
    message_text = "Список уроков:\n\n"
    for i, blesss in enumerate(lessons, 1):
        message_text += f"{i}. {blesss['date']} -  оплачено: {blesss['pay']}\n"
        message_text += "\n"
    await state.clear()
    await message.answer(
        message_text,
        reply_markup=get_engl_bot_keyboard()
    )

async def add_spam(message: Message, state: FSMContext):
    print("началось")
    chat_id = str(message.chat.id)
    try:
        scheduler.remove_job(f"mon_{chat_id}")
        print(f"Удалена существующая задача: {f"mon_{chat_id}"}")
    except Exception as e:
        print(f"Задача не найдена: {e}")

    scheduler.add_job(
        spam_mon,
        trigger=CronTrigger(
            day_of_week="mon,fri",
            hour=11,
            minute=10
        ),
        args=[chat_id],
        id=f"mon_{chat_id}",
        replace_existing=True,
        misfire_grace_time=3600
    )

    await spam_mon(chat_id)

async def spam_mon(chat_id: int):
    await bot.send_message(
        chat_id,
        '📚 Сегодня был урок?',
        reply_markup=get_inline_keyboard()
    )

async def yes_callback(callback: CallbackQuery, state: FSMContext):
        date = datetime.datetime.now()
        weekdays = {
            0: "понедельник",
            1: "вторник",
            4: "пятница"
        }

        day = weekdays[date.weekday()]
        today = datetime.datetime.now()
        formatted_date = today.strftime('%d.%m.%Y')
        text = f"{day} {formatted_date}"
        add_engl(text, 'нет')
        await state.set_state(EnglBot.engl_menu)
        await callback.message.answer(
            "✅ Добавлен новый урок",
            reply_markup=get_engl_bot_keyboard()
        )
        await callback.message.delete()
async def no_callback(callback: CallbackQuery, state: FSMContext):
    await state.set_state(EnglBot.engl_menu)
    await callback.message.edit_text(
        "😡 Не добавлен урок",
        reply_markup=get_engl_bot_keyboard()
    )
