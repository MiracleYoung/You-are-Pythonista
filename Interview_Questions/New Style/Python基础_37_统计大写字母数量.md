# Python基础_37_统计大写字母数量

## Question
计算一个文件中的大写字母数量？

```python
with open('A.txt') as fs：
    count = 0
    for i in fs.read()：
        if i.____:
            count += 1
print(count)
```

%!A. isupper()!%

%!B. upper()!%

%!C. isbigger()!%

%!D. bigger()!%

----

## Answer
@!A!@

----

## Analysis

```python
with open('A.txt') as fs：
    count = 0
    for i in fs.read()：
        if i.isupper()：
            count += 1
print(count)
```