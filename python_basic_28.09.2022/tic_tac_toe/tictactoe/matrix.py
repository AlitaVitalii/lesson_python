def create_matrix(num_rows, num_cols, value=None):
    """ Create a 2D matrix with given dimensions filled in with given value

    :param num_rows: number of rows
    :param num_cols: number of cols
    :param value: default value for elements
    :return: 2D matrix with given parameters
    """
    return [[value for _ in range(num_cols)] for _ in range(num_rows)]


def print_matrix(matrix, row_headers=None, col_headers=None, delimiter=' '):
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

    for index, row in enumerate(matrix):
        if row_headers:
            print(row_headers[index], end=delimiter)
        print(delimiter.join(row))
