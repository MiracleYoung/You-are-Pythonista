# Python基础_10_展开列表


## Question
[1,2],[3,4],[5,6]] 一行代码展开该列表，得出 [1,2,3,4,5,6]

----

## Answer
```python
l = [[1,2],[3,4],[5,6]]
x=[j for i in l for j in i]  
print(x)
```
