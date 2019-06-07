def matrix(L):
    '''
    利用索引值相同取每个子列表上的元素，组合成一个新的子列表
    :param L: 传入一个矩阵
    :return: 返回倒置的矩阵
    '''
    L_trans = []
    lenth = len(L[0])  # 得到循环次数
    for i in range(lenth):
        temp = []  # 存二级列表
        for l in L:
            temp.append(l[i])
        L_trans.append(temp)
    return L_trans
L = [[1,2],[3,4],[5,6]]
print(matrix(L))

![image](https://github.com/wubaozhen/You-are-Pythonista/blob/master/Homework/wbz/lz_episode_02/02_02.PNG)
