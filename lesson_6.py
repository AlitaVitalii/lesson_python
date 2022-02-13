# Создание списка
# list('список')
# s = []  # Пустой список
# l = ['s', 'p', ['isok'], 2]
# print(s)
# print(l)
# print(list)
#
# my_list1 = [1, 2, 3, 4, 5]
# print(my_list1)
# my_list2 = ['один', 'два', 'три', 'четыре', 'пять']
# print(my_list2)
# # # ================================
# my_list3 = ['один', 10, 2.25, [5, 15], 'пять']
# third_elem = my_list3[2]
# print(third_elem)
#
# print(third_elem)
# =================== Срез списка
# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# print(my_list[1:3])
# print(my_list[1:])
# print(my_list[:3])
# print(my_list[::-1])
# my_list[1:3]  =  ['Привет',  'Мир'] # Поскольку списки изменяемые, менять элементы можно с помощью оператора среза:
# print(my_list)
# ========== Вставить в список
# my_list = [1, 2, 3, 4, 5]
# my_list.insert(5,'Привет')
# print(my_list)
# ========================= Добавить в список
# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# my_list.append('ещё один')
# print(my_list)
#
# c = [c*3 for c in "abs"]
# c = [c*3 for c in "list"if c != "l" and c != "i"]
# c = [c + d for c in "list"if c != "i" for d in "spam" if d != "a"]
#
# print(c)
# ==================================== Sort
# prices = [159.54, 37.13, 71.17, 1.0]
# prices.sort(reverse=True)
# print(prices)
# list_2 = [3, 5, 2, 4, 1]
# list_2.sort()
# print(list_2)
# ============= Перевернуть список
# my_list = [1, 2, 3, 4, 5]
# print(my_list[::-1])
# my_list.reverse()
# print(my_list)
# ============= Индекс элемента
# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# print(my_list.index('два'))
# print(my_list[1])
# # for i in my_list:
# #  print(my_list.index(i))   # распечатать индексы списка
# print(my_list)
# temp = my_list.pop(2) #  temp = my_list.pop(my_list.index("три"))
# print(my_list)
# print(temp)

# ==========Удалить элемент
# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# removed = my_list.pop(2)
# print(my_list)
# print(removed)
# # ================ или Del
# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# del my_list[2]
# print(my_list)
#
# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# # del my_list[1:3]
# del my_list [:2]
# print(my_list)
# # =========== Функции агрегации
# my_list = [5, 3, 2, 4, 1.0]
# print(len(my_list))
# print(min(my_list))
# print(max(my_list))
# print(sum(my_list)) # sum() работает только с числовыми значениями.
# max(), len() и другие можно использовать и со строками.
# =============Сравнить списки
# my_list1 = ['один', 'два', 'три', 'четыре', 'пять']
# my_list2 = ['один', 'два', 'три', 'четыре', 'пять']
# list_2 = ['три', 'один', 'пять', 'два', 'четыре']
# print(my_list1 == my_list2 )
# print(my_list1 == list_2)


# ===================Математические операции на списках
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# print(list_1 + list_2)
# print()
#
# list_1 = [1, 2, 3]
# print(list_1  *  2)

# =============Списки и строки
# my_str = 'Monty Python'
# my_list = list(my_str)
# print(my_list)
#
# my_list = my_str.split()
# print(my_list)
# # ================== Объединить список в строку
# my_list = ['Monty', 'Python']
# delimiter = ' '
# output = delimiter.join(my_list)
# # вставляем раздилитель в список перед выводом
# print(output)
# print(" ".join(my_list))
# # =================== Алиасинг (псевдонимы)
# my_list = ['Monty', 'Python']
# list_2 = my_list
# list_2[1] = 'Java:)'
# print(my_list)
# # ================ Генерация Списка List generation
# c = [c * 3 for c in 'list']
# print(c)

# # ============================= List Comprehantion
# print([x*x for x in range(11)])
# # =============================== map
# list_of_words = ['one', 'two', 'list', '', 'dict']
# map(str.upper, list_of_words)
# print(list(map(str.upper, list_of_words)))
# # --------------------------------- Конвертация в числа:
# list_of_str = ['1', '2', '5', '10']
# print([int(x) for x in list_of_str])
# # new_list = list(map(int, list_of_str))
# # print(new_list)
# # ======================== List comprehension вместо map
# print([word.upper() for word in list_of_words])
# # =================== Форматирование строк

# vlans = [100, 110, 150, 200, 201, 202]
# print([f'vlan {x}' for x in vlans])
# # ============ Для получения пар элементов используется zip:
# nums = [1, 2, 3, 4, 5, 6]
# nums2 = [100, 200, 300, 400, 500]
# print([x * y for x, y in zip(nums, nums2)])
# # =========== zip и кортежи
# a = [1, 2, 3]
# b = [100, 200, 300]
# print(list(zip(a, b)))
# # =========== Использование zip для создания словаря
# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# d_values = ['london_r1', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.1']
# print(dict(zip(d_keys, d_values)))
#
# # ========= Tuples
# list_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
# tuple_keys = tuple(list_keys)
# print((tuple_keys))
# a = (1, 2, 3, 4, 5, 6)
# b = [1, 2, 3, 4, 5, 6]
# print(a.__sizeof__())
# print(b.__sizeof__())

# ==========
# tuple_keys[1] = 'test' # кортеж неизменяем, присвоить новое значение нельзя
# =========== Поменять местами переменными

# a = "Орел"
# b = "Решка"
# a, b = b, a
# print(a)
# print(b)
#
# # ================== Sorted
tuple_keys = ('hostname', 'location', 'vendor', 'model', 'ios', 'ip')
print(sorted(tuple_keys), type(sorted(tuple_keys)))