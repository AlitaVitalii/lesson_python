num = abs(int(input("введите число: ")))
n = 1
step = 0

while n <= num:
    p_step = n
    step += 1
    n = n * 2
else:
    print(f"Показатель степени: {p_step} \nСтепень: {step-1}")
