# Python基础_04_检测字符串中只含有数字


## Question
如何检测字符串中只含有数字?

----

## Analysis
可以通过 isdigit 方法

----

## Answer
```python
s1 = "12223".isdigit()
print(s1)

s2 = "12223a".isdigit()
print(s2)

# 结果如下：
# True
# False
```
