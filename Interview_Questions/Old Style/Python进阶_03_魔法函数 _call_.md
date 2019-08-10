# Python进阶_03_魔法函数 _call_


## Question
魔法函数 _call_怎么使用?

----

## Answer
_call_ 可以把类实例当做函数调用。 使用示例如下

```python
class Bar：
    def __call__(self, *args, **kwargs)：
        print('in call')


if __name__ == '__main__'：
    b = Bar()
    b()
```
