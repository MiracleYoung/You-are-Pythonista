""" 把字符串形式的整数或浮点数转化为int或float """

str_dic = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
}


def str_to_int(strs):
    # 位
    bit = 1
    lens = len(strs)
    new_strs = strs[::-1]
    number = 0
    for i in new_strs:
        number += str_dic[i] * bit
        bit *= 10
    return number


def str_to_float(strs):
    left_no, right_no = strs.split(".")
    left_num = str_to_int(left_no)
    # 位
    bit = 0.1
    right_num = 0
    for i in right_no:
        right_num += str_dic[i] * bit
        bit /= 10
    number = left_num + right_num
    return number


def main(strs):
    if strs.isalnum():
        return str_to_int(strs)
    if len(strs.split('.')) == 2:
        if strs.split('.')[0].isalnum() and strs.split('.')[1].isalnum():
            return str_to_float(strs)
    print("输入的字符有误!")


if __name__ == "__main__":
    strs = "1523.1243"
    number = main(strs)
    print(number)
    # 结果: 1523.1243
