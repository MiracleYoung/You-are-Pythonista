# -*- coding: utf-8 -*-
"""
author: mba1398
date: 20190518
task: 字符串形式的证书或者浮点数转化为int/float
"""

# str2int
dict_s2n = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
str_int = '20190518'
sn = len(str_int)
int_num = 0
for i in range(sn):
    int_num += dict_s2n[str_int[sn-i-1]]*(10**i)
print(int_num)


# str2float
str_float = '520.1314'
float_num = 0.0
s1, s2 = str_float.split('.')
sn1 = len(s1)
sn2 = len(s2)
for i in range(sn1):
    float_num += dict_s2n[s1[sn1-i-1]]*(10**i)

for j in range(sn2):
    float_num += dict_s2n[s2[sn2-j-1]]*(10**(-sn2+j))
print(float_num)
