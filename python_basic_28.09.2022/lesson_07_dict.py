prices = {
    'tv': 300,
    'vcr': 50,
    'dvd': 150,
}


print("Keys:")
for key in prices.keys():
    print(key)

print("Values:")
for value in prices.values():
    print(value, type(value))

print("Items:")
for key, value in prices.items():
    print(key, value)

print("Keys (with values):")
for key in prices.keys():
    print(key, prices[key])


print('-------------1')

prices = {
    'tv': 300,
    'vcr': 50,
    'dvd': 150,
}

key = 'tv'

if key in prices:
    print(prices[key])
else:
    print(f"Key '{key}' not found")

print("the end.")

#ili

print(prices.get(key, 'такой переменной нет'))

print('---------2')

prices = {
    'tv': 300,
    'vcr': 50,
    'dvd': 150,
    'telescope': None,
}

key = 'tv'

print(prices.pop(key, "Not found"))
print(prices)

print('----------------3')

prices = {
    'tv': 300,
    'vcr': 50,
    'dvd': 150,
    'telescope': None,
}

extra_prices = {
    'camera': 500,
    'fridge': 800,
    'vacuum': 550
}

prices.update(extra_prices)

print(prices)

print('------------4')

prices = {
    'tv': 300,
    'vcr': 50,
    'dvd': 150,
    'telescope': None,
}

prices.setdefault('tv', 550)
print(prices)

prices.setdefault('camera', 550)
print(prices)

print('---------------5')

prices2 = dict.fromkeys(['foo', 'bar', 'baz'])
print(prices2)

print('----------------6')

answer = input("Який колір світлофора? ")

message = {
    'червоний': "Стій.",
    'жовтий': "Приготуйся.",
    'зелений': "Іди."
}.get(answer, "Не знаю такого кольору.")

print(message)