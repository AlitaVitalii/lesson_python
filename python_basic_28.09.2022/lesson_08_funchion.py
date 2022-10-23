from time import sleep


def teletype(text):
    for c in text:
        sleep(0.1)
        print(c, end="")
    sleep(0.5)
    print()


teletype("Wake up, Neo. Wake up.")
teletype("The Matrix has got you.")
teletype("Follow the white rabbit.")
teletype("Knock, knock, Neo.")

print('--------------------1')


def double(number):
    return number * 2


def square_root(number):
    return number ** .5


print(square_root(double(2)))

print('---------------2')


def my_func(*args, **kwargs):
    print(args)
    print(kwargs)


my_func(1, 2, 3, arg_01=4, arg_02=5, message="Hello")

print('-----------------3')


def my_func_02(*args, message):
    print(args)
    print(message)


my_func_02(1, 2, 3, message="Hey")

print('--------------4')

print(1, 2, 3, end=" The end.", sep=" +++ ")

print('=============5')


def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


def calculate(func, a, b):
    # if func_name == 'add':
    #     print(a, b, add_numbers(a, b))
    # elif func_name == 'multiply':
    #     print(a, b, multiply_numbers(a, b))
    print(a, b, func(a, b))


calculate(add_numbers, 3, 5)
