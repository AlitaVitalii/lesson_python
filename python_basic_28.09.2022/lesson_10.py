# # def print_matrix():
#
#
#
# def create_matrix(num_rows, num_cols, value):
#     rows = []
#     for _ in range(num_rows):
#         rows.append([value] * num_cols)
#     return rows
#
#
# ROWS = 7
# COLS = 7
#
# board = create_matrix(ROWS, COLS, '.')
#
# for row in range(ROWS):
#     for col in range(COLS):
#         if row == 0:
#             board[row][col] = '*'
#         if row
#
#
# print(board)

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))


def create_matrix(num_rows, num_cols, value):
    """ Створити та повернути 2D матрицю заданих розмірів
        заповнену заданим значенням

    :param num_rows: кількість рядків
    :param num_cols: кількість стовбців
    :param value: значення для заповнення
    :return: 2D матриця (список списків) заданих параметрів
    """
    return [[value for _ in range(num_cols)] for _ in range(num_rows)]


# board = [
#     ['.', '.', '.'],
#     ['.', '.', '.'],
#     ['.', '.', '.'],
# ]

ROWS = 7
COLS = 7

board = create_matrix(ROWS, COLS, '.')

for row in range(ROWS):
    for col in range(COLS):
        if row == 0:
            board[row][col] = '*'
        if row == ROWS - 1:
            board[row][col] = '*'
        if col == 0:
            board[row][col] = '*'
        if col == COLS - 1:
            board[row][col] = '*'
        if row == col:
            board[row][col] = '*'
        if row == COLS - 1 - col:
            board[row][col] = '*'


print_matrix(board)


print('--------------1')

a = [False, True, True]

print(any(a))

print(a[0] or a[1] or a[2])


b = [True, True, True]

print(all(b))

print(b[0] and b[1] and b[2])