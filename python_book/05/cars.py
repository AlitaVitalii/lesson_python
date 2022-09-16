cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print()
for i in cars:
    if i != 'bmw':
        print(i.title())
    else:
        print(i.upper())