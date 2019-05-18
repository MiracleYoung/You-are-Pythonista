n = 5
k = 2
lst = [[1]]
print([1])
for i in range(1,n):
    t = []
    t.append(lst[i-1][0])
    
    for j in range(1,i):
        t.append(lst[i-1][j-1]+lst[i-1][j])
    
    t.append(lst[i-1][i-1])
    
    lst.append(t)
    print(t)
    
print(lst[n-1][k-1])
