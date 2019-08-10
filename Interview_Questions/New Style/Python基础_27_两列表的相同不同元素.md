# Python基础_27_两列表的相同不同元素

## Question
给定两个 list，A 和 B，找出相同元素和不同元素的方法分别是什么？

%!A. set(A).intersection(set(B)),set(A).difference(set(B))!%

%!B. set(A).intersection_update(set(B)),set(A).difference_update(set(B))!!%

----

## Answer
@!A!@

----

## Analysis
还能有以下方法：

A、B 中相同元素
```python
print(set(A)&set(B)) 
```

A、B 中不同元素
```python
print(set(A)-set(B)) 
```