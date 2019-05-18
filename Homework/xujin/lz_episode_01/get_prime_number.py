
def get_prime_number(number):
    prime_numbers = [1]
    if number > 1:
        for i in range(2,number+1):
            is_prime = True
            for j in range(2,int(i**0.5)+1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(i)
                print(i)
    return prime_numbers

if __name__ == '__main__':

    while 1:
        try:
            number = int(input("请输入求质数的范围:"))
            break
        except:
            print("error:请输入一个整数！")

    prime_numbers = get_prime_number(number)
    print(prime_numbers)