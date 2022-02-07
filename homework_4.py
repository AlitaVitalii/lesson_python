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

num = abs(int(input("введите число: ")))
step = 1
n = 0

while step <= num:
    p_step = step
    n += 1
    step = step * 2
else:
    print(f"Показатель степени: {p_step} \nСтепень: {n-1}")
