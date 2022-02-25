month = int(input("Введите номер месяца года: "))
def season(num):
    month_list = []
    import calendar

    for name in calendar.month_name:
        month_list.append(name)
    if 12 == num or num <= 2:
        print("Winter")
    if 3 <= num <= 5:
        print("Spring")
    if 6 <= num <= 8:
        print("Summer")
    if 9 <= num <= 11:
        print("Autumn")

    return month_list[num]

print(season(month))