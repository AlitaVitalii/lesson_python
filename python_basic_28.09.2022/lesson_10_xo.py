
def print_matrix(matrix, row_headers=None, col_headers=None, delimiter=' '):
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


def parse_coordinates(value, row_headers, col_headers):
    if len(value) == 2:
        row_index = row_headers.find(value[0])
        col_index = col_headers.find(value[1])
        if row_index >= 0 and col_index >= 0:
            return row_index, col_index

    return None, None


ROWS = 3
COLS = 3

ROW_HEADERS = 'abc'
COL_HEADERS = '123'

CROSS = 'x'
ZERO = 'o'
EMPTY = '.'

sides = {
    CROSS: "Хрестики",
    ZERO: "Нолики",
}

board = create_matrix(ROWS, COLS, EMPTY)

next_turn = CROSS

while True:
    print("Ігрове поле: ")
    print_matrix(board, row_headers=ROW_HEADERS, col_headers=COL_HEADERS)


    coord = input(f"{sides[next_turn]}, ваш хід: ")
    row, col = parse_coordinates(
        coord,
        row_headers=ROW_HEADERS,
        col_headers=COL_HEADERS
    )
    if (row, col) == (None, None) or board[row][col] != EMPTY:
        print("Некоректні координати!")
    else:
        board[row][col] = next_turn
        next_turn = CROSS if next_turn == ZERO else ZERO

    print('-----------')