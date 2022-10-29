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

