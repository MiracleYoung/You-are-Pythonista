from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def main():
    i = 1
    while i <1000000:
        if is_prime(i):
            print(i)
        i += 1

if __name__ == '__main__':
    main()

