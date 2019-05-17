# -*- coding: utf-8 -*-
import math
import time


def main():
    start = time.time()
    prime_nums = list()
    for i in range(2, 101):
        flag = True

        # 除2以外所有的质数都是奇数
        if i == 2:
            flag = True
        elif i % 2 == 0:
            flag = False
        else:
            # 如果i包含除自身以外的质因数 那肯定小于等于 i/2 直接尝试 i/2 以内的奇数
            # for k in range(3, int(i / 2) + 1):
            # 所有的因数都是成对出现 其中一个必然小于 sqrt(i)
            # sqrt(101) 需要尝试的奇数 3 5 7 9 被9整除肯定能被3整除
            # 直接尝试所有质因数
            for k in range(3, int(math.sqrt(i)) + 1):
                if k % 2 != 0:
                    # if k in prime_nums:
                    if (i % k) == 0:
                        flag = False
                        break
        if flag:
            prime_nums.append(i)
            print(i, end=' ')

    end = time.time()
    print(f"程序用时{end - start}")


if __name__ == '__main__':
    main()
