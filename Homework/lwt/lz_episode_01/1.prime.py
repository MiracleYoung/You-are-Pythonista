#求100w以内的质数
for i in range(2,1000000):#范围为2到100w
    j=2                 #从2开始
    mark=0              #mark为质数标记，是质数则为0，不是为1
    while(j*j<=i):      #结束条件为 i 的开方
        if i%j==0:      #若j被i整除，则i不是质数
            mark=1      #标记改为1
            break       #跳出循环
        j += 1          #j 自增一
    if mark==0:         #标记为0，则为质数
        print(i,end=' ')#输出质数，结尾为一个空格
