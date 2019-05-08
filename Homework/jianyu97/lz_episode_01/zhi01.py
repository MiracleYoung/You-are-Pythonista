# -*- coding:UTF-8 -*-
for i in range(2,1000000):
    fg = 0
    for j in range(2,i-1):
        if i%j == 0:
            fg = 1
            break
    if fg == 0:
        print(i)