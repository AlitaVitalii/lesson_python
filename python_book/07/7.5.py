age = int(input('Введите ваш возвраст: '))

otvet = True
while otvet:
    if age <= 3:
        print("Прохід безкоштовний.")
        otvet = False
    if 3 < age < 12:
        print("Квиток коштує 10 грн.")
        otvet = False
    if age >= 12:
        print("Квиток коштує 15 грн.")
        break
print("Дякуємо що завітали. Приходьте ще.")