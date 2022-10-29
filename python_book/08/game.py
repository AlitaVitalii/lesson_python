from random import randint

number = randint(1, 100)
print(number)

print('отгадай число')
x = int

# number = 621

while number != x:
    x = int(input('Введите число:'))
    if x < number:
        print('\tЧисло меньше')
    if x > number:
        print('\tчисло больше')


print(f'\nВы отгадали число - {number}')