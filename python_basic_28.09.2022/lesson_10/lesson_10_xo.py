from ttt.matrix import create_matrix, print_matrix, parse_coordinates

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