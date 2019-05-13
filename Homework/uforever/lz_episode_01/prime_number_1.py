#!/usr/bin/env python
# encoding:utf-8
# @Time    : 2019/5/3 上午8:46

__author__ = 'Uforever I'


def is_prime_num(num):
    new_num = int(num ** 0.5) + 1
    for i in range(2, new_num):
        if num % i == 0:
            return False
    else:
        return True

def prime_num_list(start_num,end_num):
    return list(filter(is_prime_num, range(start_num,end_num)))

min = int(input("Please input start num:"))
max = int(input("Please input end num:"))

if min>max:
    min,max=max,min
    print(prime_num_list(min,max))
elif min==max:
    print("The start num should be less than the end num!")
    print(min,is_prime_num(min))
else:
    print(prime_num_list(min, max))


if __name__ == "__main__":
    print("For example in '1~100':")
    print("[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]")