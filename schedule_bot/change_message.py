import re
from json_file import read_users_data

break_lessons = {
    "пн": [3, 4, 8],
    "чт": [3, 4],
    "сб": [3, 8],
}


async def edit_text(body):
    # Чистим мусор
    for trash in ["Уважаемая(ый) Лазаревич Арсений Александрович",
                  "------------------------------------------------------------",
                  "Автоматическая рассылка МКП 1С Колледж"]:
        body = body.replace(trash, "")

    if 'Четверг' in body:
        day_key = 'чт'
    elif 'Суббота' in body:
        day_key = 'сб'
    else:
        day_key = 'пн'

    all_schedules = read_users_data('schedule_times.json')
    day_schedule = all_schedules[day_key]

    for para_num in range(1, 8):
        for hour_num in range(1, 3):
            para_str = f"{para_num} пара {hour_num} час"

            lesson_num = (para_num - 1) * 2 + hour_num
            lesson_key = f"урок {lesson_num}"

            if lesson_key not in day_schedule:
                continue

            time = f"{day_schedule[lesson_key]['timebegin']} - {day_schedule[lesson_key]['timeend']}"
            body = body.replace(para_str, f"{lesson_num} урок({time})")

    text = ""
    added_breaks = set()

    for line in body.split("\n"):
        text += line + "\n"

        match = re.search(r'(\d+) урок\(', line)
        if match:
            lesson_num = int(match.group(1))
            if lesson_num in break_lessons[day_key] and lesson_num not in added_breaks:
                text += "🎉Перемена 20 мин🎉\n"
                added_breaks.add(lesson_num)

    first_lesson, last_lesson = get_first_last_lesson_from_text(text)

    if first_lesson and last_lesson:
        bus_first = read_users_data('bus_first.json')
        bus_last = read_users_data('bus_last.json')

        text += "\n🚌 Автобусы:\n"

        if day_key in bus_first and str(first_lesson) in bus_first[day_key]:
            text += f"На {first_lesson} урок: {bus_first[day_key][str(first_lesson)]}\n"

        if day_key in bus_last:
            if day_key == "чт":
                text += f"До курсов: {bus_last['чт']['до']}\n"
                text += f"После курсов: {bus_last['чт']['после']}\n"
            elif str(last_lesson) in bus_last[day_key]:
                text += f"С {last_lesson} урока: {bus_last[day_key][str(last_lesson)]}\n"

    return text


def get_first_last_lesson_from_text(text: str) -> tuple:
    matches = re.findall(r'(\d+) урок\(', text)
    if not matches:
        return None, None
    nums = [int(m) for m in matches]
    return min(nums), max(nums)