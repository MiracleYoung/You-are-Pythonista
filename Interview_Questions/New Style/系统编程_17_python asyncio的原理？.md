# 系统编程_17_python asyncio的原理？

## Question
python asyncio 的原理？

asyncio 这个库就是使用 python 的 yield 这个可以打断保存当前函数的上下文的机制， 封装好了 selector， 摆脱掉了复杂的回调关系

%!A. break!%

%!B. yield!%

%!C. generator!%

%!D. content!%

----

## Answer
@!B!@

----

## Analysis

asyncio 这个库就是使用 python 的 yield 这个可以打断保存当前函数的上下文的机制， 封装好了 selector 摆脱掉了复杂的回调关系