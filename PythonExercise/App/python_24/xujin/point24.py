from collections.abc import Iterable
from itertools import product,permutations,zip_longest,chain
import math

class Point24():
    # 定义操作符元祖
    OPERATIONS = ('+','-','*','/')

    # 定义格式化字符窜的格式
    FORM_STRS = [
        # 一个括号 的情况
        '(%s %s %s) %s %s %s %s',
        '(%s %s %s %s %s) %s %s',
        '(%s %s %s %s %s %s %s)',
        '%s %s (%s %s %s) %s %s',
        '%s %s (%s %s %s %s %s)',
        '%s %s %s %s (%s %s %s)',

        # 两个括号 的情况
        '(%s %s %s) %s (%s %s %s)',

        '( (%s %s %s) %s %s) %s %s',
        '( %s %s (%s %s %s)) %s %s',

        '%s %s ((%s %s %s) %s %s)',
        '%s %s (%s %s (%s %s %s))',

        # 三个括号是重复的
    ]

    def __init__(self,data_iter):
        # 判断传入的的对象是否可遍历
        if not isinstance(data_iter, Iterable):
            raise TypeError(f'{data_iter} cat`t iter')

        self.data_iter = data_iter

    def _get_all_operation_sequence(self):
        '''
        从self.OPERATIONS选取任意个数的字符，组成一个元祖，
        返回一个生成器
        :return:
        '''
        return product(self.OPERATIONS,repeat=3)

    def _get_all_data_sequence(self):
        '''
        对传入的数字进行全排列，返回一个生成器
        :return:
        '''
        return permutations(self.data_iter)

    def _format_str(self,calculate_str):
        # 对传入的没有括号的表达式，进行格式化为有括号的表达式,每次返回一个格式化好的表达式。
        for format_str in self.FORM_STRS:
            yield format_str % (
                calculate_str[0],
                calculate_str[1],
                calculate_str[2],
                calculate_str[3],
                calculate_str[4],
                calculate_str[5],
                calculate_str[6]
            )

    def calculate(self):
        '''
        计算值，返回对应的表达式和值
        :return:
        '''

        # 遍历所有可能的数字
        for data_sequence in self._get_all_data_sequence():
            # 得到所有的操作符。
            # QUESTION： 为什么每次遍历都需要重新去执行这个方法呢？而不是用一个变量保存这个方法的结果
            # ANSWER: 因为这个方法返回的是一个生成器，而生成器是不可能逆的，所以需要每次执行到这里都需要重新去生成这个生成器，在进行遍历
            operation_sequences = self._get_all_operation_sequence()
            # 对所有的操作符进行遍历
            for operation_sequence in operation_sequences:
                # 使用zip_longest对数字和操作符进行组合，
                value = zip_longest(data_sequence, operation_sequence, fillvalue='')
                value_chain = chain.from_iterable(value)
                calculate_str = ''
                # 遍历每个字符，然后得到没有括号的表达式
                for _ in value_chain:
                    calculate_str += _

                # 遍历self._format_str方法，传入没有括号的表达式，得到有括号的表达式
                for finally_calculate_str in self._format_str(calculate_str):
                    try:
                        # 使用eval函数执行表达式
                        result = eval(finally_calculate_str)
                    # 补货被除数为0的异常，然后就跳过此次循环
                    except ZeroDivisionError:
                        continue

                    # 使用math.close()判断表达式的运行结果和24是否相等,返回表达式和运算结果
                    if math.isclose(result, 24):
                        return finally_calculate_str, result
        # 运行到这葛位置，说明没有找到可以运算出24的表达式，返回None
        return None,None

if __name__ == '__main__':

    input_str = input('请输入数字（0-9），每个数字之间使用`,`隔开:')

    data_list = input_str.split(',')

    for data in data_list:
        try:
            if int(data) < 0 or int(data) > 9:
                raise ValueError('请输入0-9之间的数字')
        except TypeError:
            raise TypeError('请输入格式正确的数')

    print(Point24(data_list).calculate())
