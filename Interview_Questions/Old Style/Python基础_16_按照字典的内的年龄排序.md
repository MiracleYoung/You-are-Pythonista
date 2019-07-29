# Python基础_16_按照字典的内的年龄排序


## Question
按照字典的内的年龄排序

```python
d1 = [
    {'name'：'alice', 'age'：38},
    {'name'：'bob', 'age'：18},
    {'name'：'Carl', 'age'：28},
]
```
----

## Analysis


----

## Answer
```python
d1 = [
    {'name'： 'alice', 'age'： 38},
    {'name'： 'bob', 'age'： 18},
    {'name'： 'Carl', 'age'： 28},
]

print(sorted(d1, key=lambda x：x["age"]))
```
