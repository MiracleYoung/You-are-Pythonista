# 【从零单排】第二章作业
# 本次作业的关键字是：lz_episode_02



def triangle(n):
    n = int(n)

    LL = [[1]]
    for i in range(1,n):

        LL.append([(0 if j== 0 else LL[i-1][j-1])+
                   (0 if j ==len(LL[i-1]) else LL[i-1][j])
                   for j in range(i+1)])
    return LL

def transpose(a):
    ret = []
    for i, row in enumerate(a):#a的每一行以及下标
        for j, col in enumerate(row):#每一行里面的值以及下标
            #ret[j][i] = a[i][j]
            if len(ret) - 1 > j:
                ret[j].append(col)
            else:
                ret.append([col])
    print(ret)

if __name__ == '__main__':
    # 1. 求杨辉三角第n行第k列的值
    # 提示：直接打印有n行的杨辉三角
    # n = input("请输入第几行：")
    # print(triangle(n))

    # 2. 矩阵转置
    # 提示：了解下什么是矩阵，然后想一下在python里矩阵可以用什么来表示
    # a = [[1, 2, 0],[3, -1, 4]]
    # transpose(a)

    # 3. 把字符串形式的整数或浮点数转化为int或float，不能用int和float函数强转。
    # 提示：可以通过字典，实现对应关系。
    mapping = {str(x):x for x in range(10)}
    s = 231.548
    s = str(s)
    i, _, f = s.partition('.')

    ret = 0
    for id, x in enumerate(i[::-1]):#-1让其从个位开始
        ret += mapping[x] * 10 ** id
    print(ret,type(ret))

    for id, x in enumerate(f):
        ret += mapping[x] / 10 ** (id + 1)
    print(ret)
