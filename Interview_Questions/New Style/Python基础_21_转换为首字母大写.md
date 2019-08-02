# Python基础_21_转换为首字母大写

## Question
将"hello world"转换为首字母大写"Hello World"

Solution1
```python
arr = "hello world".____(" ")
new_str = f"{arr[0].____()} {arr[1].____()}"
print(new_str)
```

Solution2
```python
"hello world".title()
```

%!A. split, capitalize, capitalize!%

%!B. join, capital, capital!%

%!C. split, capital, capital!%

%!D. join, capitalize, capitalize!%

----

## Answer
@!A!@

----

## Analysis

思路一：
这个得看清题目是要求两个单词首字母都要大写，如果只是第一个单词首字母大小的话，可以直接使用 capitalize 即可。
所以这里需要做一定转化

思路二：
更加简洁，使用 titile 一步到步。

Solution1
```python
arr = "hello world".split(" ")
new_str = f"{arr[0].capitalize()} {arr[1].capitalize()}"
print(new_str)
```

Solution2
```python
"hello world".title()
```