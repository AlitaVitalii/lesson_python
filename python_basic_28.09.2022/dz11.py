text_1 = input('Введіть перший фрагмент тексту: ')
text_2 = input('Введіть другий фрагмент тексту: ')

list_1 = sorted([i.lower() for i in text_1 if i.isalpha()])
list_2 = sorted([i.lower() for i in text_2 if i.isalpha()])

if list_1 == list_2 and text_1 != text_2:
    print('Тексти є анаграмами')
elif text_2 == text_1:
    print('Тексти однакові')
else:
    print('Тексти не є анаграмами')

