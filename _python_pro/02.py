def func(s):
    result = []
    # my_list = s.split()
    for i in s.split():
        if len(i) >= 5:
            result.append(i[::-1])
        else:
            result.append(i)
    return ' '.join(result)


print(func('helloo word'))