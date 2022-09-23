

print('отгадай число')
x = int

number = 45

while number != x:
    x = int(input('Введите число:'))
    if x < number:
        print('Число меньше')
    if x > number:
        print('число больше')


print(f'\nВы отгадали число - {number}')