num = abs(int(input("введите число: ")))
n = 1
step = 0
mylist = []


while n <= num:
    step += 1
    n = step**2
    # mylist.append(n)
    if n <= num:  # можно обойтись без if, выводя список применив del mylist[-1]
        mylist.append(n)

# del mylist[-1]
print(f'все квадраты натуральных чисел: {mylist}')


