# Python基础_36_交换字典的键和值

## Question
如何交换字典 {"A"：1,"B"：2}的键和值，下列方法正确的是？

```python
s =  {"A"：1,"B"：2}

#dict_new = {1: 'A', 2: 'B'}
```
%!A. dict_new = {value:key for key，value in s.items()}!%

%!B. new_s= dict(zip(s.values()，s.keys()))!%

%!C. A和B!%

----

## Answer
@!C!@

----

## Analysis

Solution1
```python
s =  {"A"：1,"B"：2}
dict_new = {value:key for key，value in s.items()}
```

Solution2
```python
s =  {"A"：1,"B"：2}
new_s= dict(zip(s.values()，s.keys()))
```