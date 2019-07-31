# Python进阶_04_判断一个对象是函数还是方法


## Question
如何判断一个对象是函数还是方法？

----

## Analysis


----

## Answer
可通过以下这段代码来理解
```python
from types import MethodType, FunctionType

class Bar：
    def foo(self)：
        pass

def foo2()：
    pass

def run()：
    print("foo 是函数", isinstance(Bar().foo, FunctionType))
    print("foo 是方法", isinstance(Bar().foo, MethodType))
    print("foo2 是函数", isinstance(foo2, FunctionType))
    print("foo2 是方法", isinstance(foo2, MethodType))


if __name__ == '__main__'：
    run()


# foo 是函数 False
# foo 是方法 True
# foo2 是函数 True
# foo2 是方法 False
```