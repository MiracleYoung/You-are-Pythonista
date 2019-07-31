# 正则_01_Python里面match()和search()的区别


## Question
Python里面match()和search()的区别？

----

## Answer
re 模块中 match(pattern,string[,flags]),检查 string 的开头是否与 pattern 匹配。

re 模块中 research(pattern,string[,flags]),在 string 搜索 pattern 的第一个匹配值。

```python
print(re.match('super', 'insuperable').span())
```
(0, 5)

```python
print(re.match('super', 'insuperable'))
```
None

```python
print(re.search('super', 'superstition').span())
```
(0, 5)

```python
print(re.search('super', 'insuperable').span())
```
(2, 7)
