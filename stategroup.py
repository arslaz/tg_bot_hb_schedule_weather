from aiogram.filters.state import State, StatesGroup


class MainMenuState(StatesGroup):
    choosing_bot = State()


class HBBotState(StatesGroup):
    main_menu = State()
    adding_birthday = State()

class ScheduleBotState(StatesGroup):
    schedules_bot = State()

class AddBirthday(StatesGroup):
    name = State()
    date = State()
    user = State()

class EnglBot(StatesGroup):
    engl_menu = State()
    engl_spam = State()

class AddLess(StatesGroup):
    engl_less = State()
    engl_pay = State()