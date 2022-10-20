text = input('Введіть текст: ')

my_list = [i.lower() for i in text if i.isalpha()]
my_list_set_sorted = sorted(list(set(my_list)))

for letter_unique in my_list_set_sorted:
    sum_letter = my_list.count(letter_unique)
    print(f'"{letter_unique}": {sum_letter}')
