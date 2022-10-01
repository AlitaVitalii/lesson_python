

print('отгадай число')
x = int

number = 621

while number != x:
    x = int(input('Введите число:'))
    if x < number:
        print('\tЧисло меньше')
    if x > number:
        print('\tчисло больше')


print(f'\nВы отгадали число - {number}')