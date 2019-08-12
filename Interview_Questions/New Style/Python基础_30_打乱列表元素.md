# Python基础_30_打乱列表元素

## Question
如何打乱一个列表的元素？

```python
import random

a = [1, 2, 3, 4, 5]
print(a)

#a = [2, 4, 5, 1, 3]
```

%!A. random.shuffle(a)!%

%!B. random.change(a)!%

%!C. random.mix(a)!%

----

## Answer
@!A!@

----

## Analysis

```python
import random

a = [1, 2, 3, 4, 5]
random.shuffle(a)
print(a)
```