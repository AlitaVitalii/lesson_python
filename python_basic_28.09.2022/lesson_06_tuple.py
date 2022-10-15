text = 'Привіт, світ!'

for i, c in enumerate(text, start=10):
    print(f"{i}. {c}")
print('--------------1')


text = "Привіт, Світ!"

# num_of_t = 0
#
# for c in text:
#     if c == 'т':
#         num_of_t += 1
#
# if num_of_t > 0:
#     print("У рядку є буква 'т'")

has_t = False

for c in text:
    if c == 'т':
        has_t = True
        break

if has_t:
    print("У рядку є буква 'т'")

# Присвоєння булевих змінних:
# правильно:
# has_t = 'т' in text
# НЕ правильно:
# has_t = 'т' in text == True

print('-----------------2')

# text = input("Введіть цілі числа, розділені комою: ")
# num_list = [int(i) for i in text.split(',')]
# print(num_list)
#
# for num in num_list:
#     print(num * 2)

print('___------------------3')

fibonacci_numbers = (1, 2, 3, 5, 8, 13, 21)
small_tuple = (1,)  # увага на кому, без неї це буде рівнозначно small_tuple = 1

# fibonacci_numbers[0] = 42  # не працюватиме

print(fibonacci_numbers.index(3))  # 2
print(fibonacci_numbers.count(3))  # 1

a = 2
b = 3
print(a, b)

c = b
b = a
a = c
print(a, b)

# те ж саме на Python
a, b = b, a
print(a, b)

print('-------------4')

set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {4, 5, 6, 7, 8, 9}

set_3 = set_1.copy()
set_1.add(7) #dobavlenie
set_1.add(3)
set_1.remove(1) #ydalenie, vudaet owubky esli net znachenie.
set_1.discard(8) #ydalyaet bez vudachi owubok
set_4 = set_1.union(set_3) #ob'edenenie
set_5 = set_1.difference(set_3)
set_6 = set_1.symmetric_difference(set_2)

print(set_1)
print(set_2)
print(set_3)
print(set_4)
print(set_5)
print(set_3.issubset(set_1))
print(set_1.issuperset(set_1))
print(set_3.isdisjoint(set_4)) #если не пересекаются выдаёт True


print('------------------5')

text = "Привіт, Світ!"

print(set(text))
unique_letters = set([c.lower() for c in text if c.isalpha()])

print(len(unique_letters))
print(unique_letters)

print('-----------------6')

set_1 = frozenset([1, 2, 3, 1, 2, 3])
set_2 = frozenset({4, 5, 6})

print(set_1)
print(set_2)
print(set_1.union(set_2))

print('-------------------7')

set_1 = {43, 28, 2, 17}

print(set_1)
print(sorted(set_1))