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
    result = []
    for i in range(num_rows):
        result.append([value] * num_cols)
    return result
#    return [[value for _ in range(num_cols)] for _ in range(num_rows)]


# board = [
#     ['.', '.', '.'],
#     ['.', '.', '.'],
#     ['.', '.', '.'],
# ]

ROWS = 9  # рядки
COLS = 9  # стовбчик

board = create_matrix(ROWS, COLS, '.')

for r in range(len(board)):
    # board[len(board) - r - 1][r] = "*"
    # board[r][len(board)-r-1] = '+'
    for i in range(r):
        # board[i][r-i-1] = '+'
        board[len(board)-i-1][i-r] = '*'
        # board[i-r][i] = '*'
        # board[i][i-r] = '+'




# for row in range(ROWS):
#     for col in range(COLS):
#         # if col == 0:
#         #     board[row][col] = '*'
#         # if row == 0:
#         #     board[row][col] = '*'
#         # if col == COLS-1:
#         #     board[row][col] = '*'
#         # if row == ROWS-1:
#         #     board[row][col] = '*'
#         for i in range(col):
#             if col == row + i +1:
#                 board[row][col] = '*'
#             if row == col + i:
#                 board[row][col] = '+'

        # for i in range(row):
        #     if row == col +i + 1:
        #         board[row][col] = "+"
        # if row == ROWS-1-col:
        #     board[row][col] = '*'

print_matrix(board)