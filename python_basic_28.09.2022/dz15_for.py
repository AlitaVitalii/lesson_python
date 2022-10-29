def is_prime(number):
    """ Повернути True якщо число є простим або False якщо не є простим
    :param number: число для перевірки
    :return: bool
    """
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


min_num = int(input("Введіть нижню межу: "))
max_num = int(input("Введіть верхню межу: "))

primes_count = 0
for i in range(min_num, max_num + 1):
    if is_prime(i):
        print(i)
        primes_count += 1

print("Знайдено цілих чисел:", primes_count)