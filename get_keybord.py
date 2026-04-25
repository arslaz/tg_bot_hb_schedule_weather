from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

def get_start_button():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🚀 Запустить")]],
        resize_keyboard=True
    )