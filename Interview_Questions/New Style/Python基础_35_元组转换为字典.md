# Python基础_35_元组转换为字典

## Question
有元组 ("a","b") 和元组 (1,2)进行，请问print() dict(zip(a, b))) 的打印结果是什么？

%!A. {"a"：1,"b"：2}!%

%!B. {"a"：''b'',1：2}!%

----

## Answer
@!B!@

----

## Analysis

zip 的使用，但是最后记得把 zip 对象再转换为字典。

```python
a = ("a", "b")
b = (1, 2)
print(dict(zip(a, b)))
```