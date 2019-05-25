a = int(input('输入首项: '))
q = int(input('输入公比: '))
n = int(input('输入项数: '))
if q == 1:
    s = a * n
else:
    s = int(a*(q**n-1)/(q-1))
print (s)
