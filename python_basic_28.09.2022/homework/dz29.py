def fibonacci_gen(num):
    num_1 = 1
    num_2 = 0
    for i in range(num):
        num_3 = num_1 + num_2
        num_1 = num_2
        num_2 = num_3
        yield num_3


for f in fibonacci_gen(10):
    print(f)
