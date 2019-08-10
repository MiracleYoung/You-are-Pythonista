# Python基础_07_字符串编码


## Question
一个编码为 GBK 的字符串 S，要将其转成 UTF-8 编码的字符串，应如何操作？

----

## Answer
```python
a= "S".encode("gbk").decode("utf-8",'ignore')
print(a)
```
