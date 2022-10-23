def input_integers_list(prompt_text='', values_separator=','):
    text = input(prompt_text)
    my_list = [int(i) for i in text.split(values_separator)]
    return my_list


list_01 = input_integers_list('Введіть через пробіл суми ваших покупок (по чекам) за тиждень: ', ' ')

print('Середня сума чеку: ', sum(list_01)/len(list_01))
print('Ваши витрати на день: ', sum(list_01)/7)
print('Ваша найбільша покупка: ', max(list_01))
print('Ваша найменьша покупка: ', min(list_01))
print('Сума ваших покупок за тиждень: ', sum(list_01))


