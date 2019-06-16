class Fibo(object):
    def get_ret(self, num):
        L = list(range(0, num))
        F = L
        for i in L:
            if i <= 1:
                F[i] = L[i]
            else:
                F[i] = L[i - 1] + L[i - 2]
        print(f"拥有{num}个数的斐波那契数列是{F}")
Fibo().get_ret(10)
