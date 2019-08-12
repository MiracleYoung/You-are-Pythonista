# Python基础_28_展开列表

## Question
[1,2],[3,4],[5,6]] 一行代码展开该列表，得出 [1,2,3,4,5,6]

```python
l = [[1,2],[3,4],[5,6]]
x=____  
print(x)
```

%!A. [i for i in l for i in j]!%

%!B. [j for i in l for j in i]!%

%!C. [j for i in l for i in l]!%

%!D. [i for j in l for i in l]!%

----

## Answer
@!B!@

----

## Analysis

```python
l = [[1,2],[3,4],[5,6]]
x=[j for i in l for j in i]  
print(x)
```