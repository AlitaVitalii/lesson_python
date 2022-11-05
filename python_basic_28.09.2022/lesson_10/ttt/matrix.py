
def parse_coordinates(value, row_headers, col_headers):
    """ Повернути індекс рядка і шндекс стовбця
        для заданого рядка із координатами

    :param value: текстовий рядок
    :param row_headers: заголовки рядків
    :param col_headers: заголовки стовбців
    :return: tuple(row, col) або (None, None)
    """
    if len(value) == 2:
        row_index = row_headers.find(value[0])
        col_index = col_headers.find(value[1])
        if row_index >= 0 and col_index >= 0:
            return row_index, col_index

    return None, None


def print_matrix(matrix, row_headers=None, col_headers=None, delimiter=' '):
    """ Вивести в консоль дану матрицю
    :param matrix:
    :param row_headers: авс
    :param col_headers: 123
    :param delimiter: дільник
    :return:
    """
    if col_headers:
        if row_headers:
            print(' ', end=delimiter)
        print(delimiter.join(col_headers))

    for index, row in enumerate(matrix):
        if row_headers:
            print(row_headers[index], end=delimiter)
        print(delimiter.join(row))


def create_matrix(num_rows, num_cols, value):
    """ Створити та повернути 2D матрицю заданих розмірів
        заповнену заданим значенням

    :param num_rows: кількість рядків
    :param num_cols: кількість стовбців
    :param value: значення для заповнення
    :return: 2D матриця (список списків) заданих параметрів
    """
    return [[value for _ in range(num_cols)] for _ in range(num_rows)]

