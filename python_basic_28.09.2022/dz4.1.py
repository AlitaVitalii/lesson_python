num_1 = int(input("Введіть нижню межу діапазону для пошуку простих чисел: "))
num_2 = int(input('Введіть верхню межу діапазону для пошуку простих чисел: '))
counter_prime = 0
print('Прості числа:')

while num_1 <= num_2:
    delitel = 2
    is_prime = True
    while delitel < num_1 or num_1 == 2:
        if num_1 % delitel == 0:
            is_prime = False
            break
        delitel += 1
    if is_prime:
        counter_prime += 1
        print(num_1)
    num_1 += 1

print('Знайдено простих чисел: ', counter_prime)
