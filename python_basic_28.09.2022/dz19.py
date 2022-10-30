from random import randint

numb_random = randint(1, 100)

print('Відгадайте число від 1 до 100')

counter = 0
# numb_input = int
while numb_random != numb_input:
    numb_input = int(input('\nВведіть число: '))
    counter += 1
    if numb_input < numb_random:
        print('\tЧисло замале')
    if numb_input > numb_random:
        print('\tЧисло завелике')

print(f'\nВи відгадали за {counter} спроб! Це було число {numb_random}.')