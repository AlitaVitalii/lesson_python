my_list = [i for i in range(1, 10)]

for i in my_list:
    if i == 1:
        print(f'{i}st')
    elif i == 2:
        print(f'{i}nd')
    elif i == 3:
        print(f'{i}rd')
    else:
        print(f"{i}th")

