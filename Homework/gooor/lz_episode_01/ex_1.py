def is_prime_number(x):
    is_prime = True
    for i in range(2,x):
        if x % i == 0:
            is_prime = False

    return is_prime


if __name__ == "__main__":
    f = filter(is_prime_number,range(1,100))
    for i in f:
        print(i,end=' ')
