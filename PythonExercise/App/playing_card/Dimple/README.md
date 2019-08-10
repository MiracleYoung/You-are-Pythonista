周末又空闲下来了，手痒痒，想玩一玩斗地主，来消遣下无聊的时光。

但是每次在玩的时候，中了程序员毒的我又犯病了，这个斗地主，貌似也不是那么难吧。我何不用Python来实践下，看看这个斗地主，去一探究竟。

#### 基本规则

扑克牌一副牌由54张组成，含3~A，2各4张，小王1张，大王1张。牌面从小到大用如下字符和字符串表示（其中，小写joker表示小王，大写JOKER表示大王）。

1. 输入每手牌可能是个子，对子，顺子（连续5张），三个，炸弹（四个）和对王中的一种，不存在其他情况。

2. 除了炸弹和对王可以和所有牌比较之外，其他类型的牌只能跟相同类型的存在比较关系（如，对子跟对子比较，三个跟三个比较），不考虑拆牌情况（如：将对子拆分成个子）

3.  大小规则跟大家平时了解的常见规则相同，个子，对子，三个比较牌面大小；顺子比较最小牌大小；炸弹大于前面所有的牌，炸弹之间比较牌面大小；对王是最大的牌；

4. 输入的两手牌不会出现相等的情况

#### 输入描述

输入两手牌，两手牌之间用“-”连接，每手牌的每张牌以空格分隔，“-”两边没有空格

#### 大致思路

1. 首先因为花牌需要和大小王是没有一个数字的，所以要把花牌和大小王转换成数字。这里J、Q、K、A、2、joker、JOKER分别是11-17。

```Python
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
```

2. 为了方便计算数值，把转换过后的数字变成int数组

```Python
# 如何将一个字符串数组转换成整型数组，方便最大、最小值比较
firstChange =  list(map(int,firstChange))
secondChange = list(map(int,secondChange))
```

3. 判断是否是炸弹

```Python
# 判断是否是炸弹
def isBomb(nums):
        # 如果是4位数，并且是相同的值，那就是炸弹
        if len(nums) == 4 and min(nums) == max(nums):
                return True

        # 如果是2张牌，加起来是33，那就是王炸
        if len(nums) == 2 and sum(nums) == 33:
                return True
        return False
```

4. 5个数字以下的，只能出单个，对子，三个，四个即最大值和最小值必然相同才能算有效;5个数字的，考虑是否是顺子

```Python
# 判断输入的值是否正确
def isValidNums(nums):
        # 5个数字以下的，只能出单个，对子，三个，四个即最大值和最小值必然相同才能算有效
        if len(nums) > 0 and len(nums) < 5 and (max(nums) == min(nums)):
                return True
        # 5个数字的，考虑是否是顺子
        elif len(nums) == 5:
                return isContinuous(nums)

        return False
```

```Python
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
```

5. 把每个数组的值进行相应的求和，得到这个数组的结果，才能进行两个数组的大小比较

```Python
# 计算传入的内容的和
def sum(nums):
        result = 0
       
        for i in range(len(nums)):
                result = nums[i] + result

        return result
```

6. 来到最后一步，就是比较大小的逻辑了

```Python
# 比较两个数组的大小
def compareNums(firstChange,secondChange,first,second):
        if sum(firstChange) > sum(secondChange):
                print(first)
        else:
                print(second)
```

好吧，看上去还是有点复杂的，来来回回需要经过6个步骤才能走完一个流程。看来，斗地主这个游戏，看上去简单，但是在实际的编码过程中，还是需要一点思考的。毕竟，咱们的积分，金豆都需要辛苦赚来的嘛。

#### 执行大小比较

当上面所有的步骤都分拆好了，现在要做的自然就是把分拆的代码应用起来。是否是合法输入，是否走炸弹流程，是否走比较流程等等。

```Python
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
```

现在，就请你输入几组数据，看看吧。比如对A VS 对2,顺子3 4 5 6 7 VS 6 7 8 9 10

```Python
请输入你所要出的牌，用-隔开:
A A-2 2
2 2

请输入你所要出的牌，用-隔开:
3 4 5 6 7-6 7 8 9 10
6 7 8 9 10
```

代码安排完了，结果也执行完了，我一颗探索的心又恢复了平静。程序员的毒就是这样，日常生活中很多好玩的，都想通过程序来执行，来实现，这样才感觉到自己存在的价值，才感觉过的很有趣。