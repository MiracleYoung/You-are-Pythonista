# 求100以内的质数
```
import math
for i in range(2,100):
    for j in range(2,int(math.sqrt(i)+1)):
        if not i % j:
            break
    else:
        print(i,end=' ')
   ```     
        
  ![image](https://github.com/wubaozhen/You-are-Pythonista/blob/master/Homework/wbz/lz_episode_01/01_01.PNG)
        
        
