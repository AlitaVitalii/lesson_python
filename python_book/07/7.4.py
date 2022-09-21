message = '\nВведите название топинга:'
message += '\nДля завершения формирования пицци, введите "quit".'

list_toping = []
while True:
    toping = input(message)
    if toping == "quit":
        break
    list_toping.append(toping.title())
    print(f'\tТопинг {toping.title()} в Вашу пиццу добавлен')
print(f'\nВаша пицца с заказанными топингами {list_toping} готовится. \nОжидайте. \nПриятного аппетита.')
