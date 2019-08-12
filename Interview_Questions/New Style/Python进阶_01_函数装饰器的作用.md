# Python进阶_01_函数装饰器的作用

## Question
函数装饰器有什么作用？请列举说明？

装饰器就是一个函数，它可以在不需要做任何代码变动的前提下给一个函数增加额外功能，启动装饰的效果。 它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。 

下面是一个日志功能的装饰器

```python
from functools import wraps
def log(label)：
    def decorate(func)：
       @____(____) 
       def _wrap(*args,**kwargs)：
        try：
          func(*args,**kwargs)
          print("name",func.__name__)
        except Exception as e：
           print(e.args)
       return _wrap
    return decorate    

____log("info")
def foo(a,b,c)：
     print(a+b+c)
     print("in foo")

#decorate=decorate(foo)   

if __name__ == '__main__'：
    foo(1,2,3)
     #decorate()
```

%!A. wraps, func, @!%

%!B. wraps, func, @!%

%!C. log, decorate, $!%

%!D. log, decorate, $!%

----

## Answer
@!A!@

----

## Analysis

装饰器就是一个函数，它可以在不需要做任何代码变动的前提下给一个函数增加额外功能，启动装饰的效果。 它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。 

下面是一个日志功能的装饰器

```python
from functools import wraps
def log(label)：
    def decorate(func)：
       @wraps(func) 
       def _wrap(*args,**kwargs)：
        try：
          func(*args,**kwargs)
          print("name",func.__name__)
        except Exception as e：
           print(e.args)
       return _wrap
    return decorate    

@log("info")
def foo(a,b,c)：
     print(a+b+c)
     print("in foo")

#decorate=decorate(foo)   

if __name__ == '__main__'：
    foo(1,2,3)
     #decorate()
```