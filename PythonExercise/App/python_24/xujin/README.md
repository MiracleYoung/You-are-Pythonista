#> python实现24点算法

### 什么是24点
给定4个任意数字（0-9），然后通过`+,-,*,/,(,)`，将这4个数字计算出24。

可能有人会觉得很简单，但是真的简单吗？

比如：
* 8，3，3，3
* 7，3，3，3

你能一眼看出来答案吗？

这个时候我们的python就派上用场了，我们可以利用python写一个程序，来返回一个满足符合要求的表达式。

### 大致思路

我们可以这样想，将四个数字进行全排列，然后再他们之间添加运算符号，算符我们也需要进行排列组合，因为我们只有四个数字，所以我们只需要三个操作符，而且操作符时刻重复的，比如三个都是`+`。然后再遍历四个数字的全排列的，然后对每一组数字而言，在遍历所有的组合的操作符，然后再讲数字和操作符进行拼接运算，**应该就能**得到我们的结果了。

### 演示环境
操作系统：windows10
python版本：python 3.7
代码编辑器：pycharm 2018.2
使用模块：math，itertools, collections.abc

### 具体代码

1. 首先我们对所有数字进行去全排列，这里我们使用itertools.permutations来帮助我们完成。

*iertools.permutations 用法演示*
``` python
from itertools import permutations

data_list = permutations([1,2,3,4],2)
for data in data_list:
        print(data)

========结果显示
(1, 2)
(1, 3)
(1, 4)
(2, 1)
(2, 3)
(2, 4)
(3, 1)
(3, 2)
(3, 4)
(4, 1)
(4, 2)
(4, 3)
```

permutations第一个参数是接收一个课迭代的对象，第二个参数指定每次排列时从课迭代对象中选着几个字符进行排列。也可以不传入第二个参数，那么默认就是可迭代对象的长度。并且返回一个生成器。

所以我们需要对我们的的所有数字进行全排列，就可以像下面这样写：
```python
def get_all_data_sequence(data_iter)
    return permutations(data_iter)
```
2. 然后我们需要拿到所有的操作运算符的所有组合方式。这里我们就会使用`itertools.product`函数了。

*itertools.product* 用法演示
```python
from itertools import product

sequence1 = product('ABCD','xy')
sequence2 = product([0,1],repeat=3)

for sequence in sequence1:
    print(sequence)
    
print('-'*30)

for sequence in sequence2:
    print(sequence)
    
==========结果显示
('A','x')
('A','y')
('B','x')
('B','y')
('C','x')
('C','y')
('D','x')
('D','y')
------------------------------
(0, 0, 0)
(0, 0, 1)
(0, 1, 0)
(0, 1, 1)
(1, 0, 0)
(1, 0, 1)
(1, 1, 0)
(1, 1, 1)
```

`itertools.product`,返回传入所有序列中笛卡尔积的元祖epeat参数表示传入序列的重复次数。返回的是一个生成器。

那么我们获取所有的操作运算符就可以通过这个函数来获取了
```python
def get_all_operations_sequence():
    operations = ['+','-','*','/']
    return product(operations,repeat=3)
```
3. 现在我们已经拿到了所有可能组合的操作符合数字了，接下来我们就需要对他们进行拼接了。然后执行运算。

这一步操作我们会用到`itertools.zip_longest()`和`itertools.chain.form_iterable()`函数。

`itertools.zip_longest()` 用法演示
```python
data = zip_longest([1,2,3,4],['*','-','+'],fillvalue='')
for value in data:
    print(value)
    
==========结果显示
(1, '*')
(2, '-')
(3, '+')
(4, '')
```
zip_longest()其实和python内置的zip()函数用法差不多，只是zip_longest是以最长的一个序列为基准，缺失值就使用`fillvalue`参数的值进行填充

`itertools.chain.form_iterable()`用法演示
```python
data = zip_longest([1,2,3,4],['*','-','+'],fillvalue='')
data_chain = chain.from_iterable(data)
for value in data_chain:    
    print(value)
    
==========结果显示
1
*
2
-
3
+
4
```
这里的data是什么样的大家知道了瑟，然后我们将data传入chain.form_iterable()中，它就能将里面的值依次拿出来。

了解了这两个函数之后，那么我们就可以开始拼接我们的数字和操作运算符了。
```python
def calculate(self):
    '''
    计算值，返回对应的表达式和值
    :return:    
    '''    
    for data_sequence in get_all_data_sequence():       
        operation_sequences = get_all_operation_sequence()       
        for operation_sequence in operation_sequences:            
            value = zip_longest(data_sequence, operation_sequence, 
        fillvalue='')            
            value_chain = chain.from_iterable(value)           
            calculate_str = ''           
            # 对得到的字符进行拼接成为表达式 calculate_str
            for _ in value_chain:                
                calculate_str += _          
            try：
                result = eval(calculate_str
            # 处理被除数可能为零的情况，然后就直接跳过这次循环
            except ZeroDivisionError:
                continue
            if math.isclose(result, 24):                    
               return calculate_str,result
    return None,None
```
代码分析：
    1. eval()函数，接受一个字符窜，能让这个字符窜当成python代码运行，返回运行的结果。
    2. math.isclos()：为什么这里需要使用math.isclose(),而不是直接使用`==`运算符呢？这是因为最后算出来的表达式可能有精度问题，例如23.9...或者24.0...等数字，所以我们就需要使用math.isclose()函数来帮助我们判断了两个数字是否相等了，这个函数就有一个精度范围。这样出现上面的情况的时候，我们也能匹配得到我们的条件了。
    
    
这个时候我们运行代码，然后测试我们代码的是否能达到我们的需求。首先我们测试1,2,3,4四个数字，
程序出来了结果 `1*2*3*4` 24.看来好像我们写的代码是正确的.我们再来测试一组数据8,8,3,3.

嗯？然后我们并没有得到结果？这四个数字不能运算出24吗？答案当然是否定的。`8 / ( 3 - 8 / 3 )`这样组合显然是可以的，为什么没有算出来这种结果呢？

这是因为我们没有考虑括号的原因。kuo好是可以改变运算的优先级的。所以我们的吧括号考虑进去。

那么我们的考虑括号最多可以有几个呢？怎样给我们的表达式添加括号呢？

在4个数字的运算中，括号最多只能有三个。并且，在这里，我们使用一种简单的方法添加括号，我们把所有的可能出现括号的情况全部罗列出来，然后我们在将我们得到的运算表达式拼接进去。可能大家会觉得罗列出来所有的括号出现情况不现实，因为有很多情况.其实不然，当我们去罗列的时候，你就会发现，只有11种情况。
```python
FORM_STRS = [
    # 数字 运算符 数字 运算符 数字 运算符 数字
    # 一个括号 的情况
    '(%s %s %s) %s %s %s %s',
    '(%s %s %s %s %s) %s %s',
    '(%s %s %s %s %s %s %s)',
    '%s %s (%s %s %s) %s %s',
    '%s %s (%s %s %s %s %s)',
    '%s %s %s %s (%s %s %s)',
    # 两个括号 的情况
    '(%s %s %s) %s (%s %s %s)',
    '( (%s %s %s) %s %s) %s %s',
    '( %s %s (%s %s %s)) %s %s',
    '%s %s ((%s %s %s) %s %s)',
    '%s %s (%s %s (%s %s %s))',
    # 三个括号是重复的,就不用罗列出来了
]
```
然后我们对得到的表达式在进行遍历拼接，然后我们再运算表达式。这样我们就能得出正确的结果了

项目的完整代码：
```python
from collections.abc import Iterable
from itertools import product,permutations,zip_longest,chain
import math
class Point24():
    OPERATIONS = ('+','-','*','/')
    
    FORM_STRS = [
        # 数字 运算符 数字 运算符 数字 运算符 数字
        # 一个括号 的情况
        '(%s %s %s) %s %s %s %s',
        '(%s %s %s %s %s) %s %s',
        '(%s %s %s %s %s %s %s)',
        '%s %s (%s %s %s) %s %s',
        '%s %s (%s %s %s %s %s)',
        '%s %s %s %s (%s %s %s)',
        # 两个括号 的情况
        '(%s %s %s) %s (%s %s %s)',
        '( (%s %s %s) %s %s) %s %s',
        '( %s %s (%s %s %s)) %s %s',
        '%s %s ((%s %s %s) %s %s)',
        '%s %s (%s %s (%s %s %s))',
        # 三个括号是重复的,就不用罗列出来了
    ]
    
    def __init__(self,data_iter):
        if not isinstance(data_iter, Iterable):
            raise TypeError(f'{data_iter} cat`t iter')
        self.data_iter = data_iter
        
    def _get_all_operation_sequence(self):
        '''        
        从self.OPERATIONS选取任意个数的字符，组成一个元祖，        返回一个生成器 
        :return:       
        '''        
        return product(self.OPERATIONS,repeat=3)
        
    def _get_all_data_sequence(self):
        '''       
        对传入的数字进行全排列，返回一个生成器        
        :return:       
        '''        
        return permutations(self.data_iter)
        
    def _format_str(self,calculate_str):
        for format_str in self.FORM_STRS:
            yield format_str % (                
                calculate_str[0],               
                calculate_str[1],               
                calculate_str[2],                
                calculate_str[3],                
                calculate_str[4],               
                calculate_str[5],                
                calculate_str[6]            
                )   
            
    def calculate(self):
        '''       
        计算值，返回对应的表达式和值       
        :return:        
        '''       
        for data_sequence in self._get_all_data_sequence():           
            operation_sequences = self._get_all_operation_sequence()            
            for operation_sequence in operation_sequences:                
                value = zip_longest(data_sequence, operation_sequence, fillvalue='')                
                value_chain = chain.from_iterable(value)                
                calculate_str = ''                
                for _ in value_chain:                   
                    calculate_str += _           
                    
                for finally_calculate_str in self._format_str(calculate_str):                   
                    try:                        
                        result = eval(finally_calculate_str)                    
                    except ZeroDivisionError:                       
                        continue                  
                        
                    if math.isclose(result, 24):                       
                        return finally_calculate_str, result        
                        
        return None,None
        
if __name__ == '__main__':
    input_str = input('请输入数字（0-9），每个数字之间使用`,`隔开:')    
    data_list = input_str.split(',')    
    for data in data_list:        
        try:            
            if int(data) < 0 or int(data) > 9:                
            raise ValueError('请输入0-9之间的数字')        
        except TypeError:            
            raise TypeError('请输入格式正确的数')    
            
    print(Point24(data_list).calculate())
```

呼。。。代码终于写完了，终于可以开始运行我们的程序了
* 8,8,3,3      -->    `8 / (3 - 8 / 3)`
* 7,7,3,3      -->    `7 * (3 / 7 + 3)`
* 3,2,5,8      -->    `(3 + 2 * 8) + 5`
* 5,5,5,1      -->    `5 * (5 - 1 / 5)`
* 9,5,7,4      -->    `9 + 5 * (7 - 4)`