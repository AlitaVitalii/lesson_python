# str_1 = "some text"
# print(len(str_1))
#
# nums = [1,2,3]
# nums.append(4) #добовляет элемент в конец списка
# print(nums)
#
# words = ['Python', 'fun']
# words.insert(1, "is")  # добовляет элемент в указанную позицию
# print(words)
#
# print(words.index('is'))
# print()
#
# print(min(nums))
# print(max(nums))
# print()
#
# nums = nums*2
# nums.append(5)
# print(nums)
# print(nums.count(2))
# nums.remove(4)
# print(nums)
# nums.reverse()
# print(nums)

# spisok = ['john', 'amy', 'bob', 'adam']
# spisok.append(input())
# print(spisok)

# nums = [4,5,6]
# msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
# print(msg)
#
# print('{0}{1}{0}'.format('abra', 'cad'))

# x = " ".join(["spam", "eggs", "ham"])
# print(x)
# y = x.split()
# print(y)
# print(x.upper())
# print(x.title())


msg = input()
print(msg)
print(msg.replace("#", " "))

# def welcome(user):
#     print("Welcome " + user)
# welcome(input())

# def pr(x):
#     for i in range(x):
#         print(i)
#         return
# pr(10)



# def ser(t, w):
#     if w in t:
#         return 'Word found'
#     else:
#         return "Word not found"
#
# text = input()
# word = input()
# #
# print (ser(text, word))

# f = lambda x, y: x * y
# print(f(2, 5))

# def even_fn(x):
#     if x % 2 == 0:
#         return True
#     return False
# print(list(filter(even_fn, ([1,3,5,10,2,9,55,8]))))

# print(list(filter(lambda x: x % 2 == 0, [1,2,4,5,74,5,8,4,25,4])))

# l = [1,2,3,4]
# print(list(map(lambda x: x**2, l)))
#
# test = lambda a : True if (a > 10 and a < 20) else False
# print(test(13))
# print(test(1))
# print(test(34))