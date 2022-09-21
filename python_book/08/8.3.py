def make_shirt(message: object, size: object = 'L') -> object:
    print(f'Размер футболки - {size.title()}'
          f'\nТекст на футболке: \n{message}')


make_shirt('ptnhlo')
make_shirt(size='l', message='ПТНХЛО')


def describe_citi(citi, country="Ukraine"):
    print(f'{citi.title()} is in {country.title()}')


describe_citi('kiyv')
