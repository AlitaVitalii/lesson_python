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
a = 1
step = 0

while a <= num:
    p_step = a
    step += 1
    a = a * 2
else:
    print(f"Показатель степени: {p_step} \nСтепень: {step-1}")
