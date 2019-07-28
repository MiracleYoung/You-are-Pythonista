# Python基础_06_列表的合并


## Question
合并如下两个列表

```python
a = [1,5,7,9]
b = [2,2,6,8]

# [1, 5, 7, 9, 2, 2, 6, 8]
```

%!A. a.append(b)!%

%!B. a.extend(b)!%

%!C. a.add(b)!%


----

## Answer
@!B!@

----

## Analysis

```python
a.append(b)  # [1, 5, 7, 9, [2, 2, 6, 8]]
a.extend(b)  # [1, 5, 7, 9, 2, 2, 6, 8]
a.add(b) # AttributeError: 'list' object has no attribute 'add'
```
