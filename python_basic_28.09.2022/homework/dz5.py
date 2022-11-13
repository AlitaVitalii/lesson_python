text = input('Купи слона! ')
while True:
    if text != "вже купив":
        text = input(f'Всі кажуть "{text}", а ти купи слона! ')
    else:
        print('Молодець!')
        break
