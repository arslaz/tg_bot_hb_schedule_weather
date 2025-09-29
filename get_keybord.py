from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

def get_start_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎂 HB_bot"), KeyboardButton(text="📋 Расписание"), KeyboardButton(text="🇺🇸 Английский")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие..."
    )
    return keyboard

def get_hb_bot_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎂 Добавить ДР"), KeyboardButton(text="📋 Список ДР")],
            [KeyboardButton(text="⬅️ Назад к выбору бота")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие..."
    )
    return keyboard

def get_engl_bot_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Список уроков"), KeyboardButton(text="✏ Добавить урок")],
            [KeyboardButton(text="✉ Начать спам"),KeyboardButton(text='✒ Пометить как оплачено')],
            [KeyboardButton(text="⬅️ Назад к выбору бота")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие..."
    )
    return keyboard

def get_cancel_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="❌ Отмена")]],
        resize_keyboard=True
    )
    return keyboard

def get_out_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="⬅️ Назад к выбору бота")]],
        resize_keyboard=True
    )
    return keyboard

def get_inline_keyboard():

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="ДА",callback_data="yes")
        ],
        [
            InlineKeyboardButton(text="НЕТ",callback_data="no")
        ]
    ])
    return keyboard