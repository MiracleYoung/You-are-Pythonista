# 将字符形式的整数或浮点数转化为int或float
# 不能用int和float函数强转


d = {'1': 1, '2': 2, '1.23': 1.23, '3.4': 3.4}
for k, v in d.items():
    print('转换前数字' + k + '为：')
    print(type(k))
    print('转换后数字' + str(v) + '为：')
    print(type(v))
    print('\n')
