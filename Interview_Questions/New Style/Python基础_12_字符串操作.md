# Python基础_12_字符串操作


## Question
下列python字符串操作执行结果为True的是（ ）

```python
string='Hello World!'

print(string.islower())

print(string.isspace())

print(string.isupper())

print(string.istitle())
```

%!A. print(string.islower())!%

%!B. print(string.isspace())!%

%!C. print(string.isupper())!%

%!D. print(string.istitle())!%

----

## Answer
@!D!@

----

## Analysis

string.islower()  如果string中包含至少一个区分大小写的字符，并且所有字符都是小写，则返回True，否则返回False 

string.isspace()  如果string中只包含空格，则返回True，否则返回False 

string.isupper()  如果string中字符都是大写，则返回True，否者返回False

string.istitle()  如果string是中所有单词都是以大写的开始，其余都为小写，则返回True，否者返回False 
