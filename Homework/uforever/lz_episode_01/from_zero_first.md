## 【从零单排】第一章作业中的主要代码

> 1.求100w内的质数。
>
> 2.求任意整数的几何级数。
>
> 3.斐波那契数列。

#### 1.求任意整数区间里的质数

```python
#判断一个num是否质数
def is_prime_num(num):
    new_num = int(num ** 0.5) + 1
    for i in range(2, new_num):
        if num % i == 0:
            return False
    else:
        return True

#获取任意一个左闭右开的整数区间内所有的质数列表
def prime_num_list(start_num,end_num):
    return list(filter(is_prime_num, range(start_num,end_num)))
```

思考：1.range()的取值范围。2.如果start_num大于或等于end_num，应该如何处理？

#### 2.求任意整数的几何级数

```python
#获取任意整数的几何级数
def get_geos_sum(a,q,n):   #参数n是指最高级数，即最后一项的幂指数。
    if n == 0:             #当n取1时，只有常数项a。
        return a
    return a*q**n + get_geos_sum(a,q,n-1)
```

思考：当参数n表示全部项数时需要修改哪里？

#### 3.斐波那契数列

```python
#获取第n项斐波那契数
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

#获取n项斐波那契数列
def get_fib_list(n):
    return [fib(i) for i in range(1, n + 1)]
```

思考：会不会出现这样的情况，在run后没有错误提示，但得到的数列并不是斐波那契数列？