import itertools
import math

def getNumberList(numbers):
    result = []

    for number in set(itertools.permutations(numbers)):
        result.append(list(number))

    return result


def getOperatorList():
    operators = ['+', '-', '*', '//']
    result = []
    for operator in set(itertools.permutations(operators)):
        templist = list(operator)
        templist.pop()
        result.append(templist)
    return result
# 全排列

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
                            

    for each in expressionList:
        print(each)
        break;
   



numbers = [8,8,3,3]
# 获取打乱的列表
numberList = getNumberList(numbers)

# 获取打乱的运算符
operatorList = getOperatorList()

# 计算是否符合
calculate(numberList, operatorList)
