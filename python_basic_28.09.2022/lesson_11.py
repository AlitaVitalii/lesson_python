def my_sort(source):
    result = source.copy()
    had_swaps = True
    while had_swaps:
        had_swaps = False
        for i in range(1, len(result)):
            if result[i] < result[i - 1]:
                result[i - 1], result[i] = result[i], result[i - 1]
                had_swaps = True
        print(result)

    return result


# my_list = [38, 4, 22, 18, 17, 34, 0, 100]

my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(my_sort(my_list))


print('----------------------1')


def vertical_print(text):
    if text:
        print(text[0])
        vertical_print(text[1:])
    # for c in text:
    #     print(c)


vertical_print("Hello!")

print('-----------------------------2')

import sys

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)
    # result = 1
    # for i in range(2, n + 1):
    #     result *= i
    #
    # return result

print(sys.getrecursionlimit())
sys.setrecursionlimit(20)

# print(factorial(999))

print('----------------------------3')

