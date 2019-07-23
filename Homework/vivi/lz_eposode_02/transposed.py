#!/usr/bin/env python
# encoding: utf-8


def matrix_transposed(matrix):
    new_matrix = [
        [
            matrix[i][j] for i in range(len(matrix))
        ] for j in range(len(matrix[0]))
    ]
    return new_matrix
