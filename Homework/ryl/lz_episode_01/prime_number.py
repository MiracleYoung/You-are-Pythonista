# 暴力求解：质数只有1和本身是自己的因数，所以从2到本身减一去全部试探一遍
# 搜索到i**0.5就可以了

import time
import math
print('100万以内的质数')
start = time.time()
num = int(input('number:'))
ret = []
l = [2, 3, 5, 7, 9]
for i in range(2, num+1):
    for a in l:
        if i%a == 0:
            continue
            
    for j in range(2, int(i**0.5)):
        if i%j == 0:
            break
    else:
        ret.append(i)

print('Counts：', len(ret))
print('Time:', time.time()-start)
