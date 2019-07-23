"""
100万以内的质数
"""


def prime_number(nums):
    ls = [True for i in range(nums + 1)]
    ls[0] = ls[1] = False
    for i in range(2, nums + 1):
        if ls[i]:
            j = 2
            while i * j <= nums:
                ls[i * j] = False
                j += 1
    prime = [i for i in range(len(ls)) if ls[i]]
    print(prime)
    return prime


if __name__ == "__main__":
    num = 100
    prime_number(num)
    # 结果: [
    #   2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
    #   37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
    #   79, 83, 89, 97, ......................
    #   .............., 999773, 999809, 999853,
    #   999863, 999883, 999907, 999917, 999931,
    #   999953, 999959, 999961, 999979, 999983
    # ]
       
