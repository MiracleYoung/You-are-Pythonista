class Cal_prime_num(object):
    def primes(self, n):
        s = 0
        for i in range(2, n):
            for j in range(2, i-1):
                if i % j == 0:
                    break
            else:
                print(i)
                s += 1
        print(f'总共有{s}个')

Cal_prime_num().primes(1000000)
