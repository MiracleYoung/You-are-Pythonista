# 1、求100w内的质数
# 判断依据：对正整数n，如果用2到根号n之间的所有整数去除，
# 均无法整除，则n为质数

from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for n in range(1, 1000001):
    is_prime(n)
    if is_prime(n) == True:
        print(n, end=" ")
