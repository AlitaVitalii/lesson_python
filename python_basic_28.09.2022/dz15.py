num_1 = int(input("Введіть нижню межу діапазону для пошуку простих чисел: "))
num_2 = int(input('Введіть верхню межу діапазону для пошуку простих чисел: '))
counter_prime = 0
print('Прості числа:')


def is_prime(num):
    delitel = 2
    while delitel < num:
        if num % delitel == 0:
            return False
        delitel += 1
    return True


while num_1 <= num_2:
    if is_prime(num_1):
        print(num_1)
        counter_prime += 1
    num_1 += 1

print('Знайдено простих чисел: ', counter_prime)