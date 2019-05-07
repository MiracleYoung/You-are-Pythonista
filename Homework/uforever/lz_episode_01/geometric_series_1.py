#!/usr/bin/env python
# encoding:utf-8
# @Time    : 2019/5/3 下午3:18

__author__ = 'Uforever I'


a = int(input("Input a(!=0):"))   #还应对输入进行控制：必须是int，且不等于0。
q = int(input("Input q(!=0,1):"))   #还应对输入进行控制：必须是int，且不等于0。
n = int(input("Input n(>0):"))   #还应对输入进行控制：必须是int，且大于0。
#s = 0
#注意：pow() 通过内置的方法直接调用，内置方法会把参数作为整型，而 math 模块则会把参数转换为 float。

#def geometric_series_sum(normal,ratio,pow_num):    #此处pow_num是指最高级数，即最后一项的幂指数。
#    s = 0
#    if pow_num == 0:
#        return normal
#    for i in range(0,pow_num):
#        t = normal*pow(ratio,i)
#        print(t,end=' + ')
#        s += t
#    t = normal*pow(ratio,pow_num)
#    print(t,end=' = ')
#    s += t
#    return(s)    #return s
#
#print(geometric_series_sum(a,q,n))

#应对输入数值进行键盘检测和条件控制。
def get_geos_sum(normal,ratio,pow_num):   #此处pow_num是指最高级数，即最后一项的幂指数。
    if pow_num == 0:                      #当pow_num=1时，即只有首项a。
        return normal
    return normal*ratio**pow_num + get_geos_sum(normal,ratio,pow_num-1)    #加号前为最后一项的表达式。

print(get_geos_sum(a,q,n))


if __name__ == "__main__":
    print(get_geos_sum(1,1,1))
    print(get_geos_sum(2,3,5))
#    print(geometric_series_sum(1,1,1))
#    print(geometric_series_sum(2,3,5))
    print()
    print("The normal formula: ")
    print("a + aq + aq^2 + aq^3 + ... + aq^(n-2) + aq^(n-1) + aq^n = sum")
    print("sum = a(q^n-1)/(q-1)")
    print("The special formula:")
    print("q + q^2 + q^3 + ... + q^(n-1) + q^n = (sum/a)-1。即：(geometric_series_sum(a,q,n)/a)-1")
    print("上面的公式还可以理解为a=q,n(new)=n(old)-1。即：geometric_series_sum(q,q,n-1)")