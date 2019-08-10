# Python基础_32_转换为生成器

## Question
请将 [i for i in range(3)] 改成生成器

%!A. (i for i in range(3))!%

%!B. {i for i in range(3)}!%

%!C. generate([i for i in range(3)])!%

%!D. yield([i for i in range(3)])!%

----

## Answer
@!A!@

----

## Analysis

通过把列表生产式的中括号，改为小括号我们就实现了生产器的功能

```python
(i for i in range(3))
```