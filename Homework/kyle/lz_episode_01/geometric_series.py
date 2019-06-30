# 求任意整数的几何级数
a = int(input('please give me an int:'))
b = int(input('please give me another int:'))
c = int(input('the first number:'))
if c == 0:
    print("the initial number can't be zero")
else:
    try:
        s = c * ((b ** a) - 1) / (b - 1)
        print(s)
    except ZeroDivisionError:
        print("b can't be 1,please give another number")
