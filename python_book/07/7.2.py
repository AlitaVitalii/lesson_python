zakaz = int(input("введите количество мест: "))
if zakaz < 8:
    print(f'Вы за бронировали в нашем кафе стол на {zakaz} мест.')
else:
    print(f'К сожаленнию у нас нет возможности забранировать стол на {zakaz} мест, обратитесь пожалуйста позже.')