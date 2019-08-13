# -*- coding: utf-8 -*-
import string


def b64decode(data: str) -> bytes:
    map_table = string.ascii_letters + string.digits + '+/'
    start = 0
    decoded = bytearray()
    # 分组 每4个一组 字符串长度肯定为4的整数倍 并且 ‘=’ 只能出现在最后
    for group in range(4, len(data) + 1, 4):
        temp = 0  # 每组数据计算出来后临时存放在这里
        # 解密每一组的编码
        for index, value in enumerate(data[start:group]):
            if value != '=':
                temp += map_table.index(value) << 24 - (index + 1) * 6
            else:
                # ‘=’ 是编码时最末位补0产生的 解码时直接将其附加在数值最后就行 或者不加应该也可以
                temp += 0 << 24 - (index + 1) * 6
        # 排列顺序 big从前往后  little从后往前
        decoded.extend(temp.to_bytes(3, 'big'))
        start += 4

    return bytes(decoded)


def main():
    print(b64decode('QQ==').decode('utf-8'))
    print(b64decode('55m96YeR5LmL5pifwrfkuJbnlYw=').decode('utf-8'))


if __name__ == '__main__':
    main()
