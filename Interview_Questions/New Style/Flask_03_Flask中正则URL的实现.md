# Flask_03_Flask中正则URL的实现

## Question
Flask中正则URL的实现？

@app.route('<URL>')中 URL 显式支持 string、int、float、____ 4 种类型，隐式支持正则。

第一步：写正则类，将匹配到的值设置为 regex 的值。
```python
class RegexUrl(BaseConverter):
    def __init__(self， url_map， *args):
        super(RegexUrl， self).__init__(url_map)
        self.____ = args[0]
```
第二步：把正则类赋值给我们定义的正则规则。
```python
app.url_map.converters['re'] = RegexUrl
```
第三步：在 URL 中使用正则。
```python
@app.route('/____/<re("[a-z]{3}"):id>')
def regex111(id):
    return 'id:%s'%id
```

%!A. Converter, bool, regex, url!%

%!B. Converter,  path, regex, url!%

%!C. BaseConverter, path, regex, regex!%

%!D. BaseConverter, bool, url, url!%

----

## Answer
@!C!@

----

## Analysis

@app.route('<URL>')中 URL 显式支持 string、int、float、path 4 种类型，隐式支持正则。

第一步：写正则类，继承 BaseConverter，将匹配到的值设置为 regex 的值。
```python
class RegexUrl(BaseConverter):
    def __init__(self， url_map， *args):
        super(RegexUrl， self).__init__(url_map)
        self.regex = args[0]
```
第二步：把正则类赋值给我们定义的正则规则。
```python
app.url_map.converters['re'] = RegexUrl
```
第三步：在 URL 中使用正则。
```python
@app.route('/regex/<re("[a-z]{3}"):id>')
def regex111(id):
    return 'id:%s'%id
```