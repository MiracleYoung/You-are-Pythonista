# -*- coding: utf-8 -*-


STRING_NUMBER_MAPPING = {
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0
}


def string_to_num(str_number):
    num = 0  # 最终返回数字
    key = 0  # 10的key次幂
    # 判断字符串将要转换的数类型
    if '.' in str_number:
        str_number_list = str_number.split('.')
        # 小数点只有一个
        if len(str_number_list) > 2:
            print('输入的数字格式有误，程序退出')
            exit()
        # 整数部分
        for char in str_number_list[0]:
            # 123 = 100 + 20 + 3
            num += STRING_NUMBER_MAPPING[char] * 10 ** (len(str_number_list[0]) - 1 - key)
            key += 1
        # 小数部分
        # 小数点后没有数字
        if str_number_list[1] == '':
            num += 0.0
            return num
        else:
            key = 0
            for char in str_number_list[1]:
                # 0.25 = 2/10 + 5/100
                num += STRING_NUMBER_MAPPING[char] * 10 ** (-1 - key)
                key += 1
        return num
    else:
        for char in str_number:
            # 123 = 100 + 20 + 3
            num += STRING_NUMBER_MAPPING[char] * 10 ** (len(str_number) - 1 - key)
            key += 1
        return num


def main():
    while 1:
        str_num = input('请输入数字：')
        num = string_to_num(str_num)
        print(type(str_num))
        print(num)
        print(type(num))


if __name__ == '__main__':
    main()
