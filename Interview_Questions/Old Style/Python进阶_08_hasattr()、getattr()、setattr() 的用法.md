# Python进阶_08_hasattr()、getattr()、setattr() 的用法


## Question
hasattr()、getattr()、setattr() 的用法

----

## Answer
这三个方法属于 Python 的反射机制里面的，hasattr 可以判断一个对象是否含有某个属性，getattr 可以充当 get 获取对象属性的作用。而 setattr 可以充当 person.name = "liming"的赋值操作。

代码示例如下：

```python
class Person()：
    def __init__(self)：
        self.name = "liming"
        self.age = 12

    def show(self)：
        print(self.name)
        print(self.age)

    def set_name(self)：
        setattr(Person, "sex", "男")

    def get_name(self)：
        print(getattr(self, "name"))
        print(getattr(self, "age"))
        print(getattr(self, "sex"))


def run()：
    if hasattr(Person, "show")：
        print("判断 Person 类是否含有 show 方法")


    Person().set_name()
    Person().get_name()


if __name__ == '__main__'：
    run()
```