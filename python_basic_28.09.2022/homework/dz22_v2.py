text = input('Введіть послідовність чисел (розділених комами): ')
list_01 = [int(i) for i in text.split(',')]

counter = 0
max_count = {0, }

for i in range(len(list_01)):
    if list_01[i] % 2 == 0:
        counter += 1
        max_count.add(counter)
    else:
        counter = 0

print('Найбільше парних чисел підряд: ', max(max_count))
