n = 10
a0 = 1
a1 = 1
a2 = 0
print(str(a0)+' '+str(a1),end = " ")
for i in range(3,n+1):
    a2 = a0+a1
    a0 = a1
    a1 = a2
    print(a2,end = " ")
