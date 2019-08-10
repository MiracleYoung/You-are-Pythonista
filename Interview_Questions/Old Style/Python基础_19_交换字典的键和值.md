# Python基础_19_交换字典的键和值


## Question
如何交换字典 {"A"：1,"B"：2}的键和值

----

## Answer
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