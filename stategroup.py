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