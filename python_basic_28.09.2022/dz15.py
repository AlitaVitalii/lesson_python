num_1 = int(input("Введіть нижню межу діапазону для пошуку простих чисел: "))
num_2 = int(input('Введіть верхню межу діапазону для пошуку простих чисел: '))
counter_prime = 0
print('Прості числа:')


def is_prime(num):
    delitel = 2
    while delitel < num or num == 2:
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

#
# while num_1 <= num_2:
#     delitel = 2
#     is_prime = True
#     while delitel < num_1:
#         if num_1 % delitel == 0:
#             is_prime = False
#             break
#         delitel += 1
#     if is_prime:
#         counter_prime += 1
#         print(num_1)
#     num_1 += 1
