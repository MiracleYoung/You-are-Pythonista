

def get_geometrical_progression(number,common_ratio,count):
    answer = number
    if count > 1:
        for i in range(count-1):
            number = number*common_ratio
            print(number)
            answer += number
    return answer

if __name__ == '__main__':
    while 1:
        try:
            number = int(input("请输入底数："))
            common_ratio = int(input("请输入公比："))
            count = int(input("请输入求和的个数："))
            break
        except:
            print("error:请输入一个整数！")

    answer = get_geometrical_progression(number,common_ratio,count)
    print(answer)