# encoding: utf-8
number_range = 1000000
for prime_number in range(2,number_range):
    # 获取一个数字
    is_prime = True
    for divisior in range(2,prime_number):
    # 设置被除数，判断是否能够被整除
        if prime_number%divisior == 0:
            is_prime = False
            break
        else:
            continue
    if is_prime :
        print(prime_number)
