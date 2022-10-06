print("Дізнайся свій знак задіаку!")
print("Для виходу с програми введіть '777'")
promt = 'Ви ввели некоректну дату!'

while True:
    # print("\nДізнайся свій знак задіаку!")
    # print("Для виходу с програми натисни 'q'\n")
    month = int(input("\nВведіть номер місяця (1-12) вашої дати народження: "))
    if month == 777:
        print('The end)')
        break
    day = int(input("Введіть число вашої дати народження: "))
    if day == 777:
        print('The end)')
        break
    if month == 1:
        if 1<=day<20:
            print("Ваш знак зодіаку: Козоріг")
        elif 21<=day<=31:
            print("Ваш знак зодіаку: Водолій")
        else:
            print(promt)
    elif month == 2:
        if 1<=day<=18:
            print("Ваш знак зодіаку: Водолій")
        elif 19<=day<=29:
            print("Ваш знак зодіаку: Риби")
        else:
            print(promt)
    elif month == 3:
        if 1<=day<=20:
            print("Ваш знак зодіаку: Риби")
        elif 21<=day<=31:
            print("Ваш знак зодіаку: Овен")
        else:
            print(promt)
    elif month == 4:
        if 1<=day<=20:
            print("Ваш знак зодіаку: Овен")
        elif 21<=day<=30:
            print("Ваш знак зодіаку: Телець")
        else:
            print(promt)
    elif month == 5:
        if 1<=day<=21:
            print("Ваш знак зодіаку: Телець")
        elif 22<=day<=31:
            print("Ваш знак зодіаку: Близнята")
        else:
            print(promt)
    elif month == 6:
        if 1<=day<=21:
            print("Ваш знак зодіаку: Близнята")
        elif 22<=day<=30:
            print("Ваш знак зодіаку: Рак")
        else:
            print(promt)
    elif month == 7:
        if 1<=day<=22:
            print("Ваш знак зодіаку: Рак")
        elif 23<=day<=31:
            print("Ваш знак зодіаку: Лев")
        else:
            print(promt)
    elif month == 8:
        if 1<=day<=22:
            print("Ваш знак зодіаку: Лев")
        elif 23<=day<=31:
            print("Ваш знак зодіаку: Діва")
        else:
            print(promt)
    elif month == 9:
        if 1<=day<=23:
            print("Ваш знак зодіаку: Діва")
        elif 24<=day<=30:
            print("Ваш знак зодіаку: Терези")
        else:
            print(promt)
    elif month == 10:
        if 1<=day<=23:
            print("Ваш знак зодіаку: Терези")
        elif 24<=day<=31:
            print("Ваш знак зодіаку: Cкорпіон")
        else:
            print(promt)
    elif month == 11:
        if 1<=day<=22:
            print("Ваш знак зодіаку: Скорпіон")
        elif 23<=day<=30:
            print("Ваш знак зодіаку: Стрілець")
        else:
            print(promt)
    elif month == 12:
        if 1<=day<=21:
            print("Ваш знак зодіаку: Стрілець")
        elif 22<=day<=31:
            print("Ваш знак зодіаку: Козоріг")
        else:
            print(promt)
    else:
        print(promt)

