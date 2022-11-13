num_1 = int(input("Введіть нижню межу діапазону для пошуку простих чисел: "))
num_2 = int(input('Введіть верхню межу діапазону для пошуку простих чисел: '))
sum_delitel = 0
counter_prime = 0
print('Прості числа:')

while num_1 <= num_2:
    delitel = 2
    while delitel <= num_2:
        if num_1 % delitel == 0:
            sum_delitel += 1
        if sum_delitel > 1:
            break
        delitel += 1
    if sum_delitel == 1:
        counter_prime += 1
        print(num_1)
    sum_delitel = 0
    num_1 += 1

print('Знайдено простих чисел: ', counter_prime)
