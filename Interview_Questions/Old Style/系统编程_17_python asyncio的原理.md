# 系统编程_17_python asyncio的原理？


## Question
python asyncio的原理？

----

## Answer
asyncio这个库就是使用python的yield这个可以打断保存当前函数的上下文的机制， 封装好了selector 摆脱掉了复杂的回调关系
