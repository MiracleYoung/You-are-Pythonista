import numpy as np

#这里用了纯Python写法，里面使用Numpy格式化了
#第二个方法是Numpy实现的，更简单

class juzhen_T(object):

    def normal_type(self, List):
        print('列表：')
        print(List)
        print('原矩阵：')
        print(np.matrix(List))
        print('转置后：')
        dic = dict(List)
        List_matrix = [list(dic.keys()), list(dic.values())]
        print(np.matrix(List_matrix))

    def numpy_type(self, matrix):
        print('列表：')
        print(matrix)
        matrix = np.matrix(matrix)
        print('原矩阵：')
        print(matrix)
        matrix_transpose = np.transpose(matrix)
        print('转置后：')
        print(matrix_transpose)


juzhen_T().normal_type(List=[[1, 2], [3, 4], [5, 6]])
juzhen_T().numpy_type(matrix=[[1, 2], [3, 4], [5, 6]])
