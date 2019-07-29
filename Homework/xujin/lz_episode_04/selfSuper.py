from types import MethodType

class Super():
    def __init__(self,type,obj):
        self.type = type
        self.obj = obj

    def __getattr__(self, name):
        # name 即为属性的`名字`
        is_super = False
        mro = self.type.__mro__
        for _class in mro:
            if is_super and hasattr(_class,name):
                # return self.obj.name
                # MethodType(将函数绑定到对象)
                return MethodType(getattr(_class,name),self.obj)
            if _class == self.type:
                is_super= True
        raise AttributeError(f'{self.type} parents don`t have {name} method or attribute')

class Base():
    def method(self):
        print(self)
        print('base')

class A(Base):
    def method(self):
        Super(A,self).method1()
        print('a')


if __name__=='__main__':
    A().method()
    # mro = A.__mro__
    # A().method()
    # help(super)