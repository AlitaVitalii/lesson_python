def add_thousands_separator(fn):
    def wrapper(a, b):
        result = fn(a, b)
        r_thousand_separator = f'{result:,}'
        return r_thousand_separator.replace(",", "'")

    return wrapper


@add_thousands_separator
def multiply(a, b):
    return a * b


print(multiply(9336, 1223))
