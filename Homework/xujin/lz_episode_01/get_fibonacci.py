
def get_fibonacci(start_number,count):
    fibonacci = [start_number]
    current_position = 0
    if count == 1:
        pass
    elif count == 2:
        fibonacci.append(start_number)
    else:
        fibonacci.append(start_number)
        for i in range(count-2):
            temp = fibonacci[current_position] + fibonacci[current_position+1]
            fibonacci.append(temp)
            current_position += 1

    return fibonacci

if __name__ == '__main__':
    while 1:
        try:
            start_number = int(input("请输入起始值（第一个值）:"))
            count = int(input("请输入获取斐波那列的个数:"))
            break
        except:
            print("error:请输入一个整数")

    fibonacci = get_fibonacci(start_number,count)
    print(fibonacci)