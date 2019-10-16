from math import sqrt


def get_prime(n):
    return filter(lambda x: not [x%i for i in range(2, int(sqrt(x)+1)) if x%i == 0], range(2, n+1))


def main():
    for each in get_prime(20):
        print(each)

if __name__ == "__main__":
    main()