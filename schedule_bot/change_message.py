

async def edit_text(body):
    body = body.replace("Уважаемая(ый) Лазаревич Арсений Александрович", "")
    body = body.replace("------------------------------------------------------------", "")
    body = body.replace("Автоматическая рассылка МКП 1С Колледж", "")
    if 'Четверг' in body:
        body = body.replace("1 пара 1 час", "1 урок(8:00 - 8:45)")
        body = body.replace("1 пара 2 час", "2 урок(8:55 - 9:40)")
        body = body.replace("2 пара 1 час", "3 урок(9:50 - 10:35)")
        body = body.replace("2 пара 2 час", "4 урок(10:55 - 11:40)")
        body = body.replace("3 пара 1 час", "5 урок(12:00 - 12:45)")
        body = body.replace("3 пара 2 час", "6 урок(12:55 - 14:15)")
        body = body.replace("4 пара 1 час", "7 урок")
        body = body.replace("4 пара 2 час", "8 урок(14:35 - 15:55)")
        body = body.replace("5 пара 1 час", "9 урок")
        body = body.replace("5 пара 2 час", "10 урок(16:05 - 16:50)")
        body = body.replace("6 пара 1 час", "11 урок(17:10 - 17:55)")
        body = body.replace("6 пара 2 час", "12 урок(18:05 - 18:50)")
        body = body.replace("7 пара 1 час", "13 урок(19:00 - 19:45)")
        body = body.replace("7 пара 2 час", "14 урок(19:55 - 20:40)")
        lessons = ['10 урок(16:05 - 16:50)', '3 урок(9:50 - 10:35)']
    elif 'Суббота' in body:
        body = body.replace("1 пара 1 час", "1 урок(8:00 - 8:45)")
        body = body.replace("1 пара 2 час", "2 урок(8:55 - 9:40)")
        body = body.replace("2 пара 1 час", "3 урок(9:50 - 10:35)")
        body = body.replace("2 пара 2 час", "4 урок(10:55 - 11:40)")
        body = body.replace("3 пара 1 час", "5 урок(11:50 - 12:35)")
        body = body.replace("3 пара 2 час", "6 урок(12:45 - 13:30)")
        body = body.replace("4 пара 1 час", "7 урок(13:40 - 14:25)")
        body = body.replace("4 пара 2 час", "8 урок(14:35 - 15:20)")
        body = body.replace("5 пара 1 час", "9 урок(15:40 - 16:25)")
        body = body.replace("5 пара 2 час", "10 урок(16:35 - 17:20)")
        body = body.replace("6 пара 1 час", "11 урок(17:30 - 18:15)")
        lessons = ['8 урок(14:35 - 15:20)', '3 урок(9:50 - 10:35)']
    else:
        body = body.replace("1 пара 1 час", "1 урок(8:00 - 8:45)")
        body = body.replace("1 пара 2 час", "2 урок(8:55 - 9:40)")
        body = body.replace("2 пара 1 час", "3 урок(9:50 - 10:35)")
        body = body.replace("2 пара 2 час", "4 урок(10:55 - 11:40)")
        body = body.replace("3 пара 1 час", "5 урок(12:00 - 12:45)")
        body = body.replace("3 пара 2 час", "6 урок(12:55 - 13:40)")
        body = body.replace("4 пара 1 час", "7 урок(13:50 - 14:35)")
        body = body.replace("4 пара 2 час", "8 урок(14:45 - 15:30)")
        body = body.replace("5 пара 1 час", "9 урок(15:40 - 16:25)")
        body = body.replace("5 пара 2 час", "10 урок(16:45 - 17:30)")
        body = body.replace("6 пара 1 час", "11 урок(17:40 - 18:25)")
        body = body.replace("6 пара 2 час", "12 урок(18:35 - 19:20)")
        body = body.replace("7 пара 1 час", "13 урок(19:30 - 20:15)")
        lessons = ["9 урок(15:40 - 16:25)", '3 урок(9:50 - 10:35)', '4 урок(10:55 - 11:40)']
    text = ""
    for i in body.split("\n"):
        text += i + "\n"
        for lesson in lessons:
            if lesson in i:
                text += "🎉Перемена 20 мин🎉\n"
    return text