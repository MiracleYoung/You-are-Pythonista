def yanghui(n):
    '''
    :param n: 输入杨辉三角的第n行
    :return: 返回第n行的每个值
    '''
    #思路：列表首设为1，第k个的值为上一行的k列和k-1列的和
    pre_list = [1]  # 初始化第一行的数据
    current_list = [1]   # 初始化第二行的数据
    for i in range(n):
        for j in range(i):
            if j != 0 :
                current_list[j] = pre_list[j] + pre_list[j - 1]

        pre_list = current_list
        current_list = current_list +[1]
    current_list.pop() # 删除最后一个元素
    return current_list

print(yanghui(10))

![image]()
