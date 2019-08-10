# 杨辉三角
# 求第n行第k列的值


# 定义一个空字典
d = {}

def yanghui(n, k=1):
    for x in range(n):
        x += 1
        # 更新字典
        d.update([(x, [])])
        if x <= 2:
            for _ in range(x):
                # 循环写入每行的值
                d[x].append(1)
        else:
            # 定义列表索引
            m = 0
            # 获取上次更新的字典的值，获取的值为一个列表
            lst = d[x-1]
            # 因为每行的开头都是1，所以直接写入
            d[x].append(1)
            for _ in range(x-2):
                # 每个数等于它上方两数之和
                v = lst[m] + lst[m + 1]
                d[x].append(v)
                m += 1
            # 因为每行末尾都是1，所以也直接写入
            d[x].append(1)
    return d


# 打印杨辉三角第n行第k列的值
def dayin(n, k):
    D = yanghui(n, k)
    key = D[n]
    value = key[k-1]
    print('第' + str(n) + '行第' + str(k) + '列的值为：' + str(value) + '\n')


# 打印n行的杨辉三角
def dayin_1(n):
    print(str(n) + '行的杨辉三角为：')
    # 因为函数yanghui()有两个参数，但函数dayin_1()只有一个，
    # 为了避免报错，可以为函数yanghui()的k参数指定一个默认值1
    D = yanghui(n)
    for x in range(n):
        # 因为x是从0开始，所以要加1
        x += 1
        # 打印空格
        for _ in range(n-x):
            print(' ', end='')
        # 获取字典的键对应的值列表，x为key
        lst = D[x]
        # 遍历列表lst
        for i in lst:
            print(i, end=' ')
        print('\n')


# 打印杨辉三角第n行第k列的值
dayin(4, 3)
# 打印n行的杨辉三角
dayin_1(4)

    
     
