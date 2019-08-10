# Python进阶_07_metaclass 作用及应用场景


## Question
metaclass 作用？以及应用场景？

----

## Answer
metaclass 即元类，metaclass 是类似创建类的模板，所有的类都是通过他来 create 的(调用new)，这使得你可以自由的控制创建类的那个过程，实现你所需要的功能。 我们可以使用元类创建单例模式和实现 ORM 模式。