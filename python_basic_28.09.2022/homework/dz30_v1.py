def add_thousands_separator(fn):
    def wrapper(a, b):
        result = fn(a, b)
        revers_result = str(result)[::-1]
        count = 0
        new_text_num = ""
        for i in revers_result:
            if count == 3:
                new_text_num += "'" + i
                count = 1
            else:
                new_text_num += i
                count += 1
        return new_text_num[::-1]

    return wrapper


@add_thousands_separator
def multiply(a, b):
    return a * b


print(multiply(9336, 1223))
