num_1 = int(input("Введіть нижню межу діапазону для пошуку простих чисел: "))
num_2 = int(input('Введіть верхню межу діапазону для пошуку простих чисел: '))
s = 0
my_list = []
while num_1 <= num_2:
    a = 1
    while a <= num_2:
        if num_1 % a == 0:
            s += 1
        a += 1
    if s == 2:
        my_list.append(num_1)
    s = 0
    num_1 += 1

print('\nПрості числа: ', my_list)
# for i in my_list:
#     print(i)
print('Знайдено простих чисел: ', len(my_list))