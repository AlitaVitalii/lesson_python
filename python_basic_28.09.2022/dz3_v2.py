month = int(input("\nВведіть номер місяця (1-12) вашої дати народження: "))
day = int(input("Введіть число вашої дати народження: "))

if month == 3 and 21 <= day <= 31 or month == 4 and 1 <= day <= 20:
    print("Ваш знак зодіаку: Овен")
elif month == 4 and 21 <= day <= 30 or month == 5 and 1 <= day <= 21:
    print("Ваш знак зодіаку: Телець")
elif month == 5 and 22 <= day <= 31 or month == 6 and 1 <= day <= 21:
    print("Ваш знак зодіаку: Близнята")
elif month == 6 and 22 <= day <= 30 or month == 7 and 1 <= day <= 22:
    print("Ваш знак зодіаку: Рак")
elif month == 7 and 23 <= day <= 31 or month == 8 and 1 <= day <= 22:
    print("Ваш знак зодіаку: Лев")
elif month == 8 and 23 <= day <= 31 or month == 9 and 1 <= day <= 23:
    print("Ваш знак зодіаку: Діва")
elif month == 9 and 24 <= day <= 30 or month == 10 and 1 <= day <= 23:
    print("Ваш знак зодіаку: Терези")
elif month == 10 and 24 <= day <= 31 or month == 11 and 1 <= day <= 22:
    print("Ваш знак зодіаку: Cкорпіон")
elif month == 11 and 23 <= day <= 30 or month == 12 and 1 <= day <= 21:
    print("Ваш знак зодіаку: Стрілець")
elif month == 12 and 22 <= day <= 31 or month == 1 and 1 <= day <= 20:
    print("Ваш знак зодіаку: Козоріг")
elif month == 1 and 21 <= day <= 31 or month == 2 and 1 <= day <= 18:
    print("Ваш знак зодіаку: Водолій")
elif month == 2 and 19 <= day <= 29 or month == 3 and 1 <= day <= 20:
    print("Ваш знак зодіаку: Риби")
else:
    print('Ви ввели некоректну дату!')
