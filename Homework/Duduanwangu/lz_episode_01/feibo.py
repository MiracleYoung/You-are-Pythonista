# ì³²¨ÄÇÆõÊıÁĞ
def feibo(n):
    a = 1
    b = 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b

feibo(100)