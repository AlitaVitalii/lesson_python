class Matrix:
    def __init__(self, num_rows, num_cols, value='.'):
        """ Initialize 2D matrix

        :param num_rows: number of rows
        :param num_cols: number of cols
        :param value: default value for elements
        """
        self._data = [[value for _ in range(num_cols)] for _ in range(num_rows)]

    @property
    def data(self):
        return self._data

    def __str__(self):
        result = ''
        for row in self._data:
            result += ' '.join(row) + '\n'

        return result

    def print_matrix(self, row_headers=None, col_headers=None, delimiter=' '):
        """ Print given 2D matrix to console

        :param matrix: 2D matrix
        :param delimiter: delimiter between elements in a row
        :param row_headers: headers for rows (optional)
        :param col_headers: headers for columns (optional)
        :return: None
        """
        if col_headers:
            if row_headers:
                print(' ', end=delimiter)
            print(delimiter.join(col_headers))

        for index, row in enumerate(self._data):
            if row_headers:
                print(row_headers[index], end=delimiter)
            print(delimiter.join(row))
