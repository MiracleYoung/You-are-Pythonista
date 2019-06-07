# -*- coding: utf-8 -*-


def get_geometric_progression(first_item, common_ratio, items):
    sum = 0
    for i in range(items):
        sum += first_item * (common_ratio ** i)
    return sum


def main():
    try:
        first_item = int(input('请输入首项'))
    except Exception as err:
        print("请输入正确的数字")
        exit()
    try:
        common_ratio = int(input('请输入公比'))
    except Exception as err:
        print("请输入正确的数字")
        exit()
    try:
        items = int(input('请输入求解个数'))
    except Exception as err:
        print("请输入正确的数字")
        exit()

    sum = get_geometric_progression(first_item, common_ratio, items)
    print(sum)


if __name__ == '__main__':
    main()
