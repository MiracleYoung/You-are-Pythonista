# Python基础_11_合并列表


## Question
合并列表 [1,5,7,9] 和 [2,2,6,8]

----

## Analysis
使用 extend 和 + 都可以。

----

## Answer
```python
a = [1,5,7,9]
b = [2,2,6,8]
a.extend(b)
print(a)
```
