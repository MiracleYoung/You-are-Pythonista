def cal_geo_series(a,q,n):
    qn = 1
    for i in range(n):
        qn *= q

    s = a * (qn -1) / (q -1)

    return s

if __name__ == '__main__':
    print(cal_geo_series(1,2,3))