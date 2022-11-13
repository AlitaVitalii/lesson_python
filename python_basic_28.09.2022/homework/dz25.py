def rotate_matrix(source_matrix):
    """повертає значення елементів матриці, повернутої на 90°

    :param source_matrix: 2D матриця (список списків)
    :return:2D матриця повернута на 90° (список списків)
    """
    size_row = len(source_matrix[0])
    result_list = []
    for ind in range(size_row):
        temp_list = []
        for row in source_matrix:
            temp_list.append(row[ind])
        temp_list.reverse()
        result_list.append(temp_list)
    return result_list


def print_matrix(matrix):
    """ Виводить в консоль значення елементів матриці

    :param matrix: 2D матриця (список списків)
    :return: None
    """
    for row in matrix:
        print(' '.join(row))


print('Введіть з клавіатури значення елементів матриці розміром 3 × 4 елементи. '
      '\nЕлементи рядка вводяться через кому\n')

rows = []
for i in range(3):
    new_row = input(f"Введіть дані рядка {i + 1}: ").split(',')
    if len(new_row) == 4:
        rows.append(new_row)
    else:
        print('Некоректні дані!')
        break

if len(rows) == 3:
    rotate_rows = rotate_matrix(rows)
    print_matrix(rotate_rows)
