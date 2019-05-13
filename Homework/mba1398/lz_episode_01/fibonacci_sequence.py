"""
斐波那契数列
20190510
"""


def fibonaccisequence(n):
    FSn = []
    for i in range(3, n+1):
        FSn.append(int(1/(5**0.5)*(((1+5**0.5)/2)**i - ((1-5**0.5)/2)**i)))
    print(FSn)


fibonaccisequence(20)
