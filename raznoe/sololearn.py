# total = 0
# s = 0
# while total < 5:
#     age = int(input())
#     if age > 3:
#         s += 100
#     total += 1
#
# print(s)
# ves = float(input("vvedite ves: "))
# rost = float(input("vvedite rost: "))
# imt = ves/rost**2
#
# if imt < 18.5:
#     print("Underweight")
# elif 18.5 <= imt < 25:
#     print('Normal')
# elif 25 <= imt < 30:
#     print("Overweight")
# else:
#     print('Obesity')
#
# # print(imt)

# x = [2, 4]
# x += [6, 8]
# print(x[2]//x[0])
# print(x)

# nums = [1,2,3]
# print(nums*3)

# x = [1, 4, 45, 47, 8, 9, 10]
# num = int(input())
# if num in x:
#     print('bingo')

# str = 'testing for loops'
# count = 0
# for x in str:
#     if x == 't':
#         count += 1
# print(count)

# x = [1, 4, 45, 47, 8, 9, 10]
# s= 0
# for num in x:
#     s = s + num
# print(s)

# nums = [1,2,3,4]
# res = 0
# for x in nums:
#     if x%2 == 0:
#         continue
#     else:
#         res += x
# print(res)

# nums = list(range(0, 20 ,2))
# print(nums)

# a = int(input())
# b = int(input())
#
# x= list(range(a, b))
# print(x)

# list = [0,1,4,9,16,25,36,49,64,81]
# print(list[list[4]])
# #
# text = input()
# print(text[-1])

n = int(input())
total = 0
for i in range(0, n+1):
    total += i
print(total)

# for i in range(0,n+1):
#     x = str(i)
#     total += int(x[0])
# print(total)
