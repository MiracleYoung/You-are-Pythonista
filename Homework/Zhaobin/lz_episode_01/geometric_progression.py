"""
几何级数分析
    s = a             + a * q         + a * pow(q, 2) + ... + a * pow(q, n)
      = a * pow(q, 0) + a * pow(q, 1) + a * pow(q, 2) + ... + a * pow(q, n)
      = a * (pow(q, 0) + pow(q, 1) + pow(q, 2) + ... pow(q, n))
      = a * sum([pow(q, i) for i in range(n + 1)])
"""


def genometric(a, q, n):
    s = a * sum([pow(q, i) for i in range(n + 1)])
    print(s)
    return s


if __name__ == "__main__":
    a, q, n = 10, 20, 30
    genometric(a, q, n)
    # 结果: 11302545515789473684210526315789473684210

    # 简化版本 labmda
    # s = lambda a, q, n: a * sum([pow(q, i) for i in range(n + 1)])
