def Fibonacci_item(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_item(n - 1) + Fibonacci_item(n - 2)

def Fibonacci_list(n):
    lst = []
    for i in range(1, n+1):
        lst.append(Fibonacci_item(i))
    return lst

def main():
    print(Fibonacci_list(20))

if __name__ == "__main__":
    main()