class yanghui_tan(object):

    def __init__(self, num, row, col):
        self.A = [1]
        self.num = num
        self.row = row
        self.col = col
        if self.num < self.row or self.num < self.col:
            raise ValueError('num must lge row and col')

    def print_it(self):
        A = [1]
        A_list = [[1]]
        for i in range(self.num):
            L = A.copy()
            L = [str(L[j]) for j in range(len(L))]
            l = ' '.join(L).center(self.num * 3)
            print(l)
            A.append(0)
            A = [A[k] + A[k - 1] for k in range(i + 2)]
            A_list.append(A)
        print(f'第{self.row}行第{self.col}列的值为\
{A_list[self.row - 1][self.col - 1]}')


yanghui_tan(5, 4, 3).print_it()
