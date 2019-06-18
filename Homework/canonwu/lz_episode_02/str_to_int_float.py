def s_to_i_f(num_str):
    d = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,\
         '7': 7, '8': 8, '9': 9, '0': 0}
    num = 0

    if '.' in num_str:
        num_left, num_right = num_str.split('.')
        for i, n in enumerate(num_left, start=1):
            lenth = len(num_left)
            num += d[n] * pow(10, (lenth - i))

        for i, n in enumerate(num_right, start=1):
            num += d[n] / pow(10, i)

    else:
        for i, n in enumerate(num_str, start=1):
            lenth = len(num_str)
            num += d[n] * (10 ** (lenth - i))

    return num


s = '520.1314'
print(s_to_i_f(s))
print(type(s_to_i_f(s)))
