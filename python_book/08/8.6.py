def city_country(citi, country):
    c_k = f'{citi.title()}, {country.title()}'
    return c_k


kiyv = f"{city_country('kiyv', 'ukraine')}"
berlin = city_country('berlin', 'gemany')

print(kiyv)
print(berlin)