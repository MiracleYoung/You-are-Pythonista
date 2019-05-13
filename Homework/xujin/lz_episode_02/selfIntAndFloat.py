
NUMBER_DICT = {str(key):value for key,value in enumerate(range(0,10))}

def selfInt(str1):
    number_list = str1.split('.')
    if len(number_list) > 2: # 4.3.2
        raise ValueError(f'{str1}不能转化为整数！！！')
    number_str = number_list[0]
    length = len(number_str)
    number = 0
    for key,value in enumerate(number_str):
        dict_value = NUMBER_DICT.get(value)
        if dict_value is None:
            raise ValueError(f'不能将{value}转化为整数！！！')
        else:
            number = number + dict_value * 10 ** (length - key - 1)
    return number

def selfFloat(str1):
    number_list = str1.split('.')
    if len(number_list) > 2:
        raise ValueError(f'{str1}z不能转化为整数！！！')

    int_number_str = number_list[0]
    if len(number_list) == 1:
        decimals_number_str = '0'
    else:
        decimals_number_str = number_list[1]
    int_length = len(int_number_str)
    number = 0
    for key,value in enumerate(int_number_str):
        dict_value = NUMBER_DICT.get(value)
        if dict_value is None:
            raise ValueError(f'不能将{value}转化为整数！！！')
        else:
            number = number + dict_value * 10 ** (int_length - key - 1)

    for key,value in enumerate(decimals_number_str):
        dict_value = NUMBER_DICT.get(value)
        if dict_value is None:
            raise ValueError(f'不能将{value}转化为小数！！！')
        else:
            number = number + dict_value * 10 ** (-1 - key)

    return number



if __name__ == '__main__':
    print(selfInt('101'))
    print(selfInt('11.2'))
    print(selfInt('101.2'))
    print(selfFloat('101.2'))
    print(selfFloat('10.2'))
    print(selfFloat('10'))
