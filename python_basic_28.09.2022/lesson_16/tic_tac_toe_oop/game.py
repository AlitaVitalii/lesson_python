from matrix import Matrix


class TicTacToeGame:

    def __init__(self, row_headers, col_headers, cross='X', zero='O', empty='.'):
        self._row_headers = row_headers
        self._col_headers = col_headers
        self._cross = cross
        self._zero = zero
        self._empty = empty
        self._matrix = Matrix(3, 3, value=empty)

    def print_matrix(self):
        self._matrix.print_matrix(row_headers=self._row_headers, col_headers=self._col_headers)

    def parse_coordinates(self, value):
        """ Return row and column index for given coordinates string

            For example, when columns are titled 'abc' and rows '123':
                'a1' => 0, 0
                'b3' => 2, 1
                'z9' => None, None

        :param value: coordinates string
        :return: tuple(row, col) (Nones if not parsed)
        """
        if len(value) == 2:
            row_index = self._row_headers.find(value[1])
            col_index = self._col_headers.find(value[0])
            if row_index >= 0 and col_index >= 0:
                return row_index, col_index

        return None, None

    def has_full_row(self, element):
        """ Return True if the element occupies any row, column or diagonal
            in a given matrix

        :param element: element to check
        :return: True if element had won else False
        """
        size = len(self._matrix.data)

        # horizontals
        for row in self._matrix.data:
            if all([cell == element for cell in row]):
                return True

        # verticals
        for col_index in range(size):
            if all([row[col_index] == element for row in self._matrix.data]):
                return True

        # \ diagonal
        if all([self._matrix.data[r][r] == element for r in range(size)]):
            return True

        # / diagonal
        if all([self._matrix.data[r][size - r - 1] == element for r in range(size)]):
            return True

        return False

    def count_elements(self, element):
        """ Count of the given element entries in the given 2D matrix

        :param element: element to count
        :return: number of element entries in a matrix
        """
        count = 0
        for row in self._matrix.data:
            for cell in row:
                if cell == element:
                    count += 1
        return count

    def is_game_over(self):
        """ Return True if TicTacToe board has a victory position for any sides or the board is full

            :param cross: char for Cross representation
            :param zero: char for Zero representation
            :param empty: char for empty cell representation
        """
        return any([
            self.has_full_row(self._cross),
            self.has_full_row(self._zero),
            self.count_elements(self._empty) == 0,
        ])
