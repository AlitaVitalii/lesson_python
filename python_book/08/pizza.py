def make_pizza(size, *toppings):
    """

    :param size: розмір піци
    :param toppings: добавки
    :return: заказ
    """
    print(f'Вы заказали пиццу {size} с топингами:')
    for i in toppings:
        print(f' - {i}')


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
