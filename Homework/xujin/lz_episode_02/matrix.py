import random
import time

def transPoseMatrix(matrix):
    temp = []

    # 有几列创建几个列表 一个列表存放一行的数据
    for _ in range(len(matrix[0])):
        temp.append([])

    for row in matrix:
        index = 0
        for value in row:
            temp[index].append(value)
            index += 1

    return temp

def showMatrix(matrix):
    for row in matrix:
        for value in row:
            print(value,end="\t")
        print() # 换行

def createMatrix(row,col):
    matrix = []
    for i in range(row):
        matrix.append([])
        for j in range(col):
            matrix[i].append(random.randint(1,100))

    return matrix

if __name__ == '__main__':
    while True:
        try:
            row = int(input("请输入矩阵的行数:"))
            break
        except ValueError:
            print("请输入一个格式正确的行数!")
            time.sleep(1)
    while True:
        try:
            col = int(input("请输入矩阵的列数:"))
            break
        except ValueError:
            print("请输入一个格式正确的列数")
            time.sleep(1)

    matrix = createMatrix(row,col)
    print("原始矩阵为:")
    showMatrix(matrix)
    matrix = transPoseMatrix(matrix)
    print("转置后的矩阵为:")
    showMatrix(matrix)