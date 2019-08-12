# Python基础_20_统计大写字母数量


## Question
计算一个文件中的大写字母数量？

----

## Answer
```python
with open('A.txt') as fs：
    count = 0
    for i in fs.read()：
        if i.isupper()：
            count += 1
print(count)
```