def parse_coordinates(value, row_headers, col_headers):
    """ Return row and column index for given coordinates string

        For example, when columns are titled 'abc' and rows '123':
            'a1' => 0, 0
            'b3' => 2, 1
            'z9' => None, None

    :param value: coordinates string
    :param row_headers:
    :param col_headers:
    :return: tuple(row, col) (Nones if not parsed)
    """
    if len(value) == 2:
        row_index = row_headers.find(value[1])
        col_index = col_headers.find(value[0])
        if row_index >= 0 and col_index >= 0:
            return row_index, col_index

    return None, None


def has_full_row(matrix, element):
    """ Return True if the element occupies any row, column or diagonal
        in a given matrix

    :param matrix: 2D matrix
    :param element: element to check
    :return: True if element had won else False
    """
    size = len(matrix)

    # horizontals
    for row in matrix:
        counter = 0
        max_count = {0, }
        for cell in row:
            if cell == element:
                counter += 1
                max_count.add(counter)
            else:
                counter = 0
        if max(max_count) == 5:
            return True

    # for row in matrix:
        # if all([cell == element for cell in row]):
        #     return True

    # verticals
    for col_index in range(size):
        counter = 0
        max_count = {0, }
        for row in matrix:
            if row[col_index] == element:
                counter += 1
                max_count.add(counter)
            else:
                counter = 0
        if max(max_count) == 5:
            return True
        # if all([row[col_index] == element for row in matrix]):
        #     return True

    # \\ diagonal
    counter = 0
    max_count = {0, }
    for r in range(size):
        for i in range(r):
            if matrix[i][i-r] == element or matrix[i-r][i] == element:
                counter += 1
                max_count.add(counter)
            else:
                counter = 0
    if max(max_count) == 5:
        return True

        # // diagonal
    counter = 0
    max_count = {0, }
    for r in range(size):
        for i in range(r):
            if matrix[i][r - i - 1] == element or matrix[size - i - 1][i - r] == element:
                counter += 1
                max_count.add(counter)
            else:
                counter = 0
    if max(max_count) == 5:
        return True


    # if all([matrix[r][r] == element for r in range(size)]):
    #     return True

    # \/ diagonal
    counter = 0
    max_count = {0, }
    for r in range(size):
        if matrix[r][size-r-1] == element or matrix[r][r] == element:
            counter += 1
            max_count.add(counter)
        else:
            counter = 0
    if max(max_count) == 5:
        return True
    # if all([matrix[r][size - r - 1] == element for r in range(size)]):
    #     return True

    return False


def count_elements(matrix, element):
    """ Count of the given element entries in the given 2D matrix

    :param matrix: 2D matrix
    :param element: element to count
    :return: number of element entries in a matrix
    """
    count = 0
    for row in matrix:
        for cell in row:
            if cell == element:
                count += 1
    return count


def is_game_over(matrix, cross, zero, empty):
    """ Return True if TicTacToe board has a victory position for any sides or the board is full

        :param matrix: 2D matrix with game board
        :param cross: char for Cross representation
        :param zero: char for Zero representation
        :param empty: char for empty cell representation
    """
    return any([
        has_full_row(matrix, cross),
        has_full_row(matrix, zero),
        count_elements(matrix, empty) == 0,
    ])
