
text = input('Введіть дані: ')
list_01 = [int(i) for i in text.split(',')]

counter = 0
max_count = 0

for i in range(len(list_01)-1):
    if list_01[i] % 2 == 0 and list_01[i+1] % 2 == 0:
        counter += 1
        if max_count <= counter:
            max_count = counter + 1
    else:
        counter = 0

print('Найбільше парних чисел підряд: ', max_count)
