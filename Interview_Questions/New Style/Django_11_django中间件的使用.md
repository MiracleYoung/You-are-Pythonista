# Django_11_django中间件的使用？

## Question
Django 中间件的使用？

Django 在中间件中预置了六个方法，这六个方法的区别在于不同的阶段执行，对输入或输出进行干预，方法如下：

1.初始化：无需任何参数，服务器响应第一个请求的时候调用一次，用于确定是否启用当前中间件
```python
def __init__():
    pass
```
2.处理请求前：在每个请求上调用，返回 None 或 HttpResponse 对象。
```python
def process_request(____):
    pass
```
3.处理视图前:在每个请求上调用，返回 None 或 HttpResponse 对象。
```python
def process_view(request,____,view_args,view_kwargs):
    pass
```
4.处理模板响应前：在每个请求上调用，返回实现了 render 方法的响应对象。
```python
def process_template_response(request,____):
    pass
```
5.处理响应后：所有响应返回浏览器之前被调用，在每个请求上调用，返回 HttpResponse 对象。
```python
def process_response(request,response):
    pass
```
6.异常处理：当视图抛出异常时调用，在每个请求上调用，返回一个 HttpResponse 对象。
```python
def process_exception(request,____):
    pass
```

%!A. response, view_func, response, exception!%

%!B. request, view_func, response, exception!%

%!C. request, response, template, exception!%

%!D. response, response, template, response!%

----

## Answer
@!B!@

----

## Analysis

Django 在中间件中预置了六个方法，这六个方法的区别在于不同的阶段执行，对输入或输出进行干预，方法如下：

1.初始化：无需任何参数，服务器响应第一个请求的时候调用一次，用于确定是否启用当前中间件
```python
def __init__():
    pass
```
2.处理请求前：在每个请求上调用，返回 None 或 HttpResponse 对象。
```python
def process_request(request):
    pass
```
3.处理视图前:在每个请求上调用，返回 None 或 HttpResponse 对象。
```python
def process_view(request,view_func,view_args,view_kwargs):
    pass
```
4.处理模板响应前：在每个请求上调用，返回实现了 render 方法的响应对象。
```python
def process_template_response(request,response):
    pass
```
5.处理响应后：所有响应返回浏览器之前被调用，在每个请求上调用，返回 HttpResponse 对象。
```python
def process_response(request,response):
    pass
```
6.异常处理：当视图抛出异常时调用，在每个请求上调用，返回一个 HttpResponse 对象。
```python
def process_exception(request,exception):
    pass
```

