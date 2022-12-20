from game import TicTacToeGame

CROSS = 'x'
ZERO = 'o'
EMPTY = '.'

ROW_HEADERS = '123'
COL_HEADERS = 'abc'

sides = {
    CROSS: "Хрестики",
    ZERO: "Нолики",
}

next_turn = CROSS

game = TicTacToeGame(row_headers='123', col_headers='abc', cross=CROSS, zero=ZERO, empty=EMPTY)

while True:
    print("Ігрове поле:")
    game.print_matrix()

    print('------------')
    if game.is_game_over():
        if game.has_full_row(CROSS):
            print("Хрестики виграли!")
        elif game.has_full_row(ZERO):
            print("Нолики виграли!")
        else:
            print("Нічия!")

        print("Це була крута гра. Приходьте ще!")
        break

    print(f"{sides[next_turn]}, ваш хід!")

    while True:
        pos = game.parse_coordinates(input("Введіть координати: "))
        if pos == (None, None) or game._matrix.data[pos[0]][pos[1]] != EMPTY:
            print("Некоректні координати")
        else:
            game._matrix.data[pos[0]][pos[1]] = next_turn
            # game.board[pos[0]][pos[1]] = next_turn   <== homework
            next_turn = CROSS if next_turn == ZERO else ZERO
            print()  # just an empty row
            break
