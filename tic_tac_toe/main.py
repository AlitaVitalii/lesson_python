from tictactoe import parse_coordinates, is_game_over, has_full_row, create_matrix, print_matrix


CROSS = 'x'
ZERO = 'o'
EMPTY = '.'

ROW_HEADERS = '123456789'
COL_HEADERS = 'abcdefghi'

sides = {
    CROSS: "Хрестики",
    ZERO: "Нолики",
}

next_turn = CROSS

board = create_matrix(9, 9, value='.')

while True:
    print("Ігрове поле:")
    print_matrix(
        board,
        row_headers=ROW_HEADERS,
        col_headers=COL_HEADERS,
        delimiter='  '
    )
    print('------------')

    if is_game_over(board, cross=CROSS, zero=ZERO, empty=EMPTY):
        if has_full_row(board, CROSS):
            print("Хрестики виграли!")
        elif has_full_row(board, ZERO):
            print("Нолики виграли!")
        else:
            print("Нічия!")

        print("Це була крута гра. Приходьте ще!")
        break

    print(f"{sides[next_turn]}, ваш хід!")

    while True:
        pos = parse_coordinates(
            input("Введіть координати: "),
            row_headers=ROW_HEADERS,
            col_headers=COL_HEADERS,
        )
        if pos == (None, None) or board[pos[0]][pos[1]] != EMPTY:
            print("Некоректні координати")
        else:
            board[pos[0]][pos[1]] = next_turn
            next_turn = CROSS if next_turn == ZERO else ZERO
            print()  # just an empty row
            break
