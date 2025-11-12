def matrix_multiply(matrix1, matrix2):
    if matrix1['size_y'] != matrix2['size_x']:
        raise ValueError("Ширина первой матрицы должна равняться высоте второй матрицы")

    result_matrix = [[sum(matrix1['matrix'][i][k] * matrix2['matrix'][k][j]
                          for k in range(matrix1['size_y']))
                      for j in range(matrix2['size_y'])]
                     for i in range(matrix1['size_x'])]

    return {
        'size_x': matrix1['size_x'],
        'size_y': matrix2['size_y'],
        'matrix': result_matrix
    }


if __name__ == "__main__":
    from matrix_creator import create_matrix, matrix_to_str

    m1 = create_matrix(2, 3)
    m2 = create_matrix(3, 2)
    print("Матрица 1:\n", matrix_to_str(m1))
    print("Матрица 2:\n", matrix_to_str(m2))
    print("Результат умножения:\n", matrix_to_str(matrix_multiply(m1, m2)))
