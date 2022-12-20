# # s3 = r'C:\doc'
# # # s4 = r'\n\n\\'[:-1]
# # s4 =
# #
# # print(s4)
#
# # s1 = 'spam"s'
# # s2 = "spam’s"
# # s3 = r'C:\Users\igor_petrushchak\111111\lesson_5.py'
# # s4 = r'\n\n\\'[:-1]
# # s5 = r'\n\n' + '\\'
# # s6 = '\\n\\n'
# # s3= 'это очень большая\nстрока, многострочный\nблок текста'
# #
# # print(s1[6])
# # print(s1 + s2)
# # print(s1 * 50)
# # print(len(s1))
#
# # print(s1[0]+s1[2]+s1[-2])
#
# s = 'Hello\nWorld'
# # print(s[3:5])
# # print(s[2:-2])
# # print(s[:6])
# # print()
# # ==============================
# # s = 'spam'
# # s[1] = 'b'
# s=str(321)
# s = s[0] + 'b' + s[2:]
# print(s)
# s2 = ''
# for letter in range(len(s)-1,-1,-1):
#     s2 += s[letter]
# print(s2)
#
# # print(s2)
# # #
# print(s[::5])
# ================================
import random

#
# print(random.random())
# # =================================
from random import randint, randrange

#
# print("Вывод случайного целого числа ", randint(0,10))
# print("Вывод случайного целого числа ", randrange(0, 10, 2))
# # # # =================================
# city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
# # print(city_list[random.randint(0, len(city_list)-1)])
# # print("Выбор случайного города из списка - ", random.choice(city_list))
# phase = "Выбор случайного города из списка"
# new_phase = phase.split(" ")
# print(type(new_phase))
# print(random.choice(new_phase))
#
# # # =================================
# #
# # print("Использование random.randint() для генерации случайного целого числа")
# # print(random.randint(0, 5))
# # print(random.randint(0, 5))
# # ==================================
# #
# list = [20, 30, 40, 50, 60, 70, 80, 90]
# list_of_numbers = random.choices(list, k=5)
# print(f"Выборка с методом choices {list_of_numbers}")
# # # ===================================
#
#
# # Пишем программу выбора одежды на работу
#
# closes_list = ['Пиджак', 'Рубашка', 'Платье', 'Футболка', 'Шляпа', 'Брюки',
#                'Носки', 'Шуба', 'Кепка', 'Тапки', 'Платок',
#                'Плавки']
# print("Выбор случайной одежды из списка - ", random.sample(closes_list, k=3))
