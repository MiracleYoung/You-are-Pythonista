# Python基础_34_合并字典

## Question
请合并下面两个字典 a = {"A"：1,"B"：2},b = {"C"：3,"D"：4}

%!A. a+b!%

%!B. a.update(b)!%

%!C. a.update(bdict(a,b)!%

----

## Answer
@!B!@

----

## Analysis

合并字典方法很多，可以使用 a.update(b) 或者 字典解包的方式

```python
a = {"A"：1,"B"：2}
b = {"C"：3,"D"：4}
print({**a,**b})
```
