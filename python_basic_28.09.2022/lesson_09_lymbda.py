goods = [
    {
        'name': "TV set",
        'price': 900,
        'weight': 7,
    },
    {
        'name': "Laptop",
        'price': 1200,
        'weight': 2,
    },
    {
        'name': "Lamp",
        'price': 20,
        'weight': 1,
    },
    {
        'name': "Stereo System",
        'price': 900,
        'weight': 35,
    }
]


def get_item_weight(item):
    return item['weight']


for item in sorted(goods, key=get_item_weight):
    print(item)

print('_____________--1')


def get_item_weight(item):
    return item['weight']


def get_item_price(item):
    return item['price']


for item in sorted(goods, key=get_item_price):
    print(item)

print('---------------2')

for item in sorted(goods, key=lambda i: len(i['name'])):
    print(item)

print('-----------------3')

from random import choice, sample

color = ['green', 'red', 'blu', 'yellow']
for i in range(10):
    print(choice(color))

for i in range(10):
    print(sample(color, 3))

print('______________4')


from math import floor, ceil, pi, e

print(floor(2.1))
print(floor(2.9))

print(ceil(2.1))
print(ceil(2.9))

print(round(2.5))  # банківське заокруглення
print(round(3.5))

print(round(3.432432458908945, 6))
print(round(3.432432458908945, 3))
print(pi)
print(e)

print('______________--------5')

import random as r

r.seed(0)  # не случайная случайность

for i in range(10):
    print(int(r.random() * 2000 - 1000))

from random import seed as my_seed, random as my_random

my_seed(0)

for i in range(10):
    print(int(my_random() * 2000 - 1000))

print('------------------6')

from random import seed, random, randrange

my_list = list(range(1, 20, 2))
print(my_list)

for i in range(10):
    print(randrange(1, 20, 2))

print('-------------------7')

from random import randint

for i in range(10):
    print(randint(20, 30))

print('--------------------8')

from random import choice

color = ['green', 'yellow', 'red']

for i in range(10):
    print(choice(color))

from random import shuffle

color = ['green', 'yellow', 'red', 'orange', 'violet', 'brown']

for i in range(10):
    shuffle(color)
    print(color)

print('-------------------10')

from random import sample

color = ['green', 'yellow', 'red', 'orange', 'violet', 'brown']

for i in range(10):
    print(sample(color, 3))

print(color)