# 求100w内的质数
# 质数的定义：只能被1和本身整除

primarylist = []

def isprimarynumber(inputNumber):
    if inputNumber == 1:
        return False
    if inputNumber == 2:
        return True
    for i in primarylist:
        if i != 1 and inputNumber % i == 0:
            return False
    print(inputNumber)
    return True

number = 1
while number < 1000000:
    if isprimarynumber(number):
        primarylist.append(number)
    number = number + 1

print(primarylist)
