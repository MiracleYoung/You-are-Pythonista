# Python进阶_07_metaclass 作用及应用场景

## Question
下面关于 metaclass 的说法，错误的是（）

%!A. metaclass 即元类!%

%!B. 不能使用元类创建单例模式!%

%!C. 可以使用元类实现 ORM 模式!%

%!D. metaclass 类似创建类的模板!%

----

## Answer
@!B!@

----

## Analysis

metaclass 即元类，metaclass 是类似创建类的模板，所有的类都是通过他来 create 的(调用new)，这使得你可以自由的控制创建类的那个过程，实现你所需要的功能。 我们可以使用元类创建单例模式和实现 ORM 模式。