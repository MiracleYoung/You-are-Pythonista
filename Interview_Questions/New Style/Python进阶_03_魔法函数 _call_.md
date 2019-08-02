# Python进阶_03_魔法函数 _call_

## Question
下列选项中，哪一项是魔法函数 _call_的作用（）

%!A. 给类实例增添魔法功能!%

%!B. 可以回调类里面的函数!%

%!C. 把类实例当做函数调用!%

----

## Answer
@!C!@

----

## Analysis

_call_ 可以把类实例当做函数调用。 使用示例如下

```python
class Bar：
    def __call__(self, *args, **kwargs)：
        print('in call')


if __name__ == '__main__'：
    b = Bar()
    b()
```