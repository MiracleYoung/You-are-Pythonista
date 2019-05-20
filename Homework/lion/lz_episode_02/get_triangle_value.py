# -*- coding: utf-8 -*-


def get_value(row, colnum):
    # 行数小于2 第一列 最后一列的值都为 1
    if row <= 2:
        return 1
    elif row == colnum:
        return 1
    elif colnum == 1:
        return 1
    else:
        return get_value(row - 1, colnum - 1) + get_value(row - 1, colnum)


def print_current_row(row):
    # 每行的数值的个数是当前的行数
    current_cow = list()
    for i in range(row):
        current_cow.append(get_value(row, i + 1))
    return current_cow


def main():
    try:
        row = int(input('请输入你想知道的杨辉三角第几行：'))
        print(print_current_row(row))
    except Exception as err:
        print(f'数字格式输入有误,详细信息:{err}')


if __name__ == '__main__':
    main()
