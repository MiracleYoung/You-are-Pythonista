import math
print(2,end=" ")
for i in range(3,1000000):
    k = int(math.sqrt(i))+1
    f = True
    for j in range(2,k):
        if (i%j == 0):
            f = False
            break
    if (f):
        print(i,end=" ")
