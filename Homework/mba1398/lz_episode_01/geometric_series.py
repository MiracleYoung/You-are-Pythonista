"""
GeometricSeries
"""


def geometricseries(a, q, n):

    if q == 1:
        ss = a * n
    else:
        ss = int(a*(q**n-1)/(q-1))
    print("{}, {}, {}的几何级数是: {}".format(a, q, n, ss))


geometricseries(2, 2, 3)
