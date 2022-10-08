num_1 = int(input("Введіть нижню межу діапазону для пошуку простих чисел: "))
num_2 = int(input('Введіть верхню межу діапазону для пошуку простих чисел: '))
s = 0
sum_ = 0
print()
print('Прості числа:')
while num_1 <= num_2:
    a = 2
    while a <= num_2:
        if num_1 % a == 0:
            s += 1
        if s > 1:
            break
        a += 1
    if s == 1:
        sum_ += 1
        print(num_1)
    s = 0
    num_1 += 1

print('Знайдено простих чисел: ', sum_)
