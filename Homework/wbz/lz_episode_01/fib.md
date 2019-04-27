# 斐波那契数列
```
def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return F(n-1) + F(n-2)

for i in range(1,20):
    print(F(i),end=' ')
```
![image](https://github.com/wubaozhen/You-are-Pythonista/blob/master/Homework/wbz/lz_episode_01/01_03.PNG)
