""" 矩阵转置 """


def matrix_transpose(matrix):
    new_matrix = [
        [
            matrix[i][j] for i in range(len(matrix))
        ] for j in range(len(matrix[0]))
    ]
    # print(new_matrix)
    return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    new_matrix = matrix_transpose(matrix)
    # 结果:
    # [
    #     [1, 4, 7, 10],
    #     [2, 5, 8, 11],
    #     [3, 6, 9, 12]
    # ]
