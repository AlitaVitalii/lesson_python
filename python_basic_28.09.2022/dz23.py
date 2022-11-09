# text = "55, 60, 40, 73, 52, 62, 45, 54, 65, 50, 59, 49, 55, 52"
text = input('Введіть набір значень, через кому: ')
my_list = [int(i) for i in text.split(',')]

list_result = []
first_index = 0
for index in range(len(my_list)):
    index += 1
    if index <= 7:
        list_result.append(round(sum(my_list[first_index:index]) / len(my_list[first_index:index]), 1))
    else:
        first_index += 1
        list_result.append(round(sum(my_list[first_index:index]) / len(my_list[first_index:index]), 1))

print(list_result)
