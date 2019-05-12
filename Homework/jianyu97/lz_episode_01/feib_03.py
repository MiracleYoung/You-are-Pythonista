# -*- coding:UTF-8 -*-
def fun(n):
   a = 0
   b = 1
   i = 0
   l = []
   while i < n:
       l.append(a)
       a, b = a + b, a
       print(a,b)
       i += 1
   return l
print(fun(10))