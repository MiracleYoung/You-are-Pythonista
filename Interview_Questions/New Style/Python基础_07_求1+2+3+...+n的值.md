# Python基础_07_求1+2+3+...+n的值


## Question
求1+2+3+...+n的值

```python
sum(list(range(__, __)))
```

%!A. 1  n!%

%!B. 1  n+1!%

%!C. 0  n!%

%!D. 0  n!%

----

## Answer
@!B!@

----

## Analysis
```python
range(start, stop[, step])
```
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）

stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5

step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

