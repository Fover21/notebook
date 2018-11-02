********装饰器的形成过程********

1）装饰器简单版本

import time

def func1():
    print('in func1')

def timer(func):
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner

func1 = timer(func1)
func1()


2）装饰器----语法糖

import time
def timer(func):
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner

@timer   #==> func1 = timer(func1)
def func1():
    print('in func1')

func1()

总结：
装饰器的本质：一个闭包函数
装饰器的功能：在不修改原函数及其调用方式的情况下对原函数功能进行扩展


3）装饰器——带参数的装饰器

def timer(func):
    def inner(a):
        start = time.time()
        func(a)
        print(time.time() - start)
    return inner

@timer
def func1(a):
    print(a)

func1(1)


4）装饰器——成功hold住所有函数传参

import time
def timer(func):
    def inner(*args,**kwargs):
        start = time.time()
        re = func(*args,**kwargs)
        print(time.time() - start)
        return re
    return inner

@timer   #==> func1 = timer(func1)
def func1(a,b):
    print('in func1')

@timer   #==> func2 = timer(func2)
def func2(a):
    print('in func2 and get a:%s'%(a))
    return 'fun2 over'

func1('aaaaaa','bbbbbb')
print(func2('aaaaaa'))


5）装饰器——带返回值的装饰器

import time
def timer(func):
    def inner(*args,**kwargs):
        start = time.time()
        re = func(*args,**kwargs)
        print(time.time() - start)
        return re
    return inner

@timer   #==> func2 = timer(func2)
def func2(a):
    print('in func2 and get a:%s'%(a))
    return 'fun2 over'

func2('aaaaaa')
print(func2('aaaaaa'))


****补充****

1）查看函数信息的一些方法

def index():
    '''这是一个主页信息'''
    print('from index')

print(index.__doc__)    #查看函数注释的方法
print(index.__name__)   #查看函数名的方法

2）装饰器——wraps demo

from functools import wraps

def deco(func):
    @wraps(func) #加在最内层函数正上方
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

@deco
def index():
    '''哈哈哈哈'''
    print('from index')

print(index.__doc__)
print(index.__name__)


**总结**

1）开放封闭原则

　　1.对扩展是开放的

　　　　为什么要对扩展开放呢？

　　　　我们说，任何一个程序，不可能在设计之初就已经想好了所有的功能并且未来不做任何更新和修改。所以我们必须允许代码扩展、添加新功能。

　　2.对修改是封闭的

　　　　为什么要对修改封闭呢？

　　　　就像我们刚刚提到的，因为我们写的一个函数，很有可能已经交付给其他人使用了，如果这个时候我们对其进行了修改，很有可能影响其他已经在使用该函数的用户。

装饰器完美的遵循了这个开放封闭原则。



2）装饰器的主要功能和装饰器的固定结构

装饰器的主要功能：在不改变函数调用方式的基础上在函数的前、后添加功能。

装饰器的固定格式：

（1）装饰器的固定格式

def timer(func):
    def inner(*args,**kwargs):
        '''执行函数之前要做的'''
        re = func(*args,**kwargs)
        '''执行函数之后要做的'''
        return re
    return inner

（2）装饰器的固定格式——wraps版

from functools import wraps

def deco(func):
    @wraps(func) #加在最内层函数正上方
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper



****补充****

1）带参数的装饰器

def outer(flag):
    def timer(func):
        def inner(*args,**kwargs):
            if flag:
                print('''执行函数之前要做的''')
            re = func(*args,**kwargs)
            if flag:
                print('''执行函数之后要做的''')
            return re
        return inner
    return timer

@outer(False)
def func():
    print(111)

func()

2）多个装饰器装饰同一个函数

def wrapper1(func):
    def inner():
        print('wrapper1 ,before func')
        func()
        print('wrapper1 ,after func')
    return inner

def wrapper2(func):
    def inner():
        print('wrapper2 ,before func')
        func()
        print('wrapper2 ,after func')
    return inner

@wrapper2
@wrapper1
def f():
    print('in f')

f()