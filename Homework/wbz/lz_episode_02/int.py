```
def Sint(s):
    '''
    字符串转整数，利用乘以10的幂，eg：10**1 = 10 10**2 = 100 ;小数部分利用除以10，eg:4/10 = 0.4  4/100 = 0.04
    :param s: s是一个传入的字符串
    :return: 把字符串的引号去掉，使其成为int或float
    '''
    d = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
    num = 0
    if '.' in s:
        inte,deci = s.split('.')  # 用.把整数小数分开，并分别赋值
        for id,v in enumerate(inte,start=1):
            lenth = len(inte)
            num += d[v] * (10 ** (lenth-id))

        for id,v in enumerate(deci,start=1):
            lenth = len(deci)
            num += d[v] /(10 ** id)

    else:
        for id,v in enumerate(s,start=1):
            lenth = len(s)
            num += d[v] * (10 ** (lenth-id))

    return num

s = '123.456'
print(Sint(s))
```
![image](https://github.com/wubaozhen/You-are-Pythonista/blob/master/Homework/wbz/lz_episode_02/02_03.PNG)


