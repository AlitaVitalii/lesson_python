zodiac = {
    "овен": '21.03-20.04',
    "тілець": '21.04-21.05',
    "близнята": '22.05-21.06',
    "рак": '22.06-22.07',
    "лев": '23.07-22.08',
    "діва": '23.08-23.09',
    "терези": '24.09-23.10',
    "скорпіон": '24.10-22.11',
    "стрілець": '23.11-21.12',
    "козоріг": '22.12-20.01',
    "водолій": '21.01-18.02',
    "риби": '19.02-20.03',
}

days_in_month = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month = int(input("\nВведіть номер місяця (1-12) вашої дати народження: "))
day = int(input("Введіть число вашої дати народження: "))

if days_in_month.get(month) and days_in_month.get(month) >= day:
    for k, v in zodiac.items():
        zodiac[k] = [i for i in v.split('-')]

    for k, v in zodiac.items():
        zodiac[k] = [int(i) for i in v[0].split('.')], [int(i) for i in v[1].split('.')]

    for k, v in zodiac.items():
        if month == v[0][1]:
            if v[0][0] <= day <= days_in_month[month]:
                print(k.title())
        if month == v[1][1]:
            if v[1][0] >= day >= 1:
                print(k.title())
else:
    print('Ви ввели некоректну дату!')



