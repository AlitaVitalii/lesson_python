day_week = {
    0: "Понеділок",
    1: "Вівторок",
    2: "Середа",
    3: "Четвер",
    4: "П'ятниця",
    5: "Субота",
    6: "Неділя"

}

text = input('Введіть дату (у форматі YYYY-MM-DD): ')

from datetime import datetime

today = datetime.strptime(text, '%Y-%m-%d')
key_data = today.weekday()

print('День тижня: ', day_week[key_data])

