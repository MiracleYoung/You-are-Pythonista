def prime_num(num):
    prime_list = [2,3,5]
    if num <=5:
        return prime_list

    for i in range(5,num):
        for prime in prime_list:
            if i % prime == 0:
                break
        else:
            prime_list.append(i)

    prime_list.insert(0,1)
    return prime_list

if __name__ == "__main__":
    print(prime_num(100))