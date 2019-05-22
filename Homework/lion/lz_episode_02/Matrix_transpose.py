# -*- coding: utf-8 -*-


def originate_matrix():
    """ 将输入的字符串转化为矩阵 """
    matrix_str = input('请输入待转置的矩阵,行与行之间以‘,’分割（示例：（123,456））：')
    matrix_str = matrix_str.split(',')
    matrix = [[] for i in matrix_str]  # 存放字符串转化的矩阵
    row = 0  # 行号
    for i in matrix_str:
        for c in i:
            matrix[row].append(int(c))
        row += 1
    return matrix


def transpose_matrix(matrix):
    # 将行、列倒置，取列最长的行的长度 为新矩阵的行
    max_length = 0
    for i in matrix:
        if len(i) > max_length:
            max_length = len(i)
    matrix_transpose = [[] for i in range(max_length)]

    for row in matrix:
        for i in range(len(row)):
            matrix_transpose[i].append(row[i])
    print(matrix_transpose)
    return matrix_transpose


def main():
    matrix = originate_matrix()
    transpose_matrix(matrix)


if __name__ == '__main__':
    main()
