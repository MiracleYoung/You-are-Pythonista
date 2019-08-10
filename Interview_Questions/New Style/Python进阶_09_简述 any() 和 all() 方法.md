# Python进阶_09_简述 any() 和 all() 方法

## Question
简述 any() 和 all() 方法，错误的是（）

#any(x)  all(x)
%!A. any => x都为空、0、False返回False!%

%!B. any => x不都为空、0、False返回False!%

%!C. all => x都为空、0、False返回True!%

%!D. all => x不都为空、0、False返回True!%

----

## Answer
@!A!@

----

## Analysis

any(x)：判断 x 对象是否为空对象，如果都为空、0、false，则返回 false，如果不都为空、0、false，则返回 true。 all(x)：如果 all(x) 参数 x 对象的所有元素不为 0、''、False 或者 x 为空对象，则返回 True，否则返回 False。