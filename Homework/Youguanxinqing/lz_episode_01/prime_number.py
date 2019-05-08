#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Guan
@Github: https://github.com/youguanxinqing
@Date: 2019-04-26 17:21:58
@LastEditTime: 2019-04-27 21:36:16
'''

def get_prime_number(num):
    new_num = int(num ** 0.5) + 1
    for i in range(2, new_num):
        if num % i == 0:
            return False
    else:
        return True


def get_prime_number_sequence():
    return list(filter(get_prime_number, range(2, 1000000)))

if __name__ == "__main__":
    rlt = get_prime_number_sequence()
    print(rlt)