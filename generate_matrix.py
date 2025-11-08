from random import randint

def create_matrix(x, y):
    return {
        'size_x': x,
        'size_y': y,
        'matrix': [[randint(1, 10) for j in range(y)] for i in range(x)]
    }

def matrix_to_str(matrix):
    return "\n".join(", ".join(str(j) for j in i) for i in matrix['matrix'])

if __name__ == "__main__":
    test_matrix = create_matrix(2, 3)
    print("Создание матрицы:")
    print(matrix_to_str(test_matrix))