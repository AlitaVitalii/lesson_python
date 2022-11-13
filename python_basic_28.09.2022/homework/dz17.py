def cars(prompt_text=''):
    text = input(prompt_text)
    if text:
        my_list = [i for i in text.split('/')]
        my_dict = {
            'model': my_list[0],
            'max_speed': int(my_list[1]),
            'engine': {
                'capacity': int(my_list[2]),
                'power': int(my_list[3])
            }
        }
        return my_dict
    else:
        return None


list_car = []
while True:
    dict_car = cars('Введіть дані про авто (модель/швидкість/об’єм двигуна/потужність): ')
    if dict_car:
        list_car.append(dict_car)
    else:
        break

for car in sorted(list_car, key=lambda i: i['engine']['power']):
    print(car)
