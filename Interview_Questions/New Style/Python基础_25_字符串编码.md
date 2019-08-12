# Python基础_25_字符串编码

## Question
一个编码为 GBK 的字符串 S，要将其转成 UTF-8 编码的字符串，应如何操作？

```python
a= "S".____("gbk").____("utf-8",'ignore')
print(a)
```

%!A. encode, decode!%

%!B. decode, encode!%

----

## Answer
@!A!@

----

## Analysis

```python
a= "S".encode("gbk").decode("utf-8",'ignore')
print(a)
```