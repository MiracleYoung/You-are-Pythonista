a = input("请输入第一项a：")
q = input("请输入要乘的固定比q：")
n = input("请输入需要要求和的n：")

s = 0
for i in range(int(n)):
    s = s + int(a) * pow(int(q),i)
print(s)