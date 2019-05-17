d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
'''实现字符串型的int转换'''
s = '2019516'
I = 0
l = len(s)
for x in range(l):
    I += d[s[l-x-1]]*(10 ** x)
print(I)


'''实现字符串型的float转换'''
s = '2019.516'
F = 0.0
f1,f2 = s.split('.')
l = len(f1)
for x in range(l):
    F += d[f1[l-x-1]]*(10 ** x)
    
l = len(f2)
for x in range(l):
    F += d[f2[x]]*(10 ** (-x-1))

print(F)