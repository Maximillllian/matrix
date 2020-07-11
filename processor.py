import numpy as np
import sys

# Программа умеет производить разные операции над матрицами. Использована библиотека numpy


def main_menu():
    while True:
        print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
        user_option = input('Your choice: > ')
        if user_option == '1':
            matrix = add_matrix()
            print_matrix(matrix)
        elif user_option == '2':
            matrix = multiple_matrix_const()
            print_matrix(matrix)
        elif user_option == '3':
            matrix = multiple_matrix()
            print_matrix(matrix)
        elif user_option == '4':
            transpose_menu()
        elif user_option == '5':
            res = det_matrix()
            print(res)
        elif user_option == '6':
            matrix = inv_matrix()
            print_matrix(matrix)
        elif user_option == '0':
            sys.exit()


def transpose_menu():
    print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
    user_option = input('Your choice: > ')
    if user_option == '1':
        matrix = main_diagonal_transpose()
        print_matrix(matrix)
    elif user_option == '2':
        matrix = side_diagonal_transpose()
        print_matrix(matrix)
    elif user_option == '3':
        matrix = vertical_line_transpose()
        print_matrix(matrix)
    elif user_option == '4':
        matrix = horizontal_line_transpose()
        print_matrix(matrix)


def add_matrix():
    matrix_1, size_matrix_1 = input_matrix()
    matrix_2, size_matrix_2 = input_matrix()
    if size_matrix_1 != size_matrix_2:
        print('\nThe operation cannot be performed\n')
        return
    else:
        res_matrix = matrix_1 + matrix_2
        return res_matrix


def multiple_matrix_const():
    matrix, size_matrix = input_matrix()
    const = int(input('Enter constant: > '))
    res_matrix = matrix * const
    return res_matrix


def multiple_matrix():
    matrix_1, size_matrix_1 = input_matrix()
    matrix_2, size_matrix_2 = input_matrix()
    if size_matrix_1[1] != size_matrix_2[0]:
        print('\nThe operation cannot be performed\n')
        return
    else:
        res_matrix = np.dot(matrix_1, matrix_2)
        return res_matrix


def det_matrix():
    matrix, size_matrix = input_matrix()
    if size_matrix[0] != size_matrix[1]:
        print('\nThe operation cannot be performed\n')
        return
    else:
        res = np.linalg.det(matrix)
        return res


def inv_matrix():
    matrix, size_matrix = input_matrix()
    return np.linalg.inv(matrix)


def main_diagonal_transpose():
    matrix, size_matrix = input_matrix()
    return matrix.transpose()


def side_diagonal_transpose():
    matrix, size_matrix = input_matrix()
    new_matrix = []
    for j in range(1, len(matrix[0]) + 1):
        vector = []
        for i in matrix[::-1]:
            vector.append(i[-j])
        new_matrix.append(vector)
    return np.array(new_matrix)


def vertical_line_transpose():
    matrix, size_matrix = input_matrix()
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(reversed(i)))
    return np.array(new_matrix)


def horizontal_line_transpose():
    matrix, size_matrix = input_matrix()
    new_matrix = []
    for i in matrix[::-1]:
        new_matrix.append(i)
    return np.array(new_matrix)


def print_matrix(matrix):
    if matrix.any():
        print('The result is:')
        for i in matrix:
            for j in i:
                print(j, end=' ')
            print()
        print()


def input_matrix():
    print()
    size_matrix = [int(size) for size in input('Enter size of matrix: > ').split()]
    print('Enter matrix:')
    matrix = np.array([[float(i) for i in input().split()] for _ in range(size_matrix[0])])
    return matrix, size_matrix


if __name__ == '__main__':
    main_menu()
