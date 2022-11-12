from datetime import datetime

now = datetime.now()
print(now)

tomorrow = datetime(year=2022, month=11, day=1, hour=22, minute=30, second=55)

print(tomorrow.strftime('%Y/%m/%d, %A'))
print(f"{tomorrow.year}/{tomorrow.month}/{tomorrow.day:02d}")
# print(now.strftime())

print(':::::::::::::1')

from datetime import datetime, timedelta

d = '2022-11-09 00:00'

dt = datetime.strptime(d, '%Y-%m-%d %H:%M')
print(dt)

print(dt + timedelta(days=134, hours=2, minutes=3, seconds=4, milliseconds=5, microseconds=6))

print('======================2')

from datetime import datetime, date, timedelta

dt = datetime(2022, 1, 1)
dd = date(2022, 11, 9)


print(dd - dt.date())
print(datetime.fromordinal(dd.toordinal()) - dt)

print('------------------3')

from datetime import datetime, date, timedelta

dt = datetime(2022, 1, 1)
dd = date(2022, 11, 9)


print(dd - dt.date())
print((datetime.fromordinal(dd.toordinal()) - dt).days)

print('---------def-------------4')

import random


def random_numbers():
    while True:
        yield random.randint(0, 100)


for count, number in enumerate(random_numbers()):
    print(number)
    if count > 15:
        break

print('------------------------5')

def add_one(fn):

    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        print("original value =", res)
        return res + 1

    return wrapper


@add_one
def add(a, b):
    return a + b


print(add(2, 3))

print('------------------------6')

def add_one(fn):

    def wrapper(*args, **kwargs):
        print(f"Calling function {fn.__name__} with args {args} and kwargs {kwargs}")
        res = fn(*args, **kwargs)
        print("original value =", res)
        return res + 1

    return wrapper


@add_one
def add(a, b):
    return a + b


@add_one
def mul(a, b):
    return a * b


@add_one
def div(a1, a2):
    return a1 / a2


@add_one
def my_sum(a, b, c):
    return a + b + c


print(add(2, 3))
print(mul(2, 2))
print(div(12, 4))
print(my_sum(1, 2, 3))

print('-------------------7')

from functools import wraps


def add_one(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Calling function {fn.__name__} with args {args} and kwargs {kwargs}")
        res = fn(*args, **kwargs)
        print("original value =", res)
        return res + 1

    return wrapper


@add_one
def add(a, b):
    return a + b


print(add.__name__)

