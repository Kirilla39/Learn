from generate_matrix import create_matrix, matrix_to_str
from addition import matrix_add
from multiplication import matrix_multiply

def main():
    m1 = create_matrix(0, 0)
    m2 = create_matrix(0, 0)
    command = "F"
    
    while command != "Q":
        match command:
            case "H":
                print("H - помощь")
                print("V - показать матрицы")
                print("F - создать новые матрицы")
                print("+ - сложение матриц")
                print("* - умножение матриц")
                print("Q - выход\n")
                
            case "F":
                try:
                    m1x, m1y, m2x, m2y = map(int, input("Введите размеры двух матриц через пробел (x1 y1 x2 y2): ").split())
                    m1 = create_matrix(m1x, m1y)
                    m2 = create_matrix(m2x, m2y)
                    print("Матрицы созданы!")
                except ValueError:
                    print("Ошибка: введите 4 целых числа через пробел")
                    
            case "V":
                print("Текущие матрицы:")
                print("Матрица 1:\n", matrix_to_str(m1), sep="")
                print("\nМатрица 2:\n", matrix_to_str(m2), sep="")
                
            case "+":
                try:
                    result = matrix_add(m1, m2)
                    print("Результат сложения:\n", matrix_to_str(result), sep="")
                except ValueError as e:
                    print(f"Ошибка: {e}")
                    
            case "*":
                try:
                    result = matrix_multiply(m1, m2)
                    print("Результат умножения:\n", matrix_to_str(result), sep="")
                except ValueError as e:
                    print(f"Ошибка: {e}")
                    
            case "Q":
                print("Выход из программы...")
                break
                
            case _:
                print("Неизвестная команда. H - для списка действий")

        command = input("\nВведите действие (H - для списка действий): ").upper()

if __name__ == "__main__":
    main()
