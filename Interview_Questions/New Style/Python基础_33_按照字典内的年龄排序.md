# Python基础_33_按照字典内的年龄排序

## Question
按照字典内的年龄排序

```python
d1 = [
    {'name'：'alice', 'age'：38},
    {'name'：'bob', 'age'：18},
    {'name'：'Carl', 'age'：28},
]
```

%!A. sorted(d1, key="age")!%

%!B. sorted(d1, key=lambda x：x["age"])!%

%!C. sort(d1, key="age")!%

%!D. sort(d1, key=lambda x：x["age"])!%

----

## Answer
@!B!@

----

## Analysis

```python
d1 = [
    {'name'： 'alice', 'age'： 38},
    {'name'： 'bob', 'age'： 18},
    {'name'： 'Carl', 'age'： 28},
]

print(sorted(d1, key=lambda x：x["age"]))
```