def fib(n):
    a, b = 1, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b

fib(100)  # 输出的是100以内的斐波那契数列


#result
1 1 2 3 5 8 13 21 34 55 89 
