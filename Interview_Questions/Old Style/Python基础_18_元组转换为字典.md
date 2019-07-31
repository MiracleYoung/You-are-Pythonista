# Python基础_18_元组转换为字典


## Question
如何把元组 ("a","b") 和元组 (1,2)，变为字典 {"a"：1,"b"：2}

----

## Analysis
zip 的使用，但是最后记得把 zip 对象再转换为字典。

----

## Answer
```python
a = ("a", "b")
b = (1, 2)
print(dict(zip(a, b)))
```