# for number in [0, 1, 2, 3, 4]:
#     print(number)
#
# for num in range(10, 50, 10):
#     print(num)
# else:
#     print("числа закончились")
#
# print(len(list(range(10,50)))) #len - длина списка

# mystr = "привет Пайтон!"
# line_str = "-" * len(mystr)
# print(f'{mystr}\n{line_str}')



# for num in range(5):
#     if num == 3:
#         break
#     else:
#         print(num)
# else:
#     print("числа закончились")
#


# import random
# print(random.randrange(3, 9))
# print(random.random())


# import time
# print(time.time())
# time.sleep(5)
# print(time.time())



# i = 0
# while i < 5:
#     if i == 3:
#         continue   #получается замкнутый цикл, нужно +1 поставить до континью
#     print(i)
#     i += 1
# else:
#     print("the end")


# import time
# end_time = time.time() + 20
# while time.time() < end_time:
#     time.sleep(5)
#     print("Прошло 5 сек")
# else:
#     print("Alarm")


# def generator():
#     for num in range(10):


# print(list(range(0)))
# print(list(range(2, 1, 3)))
#
# print(list(range(0, 3, 2)))
# print(list(range(0, 4, 2)))


# for n, i in enumerate(range(0, 7, 2), 1):
#     print(f'{n}) =-> {i}')
# print()
#
# for n, i in enumerate(range(-7, 0, 2), 1):
#     print(f'{n}) =-> {abs(i)}')


mylist = ['apple', 'banana', 'cherry', 'pear', 'plum']
# for i in range(len(mylist)):
#     print(mylist[i])

print(len(mylist))

# mylist = []
# for n in range(30):
#     x = 2**n
#     mylist.append(x)
#
# num = abs(int(input("введите число: ")))
#
# for n in mylist:
#     if num // n == 1:
#         print(f"Для числа: {num}")
#         print(f"степень: {mylist.index(n)}")
#         print(f"показатель степени: {n}")