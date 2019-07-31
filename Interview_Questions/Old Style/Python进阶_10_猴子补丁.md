# Python进阶_10_猴子补丁


## Question
什么是猴子补丁？

----

## Answer
猴子补丁（monkey patching)：在运行时动态修改模块、类或函数，通常是添加功能或修正缺陷。猴子补丁在代码运行时内存中）发挥作用，不会修改源码，因此只对当前运行的程序实例有效。因为猴子补丁破坏了封装，而且容易导致程序与补丁代码的实现细节紧密耦合，所以被视为临时的变通方案，不是集成代码的推荐方式。

大概是下面这样的一个效果
```python
def post()：
    print("this is post")
    print("想不到吧")

class Http()：
    @classmethod
    def get(self)：
        print("this is get")


def main()：
    Http.get=post #动态的修改了 get 原因的功能，

if __name__ == '__main__'：
    main()      
    Http.get() 
```