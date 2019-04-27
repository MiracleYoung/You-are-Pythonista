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
![image]()
