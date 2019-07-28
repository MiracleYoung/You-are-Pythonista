#> python实现24点算法

还记得学生时代，我妈妈一直说我数学很差，每周上学都要提醒我数学课认真认真再认真；但是呢，我却不以为意，明明我考试考的挺好的呀，何况很多东西不可能算错，因为我有计算器。

但是，后来一个游戏改变了我对自己的看法。计算器并不是万能的，也不是最快的；而我，数学也不是挺好的。这就是我们今天要说的24点游戏。

那是一个炎热的夏天，我在表姐家过暑假，大家提议玩24点游戏。规则大致如下：**拿出一副扑克牌去掉大小怪，其中，J代表11，Q代表12，K代表13，A代表1（也可以去掉这些花牌），从剩下的牌里随便找出四张，谁能先用加减乘除算出24就算赢。结果我那表姐胜多负少。**

当时就想，心算确实好像挺难的，加上自己数学的感觉很差，失败就在所难免。回家路上，还一直幻想着，什么时候电脑能做这个就好了。没想到，长大以后，接触了Python，帮我解决了这个大难题。小时候的梦想，今天终于实现了。

#### 思路和算法

因为这4个数字顺序是不定的，所以我们需要实现输入4个数字，然后进行排列组合，期间再通过加、减、乘、除的运算符来进行组合计算。

在这里，无论是数字，还是运算符号，都要做相应的顺序重排。当然，这在我们的Python面前还是没有一点点难度，通过permutations即可完成。详细如下：

重排输入的数字:

```Python
def getNumberList(numbers):
    result = []
    
    for number in set(itertools.permutations(numbers)):
        result.append(list(number))

    return result

```

重排输入的运算符。因为我们是四个数字进行运算，所以只需要取前三个运算符即可，把最后一个运算符删去，节省开销:

```Python
def getOperatorList():
    operators = ['+', '-', '*', '//']
    result = []
    
    for operator in set(itertools.permutations(operators)):
        templist = list(operator)
        templist.pop()
        result.append(templist)
    return result
```

#### 核心计算

首先我们考虑最理想的情况，就是当你四个数字依次出现，并且把运算符依次排序好之后，竟然就能神奇的得到24，那这样就能快速的求解，输出结果即可。

这里还要强调一点，我们是通过两两计算得到结果，在Python中提供了一种更加简单和快捷的方法，**eval函数**就可以满足我们的需要。

```Python
expression1 = str(number[0]) + operate[0] + str(number[1]) + operate[1] + str(number[2]) + operate[2] + str(number[3])
            
result = eval(expression1)
            
if result == 24:
    expressionList.append(expression1 + '=' + str(result))
                
```

当然，这样的情况真的是少之又少，所以，还是需要做更好的判断。通过**加括号**的形式进行。我们都知道，括号在这里就是优先级最高的操作，所以加括号，再进行相应的运算，会产生不一样的效果。

```Python
比如

5 * 7 - 10 + 1 = 26

5 * 7 - (10 + 1) = 24
```

这就是括号的魅力所在，放在我们这个程序里，就是在1和我，2和3以及3和4上分别加上括号，已达到优先级的目的。至此，我们所有的流程均已覆盖。

```Python
def calculate(numberList, operatorList):
    
    expressionList = []
    for number in numberList:
        for operate in operatorList:

            expression1 = str(number[0]) + operate[0] + str(number[1]) + operate[1] + str(number[2]) + operate[2] + str(number[3])
            
            try:
                result = eval(expression1)
            except:
                result = 0

            if result == 24:
                expressionList.append(expression1 + '=' + str(result))
                
            else:
                expression2 = '(' + str(number[0]) + operate[0] + str(number[1]) + ')' + operate[1] + str(number[2]) + operate[2] + str(number[3])
                
                try:
                    result = eval(expression2)
                except:
                    result = 0

                if result == 24:
                    expressionList.append(expression2 + '=' + str(result))
                    
                else:
                    expression3 = str(number[0]) + operate[0] + '(' + str(number[1]) + operate[1] + str(number[2]) + ')' + operate[2] + str(number[3])
                    
                    try:
                        result = eval(expression1)
                    except:
                        result = 0
                    
                    if result == 24:
                        expressionList.append(expression3 + '=' + str(result))
                       
                    else:
                        expression4 = str(number[0]) + operate[0] + str(number[1]) + operate[1] + '(' + str(number[2]) + operate[2] + str(number[3]) + ')'
                        
                        try:
                            result = eval(expression4)
                        except:
                            result = 0
                        
                        if result == 24:
                            expressionList.append(expression4 + '=' + str(result))
```

#### 疑惑解答

可能细心的朋友已经看到了，我这里用的是 result == 24 来判断是否符合要求。为什么呢？纯粹是为了我想简单点吗？其实，用我的诡辩来说就是，要从用户的角度来看待问题。

玩这个游戏的都是练习智力游戏的朋友，所以，更多的想到还是用整除来对待这个游戏，比如 8/3 会产生精度问题，通过整除来表现，即 8 // 3 就不会。从玩游戏的角度来看，还是整除这个比较合理，你觉得呢？

当然，从精度的角度来看，在Python 3.5 新增了 math.isclose函数，来增加精度的判断，这里就不进行赘述了。

#### 结果查看

当所有流程都结束，当所有分析都做完，当所有想法都实现，是不是很开心呢？不急不急，这个还有待我们的进一步验证，不然怎么知道你到底是对是错呢。接下来，开启我们的验证。

```Python
numbers = [1,5,7,10]
# 获取打乱的列表
numberList = getNumberList(numbers)

# 获取打乱的运算符
operatorList = getOperatorList()

# 计算是否符合
calculate(numberList, operatorList)

```

运行结果如下：

```Python
5*7-(10+1)=24

```

需要加、减、乘、除，还加上括号的操作，怪不得当初数学不好的我，经常被打败，真香！

Python给了我们一个全新的世界，小时候的梦想终于在我学习完Python之后实现了。现在，谁还敢和我比24点，我一定拿出我这几年写程序的功力来和他一比高下。