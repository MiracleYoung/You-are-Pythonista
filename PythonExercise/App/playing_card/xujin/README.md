#> python实现扑克牌比较大小，斗地主的规则

### 规则详情
1. 首先可以打出的牌有个子，对子，三带一，顺子（大于或等于五张），炸弹。(不允许出三张牌的，即三个一样的不带一张牌)
2. 两手牌必须是相同的相同类型的，如个子对个子，对子对对子，顺子对顺子。。。炸弹可以和任何牌相比较,两个王最大。
3. 这里我们假设输入已经合法化，并且输入的牌已经**排好序**了，因为我们的重点在于比较两手牌的大小。
4. 定义J,Q,K,A,2 分别对应11,12,13,14,15,joker和JOKER分别为大王小王,对应数字为16,17。

### 操作环境
* 操作系统：windows10
* python版本：python 3.7
* 代码编辑器：pycharm 2018.2
* 使用模块：无

### 大致思路
1. 定义一个类来对我们的代码进行封装。这个类需要接收两个参数，也就是两手牌的值。两手牌分别使用两个列表存起来。
2. 对传入手牌的值进行格式化，变成我们能比较的值。
3. 进行比较，再将大的手牌格式化回去，返回手牌。

### 具体思路

1. 定义一个`PlayingCard`类，接收两手牌，(两手牌得是一个列表).并且对接收的手牌进行格式化，变成可以直接比较的值。
```python
class PlayingCard():
    # 定义格式化操作的对应值
    format_playing_card_dict = {
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        '10' : 10,
        'J' : 11,
        'Q' : 12,
        'K' : 13,
        'A' : 14,
        '2' : 15,
        'joker' : 16,
        'JOKER' : 17,
    }

    def __init__(self,left_card,right_card):
        self.left_card = self._format_playing_card(left_card)
        self.right_card = self._format_playing_card(right_card)
        
    def _format_playing_card(self,cards):
        '''
        对手牌进行格式化，成为能直接比较的值
        :param cards: 手牌列表
        :return: 返回格式化好的列表
        '''
        for index,card in enumerate(cards):
            if card not in self.format_playing_card_dict:
                raise ValueError('请输入合法的牌')
            cards[index] = self.format_playing_card_dict[card]

        return cards
```

2. 我们将手牌格式化好了，就需要来分析怎样进行比较。因为我们认为输入的手牌是合法的，并且经过排序了的，两者也是可以进行比较的手牌，所以就可能出现以下情况
* 个子与个子比较
* 对子与对子比较
* 三带一与三带一比较
* 顺子与顺子比较
* 炸弹与炸弹比较，但不包含王炸
* 炸弹与其他牌进行比较，不包含王炸
* 包含王炸的比较

这样看起来我们要分七种情况，那么就要写七个方法了。感觉好像有点多啊，还可不可以少点呢？

答案当然是可以的？

因为传入的手牌都是经过排序好了的，并且合法的。那么`个子与个子`、`对子与对子`、`顺子与顺子`、`炸弹与炸弹`这些比较我们都可以只比较最小的一张牌就能够判断出大小了，所以我们可以把这些都写在一个方法里面。

那么这样分下来，我们就只有四种情况了啊。

* 比较列表第一个值（第一张牌）的大小
* 两个都是三带一的比较
* 炸弹与其他牌进行比较，不包含王炸
* 包含王炸的比较

这样分下来就少了一些了啊，完美啊！！！

然后我们就开始编写方法。

① 比较两个列表第一个值（第一张牌）的大小
```python
def _compare_first_value(self):
    '''
    只需要比较第一张牌的情况
    :return: 返回较大的一手牌
    '''
    if self.left_card[0] > self.right_card[0]:
        return self.left_card
    else:
        return self.right_card
```

② 两个都是三带一的比较

两个都是三带一的话，想要比较两手牌的大小，那么我们就得获取到三张牌的是哪一个牌，得到他的值，然后再比较就可以了。

这里我们就需要获取手牌中每一张牌重复的个数。考虑到我么可能其他位置也需要获取手牌中每一张牌的重复个数，这里我们就单独定义一个方法，来获取每一张牌重复的个数。

```python
def _get_every_value_repeat_count(self,cards):
    '''
    给传入的列表中的每个数计数
    => [7,7,7,4] : {7:3,4:1}
    => [7,7,7,7] : {7:4}
    :param cards: 牌的列表
    :return: 返回一个字典，包含不同的每张牌的个数
    '''
    temp_dict = {}
    for card in cards:
        if card not in temp_dict:
            temp_dict[card] = 1
        else:
            temp_dict[card] += 1

    return temp_dict
```

然后我们比较两个三带一的函数就这样写：
```python
def _compare_three_with_one(self):
    '''
    比较两个三带一
    :return: 返回较大的一手牌
    '''
    
    # 分别调用我们的上面写的得到手牌重复个数的方法,得到一个字典
    left_cards_dict = self._get_every_value_repeat_count(self.left_card)
    right_cards_dict = self._get_every_value_repeat_count(self.right_card)

    left_number = right_number = 0

    # 分别从返回的字典中得到重复个数为三的值，就是我们三带一的比较对象
    for key,value in left_cards_dict.items():
        if value == 3:
            left_number = key
            break

    for key,value in right_cards_dict.items():
        if value == 3:
            right_number = key
            break

    if left_number > right_number:
        return self.left_card
    else:
        return self.right_card
```

③ 炸弹和其他牌的比较，但是不包含王炸
```python
def _compare_bomb_and_others(self):
    '''
    炸弹和其他牌的比较
    :return: 返回较大的一手牌
    '''
    if max( self._get_every_value_repeat_count(self.left_card).values() ) == 4:
        return self.left_card
    else:
        return self.right_card
```

果然我们还时会用到`self._get_every_value_repeat_count()`这个方法.这个方法我们定义的是返回一个字典，我们再调用字典的`.values()`方法，就能得到所有的值了。

这里说一下max函数的使用方法：得到一个序列中的最大值并返回该值

* max函数演示
```python
max([2,6,9,4,10,8])     # => 10
```

④ 包含王炸的比较
```python
def _compare_has_two_joker(self):
    '''
    有两个王的比较
    :return: 返回较大的一手牌
    '''
    if self.left_card[0] == 16:
        return self.left_card
    else:
        return self.right_card
```
因为我们传入的手牌是排序好了的，所以我们直接判断第一张牌的值是否为16(也就是小王joker),如果是，那么他就肯定是王炸了，如果不是，那么另外一个肯定是王炸了。因为如果没有王炸我们肯定是不会执行这个函数的。

到这里为止，我们就把所有的比较方法写完了，接下来我们就要判断我们到底该使用哪一种方法了

首先我们可以写一个字典，来存储我们方法的对应表。我们就直接在`__init__()`函数中添加了。
```python
def __init__(self,left_card,right_card):
    self.left_card = self._format_playing_card(left_card)
    self.right_card = self._format_playing_card(right_card)
    self.function_map = {
        1: self._compare_first_value,  # 只用比较第一张牌的大小
        2: self._compare_has_two_joker,  # 有双王的比较
        3: self._compare_three_with_one,  # 都是三带一的比较
        4: self._compare_bomb_and_others,  # 一个炸弹和其他牌的比较
    }
```

然后我们判断出应该使用哪一种方法之后，就返回相应的值就可以了。
```python
def _judge_compare_method(self):
    '''
    判断使用那一中方法比较手牌，
    :return: 返回相应的key
    '''
    left_len = len(self.left_card)
    right_len = len(self.right_card)

    # 首先判断两手牌长度相等的情况
    if left_len == right_len:
        # 都是单个 只需要比较第一张牌
        if left_len == 1:
            return 1
        # 都有两张牌，有两张情况，都是对子，或者为两个王,但是不可能出现两个人都是两个王
        elif left_len == 2:
            # 因为我们的输入默认是已经经过排序了的，所以我们只需要知道第一张牌是否为16，如果是的话，就是双王，有双王的情况
            if self.left_card[0] == 16 or self.right_card[0] == 16:
                return 2
            # 两个对子比较，只需要比较第一张牌的大小
            else:
                return 1
        # 没有牌数等于三的情况,所以就跳过三张牌的情况，分析四张牌的情况。
        # 这里有三种情况，都是三带一，都是炸弹，一个炸弹一个三带一
        elif left_len == 4:
            # 看，这个位置又可以使用我们的`self._get_every_value_repeat_count()`方法了
            left_max_repeat_count = max( self._get_every_value_repeat_count(self.left_card).values() )
            right_max_repeat_count = max( self._get_every_value_repeat_count(self.right_card).values() )
            # 都是三带一或者炸弹情况
            if left_max_repeat_count == right_max_repeat_count:
                # 都是三带一的情况
                if left_max_repeat_count == 3:
                    return 3
                # 都是炸弹的情况，只需要比较第一张牌
                else:
                    return 1
            # 一个三带一，一个炸弹的情况
            else:
                return 4
        # 都是顺子的情况 最少5张牌，最多12张牌，也只需要比较第一张牌
        elif left_len >= 5 and left_len <= 12:
            return 1
        # 处理其他意外情况，应该是不会出现这种情况的
        else:
            return None
    # 两手牌长度不相等的情况 必须得有一个炸弹
    else:
        # 有王炸的情况
        if left_len == 2 or right_len == 2:
            return 3
        # 没有王炸的情况,有一个炸弹的情况
        else:
            return 4
```
到了这一步为止，我们对手牌的比较基本上算是完成了，只是还有一点，我们是对传入进来的手牌进行 格式化的，所以我们需要将手牌变回去，在返回回去。

```python
def _show_playing_card(self,cards):
    '''
    对格式化之后的手牌改变回去
    :param cards: 格式化之后的手牌列表
    :return: 返回改变回去的手牌列表
    '''
    keys_list = list(self.format_playing_card_dict.keys())
    values_list = list(self.format_playing_card_dict.values())
    for index,card in enumerate(cards):
        key_index = values_list.index(card)
        cards[index] = keys_list[key_index]

    return cards
```
这里说一下`list.index(value)`方法。返回列表中传入值得下标，如果不存在这个值，就会抛出`ValueError`的异常.

* list.index(value)用法演示
```python
a = [1,2,3,4,5]
print(a.index(4))   # => 3
print(a.index(6))   # 抛出ValueError的异常
```

好了，到了这一步，我们就将所有的功能函数都写完了，接下来我们个这个类写一个接口函数，然后将我们的结果返回回去。
```python
def compare_two_cards(self):
    '''
    比较两副牌的大小，返回较大的一副牌
    :return:
    '''
    # 得到应该使用哪一种方法的可以
    method_key = self._judge_compare_method()
    # 通过key拿到对应的函数
    method = self.function_map[method_key]
    # 执行函数，得到结果手牌
    cards = method()
    # 对手牌进行可视化
    cards = self._show_playing_card(cards)
    return cards
```

好了，我们的代码终于写完了，可以开心的测试我们的代码了

```python
PlayingCard(['4'],['9']).compare_two_cards()    # => ['9']
PlayingCard(['joker'],['JOKER']).compare_two_cards()    # => ['JOKER']
PlayingCard(['2','2'],['J','J']).compare_two_cards()    # => ['2','2']
PlayingCard(['2','2','2','5'],['8','8','8','joker']).compare_two_cards()    # => ['2','2','2','5']
PlayingCard(['2','2','2','9'],['4','4','4','4']).compare_two_cards()    # => ['4','4','4','4']
PlayingCard(['joker','JOKER'],['K','K','K','K']).compare_two_cards()    # => ['joker','JOKER]
```
