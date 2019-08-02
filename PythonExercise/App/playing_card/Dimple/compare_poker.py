#  将每张J、Q、K、A、2,joker,JOKER都转换成具体的数字11-17
def replaceFlower(nums):
        nums = nums.replace('JOKER','17')
        nums = nums.replace('joker','16')
        nums = nums.replace('2','15')
        nums = nums.replace('A','14')
        nums = nums.replace('K','13')
        nums = nums.replace('Q','12')
        nums = nums.replace('J','11')
        return nums

# 计算传入的内容的和
def sum(nums):
        result = 0
       
        for i in range(len(nums)):
                result = nums[i] + result

        return result

# 判断是否是炸弹
def isBomb(nums):
        # 如果是4位数，并且是相同的值，那就是炸弹
        if len(nums) == 4 and min(nums) == max(nums):
                return True

        # 如果是2张牌，加起来是33，那就是王炸
        if len(nums) == 2 and sum(nums) == 33:
                return True
        return False

# 判断是否是顺子
def isContinuous(nums):
        # 对数字进行排序
        nums.sort()

        for i in range(len(nums) - 1):
                # 相邻两个数之间相同，肯定不是顺子
                if nums[i] == nums[i + 1]:
                        return False

                # 后一个比前一个多1，继续执行
                if nums[i+1] == nums[i] + 1:
                        continue
                else:
                        return False
                       
        return True


# 判断输入的值是否正确
def isValidNums(nums):
        # 5个数字以下的，只能出单个，对子，三个，四个即最大值和最小值必然相同才能算有效
        if len(nums) > 0 and len(nums) < 5 and (max(nums) == min(nums)):
                return True
        # 5个数字的，考虑是否是顺子
        elif len(nums) == 5:
                return isContinuous(nums)

        return False

# 比较两个数组的大小
def compareNums(firstChange,secondChange,first,second):
        if sum(firstChange) > sum(secondChange):
                print(first)
        else:
                print(second)

print("请输入你所要出的牌，用-隔开:")
nums = input();
nums = nums.split('-')
first = nums[0]
second = nums[1]

# 转换大小王和花牌
firstChange = replaceFlower(first)
secondChange = replaceFlower(second)

firstChange = firstChange.split(" ")
secondChange = secondChange.split(" ")

# 将一个字符串数组转换成整型数组，方便最大、最小值比较
firstChange =  list(map(int,firstChange))
secondChange = list(map(int,secondChange))

# 判断输入的两个数据是否相等，如果不等，需要判断是不是炸，否则直接输出错误
if len(firstChange) != len(secondChange):
        if isBomb(firstChange) or isBomb(secondChange):
                compareNums(firstChange,secondChange,first,second)
        else:
                print("You input is Error")

else:
        # 判断是否是合法数据
        if isValidNums(firstChange) == False:
                print("You first input is Error " + str(firstChange))
                
        elif isValidNums(secondChange) == False:
                print("You second input is Error " + str(secondChange))
        else:
                # 合法数据，则进行结果输出
                compareNums(firstChange,secondChange,first,second)


