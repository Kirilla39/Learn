def matrix_transpose(matrix):
    transposed_matrix = [[matrix['matrix'][j][i] for j in range(matrix['size_x'])] 
                        for i in range(matrix['size_y'])]
    
    return {
        'size_x': matrix['size_y'],
        'size_y': matrix['size_x'],
        'matrix': transposed_matrix
    }

if __name__ == "__main__":
    from matrix_creator import create_matrix, matrix_to_str
    
    test_matrix = create_matrix(2, 3)
    print("Исходная матрица:\n", matrix_to_str(test_matrix))
    print("Транспонированная матрица:\n", matrix_to_str(matrix_transpose(test_matrix)))
