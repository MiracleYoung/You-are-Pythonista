matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrixTranspose = []

for _ in range(len(matrix)):
    matrixTranspose.append([])

for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrixTranspose[j].append(matrix[i][j])

matrixTranspose